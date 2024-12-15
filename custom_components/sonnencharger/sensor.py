import json
import logging

from .coordinator import SonnenChargerCoordinator
from .mappings_ha import SENSORMAP

from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
)

from homeassistant.components.sensor import (
    SensorEntity,
    SensorEntityDescription,
)

from homeassistant.const import EntityCategory
from homeassistant.helpers.typing import StateType

# pylint: disable=no-name-in-module
from sonnencharger import sonnencharger
from collections.abc import Callable
from dataclasses import dataclass
# pylint: enable=no-name-in-module

from .const import (
    CONF_IP_ADDRESS,
    CONF_PORT,
    CONF_SCAN_INTERVAL,
    ATTR_SONNEN_DEBUG,
    DOMAIN
)

LOGGER = logging.getLogger(__name__)

@dataclass(frozen=True, kw_only=True)
class SonnenChargerSensorEntityDescription(SensorEntityDescription):
   """Describes sensor entity."""
   value_fn: Callable[[SonnenChargerCoordinator], StateType]


async def async_unload_entry(hass, entry):
   """Unload a config entry."""
   return

async def async_setup_entry(hass, config_entry, async_add_entities):
   """Setup the sensor platform."""
   sc_host   = config_entry.data.get(CONF_IP_ADDRESS)
   sc_port   = config_entry.data.get(CONF_PORT)
   sc_update = config_entry.data.get(CONF_SCAN_INTERVAL)
   sc_debug  = config_entry.data.get(ATTR_SONNEN_DEBUG)

   def _internal_setup(_sc_host, _sc_port):
      return sonnencharger(_sc_host, _sc_port)
   
   sc_charger = await hass.async_add_executor_job(_internal_setup, sc_host, sc_port)
   sc_update = sc_update or 10

   """The coordinator is called from HA"""
   coordinator = SonnenChargerCoordinator(
      hass,
      sc_charger,
      sc_update,
      sc_host,
      sc_port,
      sc_debug,
      config_entry.entry_id
   )

   await coordinator.async_config_entry_first_refresh()

   async_add_entities(
      SonnenChargerSensor(coordinator=coordinator, entity_description=description)
      for description in generate_sensors(_coordinator=coordinator)
   )

def generate_sensors(_coordinator):
   sensor_list: list[SonnenChargerSensorEntityDescription] = []
   prefix = f"sensor.{DOMAIN}_{_coordinator.latest_data["sysinfo"]["serial"]}"
 
   for skey in SENSORMAP["sysinfo"]:
      # This becomes the Entity ID
      sensor_name = f"{prefix}_{skey}"
      # This is the translation key
      sensor_key  = f"{skey}"
      LOGGER.warning(f"Sensor List: {sensor_key} {sensor_name}")
      sensor_list.append(
         SonnenChargerSensorEntityDescription(
            key=sensor_key,
            name=sensor_name,
            # translation_key=key,
            force_update=True,
            state_class=SENSORMAP["sysinfo"][skey]["state_class"],
            device_class=SENSORMAP["sysinfo"][skey]["device_class"],
            value_fn=lambda coordinator, _index=skey: coordinator.latest_data.get("sysinfo", {}).get(_index)
         )
      )

   num_connectors = _coordinator.latest_data["sysinfo"]["connectors"]
   for cur_conn in range(0, num_connectors):
      prefix = f"sensor.{DOMAIN}_{_coordinator.latest_data["sysinfo"]["serial"]}_conn{cur_conn}"
      for key in SENSORMAP["connectors"]:
         # This becomes the Entity ID
         sensor_name = f"{prefix}_{key}"
         # This is the translation key
         sensor_key  = f"{key}"
         LOGGER.warning(f"Sensor List: {sensor_key} {sensor_name}")
         sensor_list.append(
            SonnenChargerSensorEntityDescription(
               key=sensor_key,
               name=sensor_name,
               # translation_key=key,
               force_update=True,
               state_class=SENSORMAP["connectors"][key]["state_class"],
               native_unit_of_measurement=SENSORMAP["connectors"][key]["native_unit_of_measurement"],
               device_class=SENSORMAP["connectors"][key]["device_class"],
               suggested_display_precision=( 
                  val
                  if (val := SENSORMAP["connectors"][key].get("precision"))
                  else None
                ),
               value_fn=lambda coordinator, _conn=cur_conn, _index=key: coordinator.latest_data.get("connectors", {}).get(_conn, {}).get(_index, None)
            )
         )


   return sensor_list

class SonnenChargerSensor(CoordinatorEntity[SonnenChargerCoordinator], SensorEntity):
   _attr_should_poll = False
   # _attr_has_entity_name = True
   entity_description: SonnenChargerSensorEntityDescription

   def __init__(
         self,
         coordinator: SonnenChargerCoordinator, 
         entity_description: SonnenChargerSensorEntityDescription,
      ) -> None:
      super().__init__(coordinator=coordinator)
      self.coordinator = coordinator
      self.entity_description = entity_description
      self._attr_device_info = coordinator.device_info

   @property
   def unique_id(self) -> str:
      """Return a uniqe id."""
      return f"{self.coordinator.serial}_{self.entity_description.key}"
   
   @property
   def native_value(self) -> StateType:
      """Return sensor state."""
      return self.entity_description.value_fn(self.coordinator)

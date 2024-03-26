"""The data update coordinator for SonnenCharger."""

import traceback

from .const import (
    DOMAIN,
    LOGGER,
    logging,
    timedelta
)

from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator
)

from sonnencharger import sonnencharger
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

class SonnenChargerCoordinator(DataUpdateCoordinator):
   """The SonnenChargerCoordinator class."""

   def __init__(
      self,
      hass: HomeAssistant,
      charger: sonnencharger,
      update_interval_seconds: int,
      ip_address,
      port,
      debug_mode,
      device_id
   ):
      """Initialize SonnenCharger coordinator."""
      super().__init__(
         hass,
         _LOGGER,
         name = f"sonnencharger-{device_id}",
         update_interval = timedelta(seconds=update_interval_seconds),
      )
      self.sensor = None
      self.hass = hass
      self.disabled_sensors = []
      self.latest_data = {}
      self.device_id = device_id

      self.stopped = False

      self.charger: sonnencharger = charger
      self.meter_sensors = {}
      self.update_interval_seconds = update_interval_seconds
      self.ip_address = ip_address
      self.port = port

      self.debug = debug_mode
      self.full_logs_already_sent = False
      
      self.serial = ""

   @property
   def device_info(self) -> DeviceInfo:
      system_info = self.latest_data["sysinfo"]

      return DeviceInfo(
         identifiers={(DOMAIN, self.device_id)},
         configuration_url=f"http://{self.ip_address}",
         manufacturer="Sonnen (Etrel)",
         model=system_info.get("model", "unknown"),
         name=f"{DOMAIN}_{system_info.get("serial", "unkown")}",
         sw_version=system_info.get("swrevision", "unknown"),
         hw_version=system_info.get("hwrevision", "unknown"),
   )

   async def _async_update_data(self):
      """Fetch data from API endpoint
      Here is the place to pre-process the data to lookup tables
      for the different entities
      """
      try:
         self.latest_data["sysinfo"] = await self.hass.async_add_executor_job(
            self.charger.get_sysinfo
         )
         self.latest_data["connectors"] = await self.hass.async_add_executor_job(
            self.charger.get_connectors
         )
      except:
         LOGGER.error(traceback.format_exc())

      if self.debug:
         self.send_all_data_to_log()

      if self.serial == "":
         if "serial" in self.latest_data["sysinfo"]:
            self.serial = self.latest_data["sysinfo"]["serial"]
         else:
            self.serial = "unknown"

   def send_all_data_to_log(self):
      if not self.full_logs_already_sent:
         LOGGER.warning("System data:")
         LOGGER.warning(self.latest_data["sysinfo"])
         LOGGER.warning("Connectors")
         LOGGER.warning(self.latest_data["connectors"])
         self.full_logs_already_sent = True

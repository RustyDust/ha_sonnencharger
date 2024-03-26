"""The Sonnenbatterie integration."""
from .const import *
import json
from homeassistant.helpers import config_validation as cv
from homeassistant.const import CONF_SCAN_INTERVAL, Platform
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

# async def async_setup(hass, config):
#     hass.data.setdefault(DOMAIN, {})
#     """Set up a skeleton component."""
#     return True

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry):
    # LOGGER.warning("setup_entry: "+json.dumps(dict(config_entry.data)))
    hass.async_add_job(hass.config_entries.async_forward_entry_setup(config_entry, Platform.SENSOR))
    config_entry.add_update_listener(update_listener)
    return True

async def async_reload_entry(hass, entry):
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)

async def async_unload_entry(hass, entry):
    return await hass.config_entries.async_forward_entry_unload(entry, Platform.SENSOR)

async def update_listener(hass, entry):
    # LOGGER.warning("Update listener" + json.dumps(dict(entry.options)))
    hass.data[DOMAIN][entry.entry_id]["monitor"].updateIntervalSeconds=entry.options.get(CONF_SCAN_INTERVAL)

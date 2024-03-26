import logging
import voluptuous as vol

from datetime import timedelta

from homeassistant.helpers import config_validation as cv
from homeassistant.const import (
    CONF_PORT,
    CONF_IP_ADDRESS,
    CONF_SCAN_INTERVAL,
    Platform
)

LOGGER = logging.getLogger(__package__)

DOMAIN = "sonnencharger"

DEFAULT_SCAN_INTERVAL = 10

CONFIG_SCHEMA_A = vol.Schema(
  {
    vol.Required(CONF_IP_ADDRESS): str,
    vol.Required(CONF_PORT): cv.positive_int,
    vol.Optional(CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL): cv.positive_int
  }
)

CONFIG_SCHEMA = vol.Schema(
  {DOMAIN: CONFIG_SCHEMA_A},
  extra=vol.ALLOW_EXTRA,
)

ATTR_SONNEN_DEBUG = "sonnencharger_debug"
DEFAULT_SONNEN_DEBUG = False
PLATFORMS: list[Platform] = [ Platform.SENSOR ]

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass
)

SENSORMAP = {
   'sysinfo': {
      'connectors': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               None,
      },
      'hwrevision': {
         'state_class':                None,
         'device_class':               None,
      },
      'model': {
         'state_class':                None,
         'device_class':               None,
      },
      'serial': {
         'state_class':                None,
         'device_class':               None,

      },
      'swrevision': {
         'state_class':                None,
         'device_class':               None,
      },
   },
   'connectors': {
      'active_session_duration': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.DURATION,
         'native_unit_of_measurement': "s",
      },
      'active_session_imported_energy': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.ENERGY_STORAGE,
         'native_unit_of_measurement': "kWh",
         'precision':                  2,
      },
      'ev_max_phase_current': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.CURRENT,
         'native_unit_of_measurement': "A",
         'precision':                  2,
      },
      'ev_max_power': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.POWER,
         'native_unit_of_measurement': "kW",
         'precision':                  2,
      },
      'ev_required_energy': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.POWER,
         'native_unit_of_measurement': "kW",
         'precision':                  2,
      },
      'l1_active_power': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.POWER,
         'native_unit_of_measurement': "kW",
         'precision':                  2,
      },
      'l1_current': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.CURRENT,
         'native_unit_of_measurement': "A",
         'precision':                  2,
      },
      'l1_ln_voltage': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.VOLTAGE,
         'native_unit_of_measurement': "V",
         'precision':                  2,
      },
      'l1_phase': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               None,
         'native_unit_of_measurement': None,
      },
      'l2_active_power': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.POWER,
         'native_unit_of_measurement': "kW",
         'precision':                  2,
      },
      'l2_current': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.CURRENT,
         'native_unit_of_measurement': "A",
         'precision':                  2,
      },
      'l2_ln_voltage': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.VOLTAGE,
         'native_unit_of_measurement': "V",
         'precision':                  2,
      },
      'l2_phase': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               None,
         'native_unit_of_measurement': None,
      },
      'l3_active_power': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.POWER,
         'native_unit_of_measurement': "kW",
         'precision':                  2,
      },
      'l3_current': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.CURRENT,
         'native_unit_of_measurement': "A",
         'precision':                  2,
      },
      'l3_ln_voltage': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.VOLTAGE,
         'native_unit_of_measurement': "V",
         'precision':                  2,
      },
      'l3_phase': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               None,
         'native_unit_of_measurement': None,
      },
      'max_current': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.CURRENT,
         'native_unit_of_measurement': "A",
         'precision':                  2,
      },
      'net_frequency': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.FREQUENCY,
         'native_unit_of_measurement': "Hz",
         'precision':                  2,
      },
      'num_phases': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               None,
         'native_unit_of_measurement': None,
      },
      'power_factor': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.POWER_FACTOR,
         'native_unit_of_measurement': "%",
         'precision':                  2,
      },
      'session_departure_time': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               None,
         'native_unit_of_measurement': None,
      },
      'session_id': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               None,
         'native_unit_of_measurement': None,
      },
      'state': {
         'state_class':                None,
         'device_class':               None,
         'native_unit_of_measurement': None,
      },
      'state_numeric': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               None,
         'native_unit_of_measurement': None,          
      },
      'target_current': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.CURRENT,
         'native_unit_of_measurement': "A",
         'precision':                  2,
      },
      'total_active_power': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               SensorDeviceClass.POWER,
         'native_unit_of_measurement': "kW",
         'precision':                  2,
      },
      'type': {
         'state_class':                None,
         'device_class':               None,
         'native_unit_of_measurement': None,
      },
      'type_numeric': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               None,
         'native_unit_of_measurement': None,          
      },
      'vehicle_connected_phases': {
         'state_class':                None,
         'device_class':               None,
         'native_unit_of_measurement': None,
      },
      'vehicle_connected_phases_code': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               None,
         'native_unit_of_measurement': None,
      },
      'vehicle_connected_phases_numeric': {
         'state_class':                SensorStateClass.MEASUREMENT,
         'device_class':               None,
         'native_unit_of_measurement': None,
      }
   }
}

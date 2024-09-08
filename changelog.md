# ChangeLog
### 24.09.08

+ Replace `async_forward_entry_setup` with `await async_forward_entry_setups`
+ Require homeassistant >= 2024.9.0

### 24.03.02

+ require sonnencharger >= 0.1.2 (stupid me!)

### 24.03.01

+ require pymodbus >= 3.5.0
+ require sonnencharger >= 0.1.1

### 0.1.0

+ fix wrong units:
    - `l1_active_power`: W -> kW
    - `l2_active_power`: W -> kW
    - `l3_active_power`: W -> kW
    - `l3_ln_voltage`:   A -> V
+ fix GitHub 

### 0.0.1

+ initial release

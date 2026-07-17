# Environment, Lighting, and VPD

Environmental metrics are coupled descriptions, not independent knobs.

## VPD needs leaf temperature

Leaf VPD compares saturation vapor pressure at **leaf temperature** with actual vapor pressure represented by air temperature and RH. Air-temperature-only charts assume a leaf-to-air offset; that assumption must be visible. Sensor location, radiation, airflow, transpiration, and lighting technology can change leaf temperature.

Using the Tetens approximation:

`SVP(T) = 0.6108 × exp((17.27 × T) / (T + 237.3))` kPa

`VPD = SVP(leaf °C) − RH/100 × SVP(air °C)`

Use `scripts/calculate_vpd.py`. A mathematically exact result can still have a weak interpretation when leaf temperature is estimated or sensors are poorly placed.

## PPFD is not DLI

PPFD describes an instant. DLI integrates photons over time:

`DLI = PPFD µmol/m²/s × photoperiod hours × 3600 / 1,000,000`

Use `scripts/calculate_dli.py`. A single PPFD reading does not establish canopy uniformity, dimming schedule, fixture degradation, or delivered DLI.

## Interpret transitions

Check day/night and lights-on/off transitions, not only averages. Humidity spikes may emerge when transpiration, surface temperature, and HVAC/dehumidification state change together. Condensation risk is spatial; dense flowers, cold surfaces, canopy interiors, and stagnant zones can diverge from room sensors.

## Targets belong to the facility

Stage-based target ranges in vendor guides or source literature are starting evidence, not operating authority. The active target should cite the facility plan/SOP, cultivar response, equipment capacity, measurement method, and approval state.

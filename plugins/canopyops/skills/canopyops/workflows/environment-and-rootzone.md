# Environment and Root Zone

Use for environmental interpretation, lighting, VPD, DLI, substrate water behavior, irrigation, dryback, runoff, EC, pH, and fertigation decisions.

Read `references/environment-lighting-vpd.md`, `references/rootzone-fertigation.md`, and the facility/crop profiles. Use the calculators and normalization scripts rather than mental arithmetic when available.

1. Normalize time, units, measurement method, sensor location, crop stage, photoperiod, substrate, container, irrigation system, and active facility target before comparing values.
2. Treat interacting variables as a system. Air temperature is not leaf temperature; instantaneous PPFD is not DLI; runoff EC is not root-zone EC; water content is not plant-available water; a target copied from another room—or supplied without stage, scope, tolerance, source, and approval—is a comparison value, not authority.
3. Diagnose trends and spatial patterns before isolated readings. Compare input, root-zone or validated extract, runoff, dryback, irrigation events, plant demand, and room conditions on aligned timestamps.
4. Expose every deterministic result as inputs → unit normalization → formula → result → operational interpretation. Against an exact comparison value, report each result’s direction and magnitude without inventing an acceptable side. If input or target quality is poor, report the calculation accurately and the interpretation provisionally.
5. Propose the smallest reversible change that can improve the condition while preserving diagnostic legibility. Define monitoring, stop limits, owner, and rollback or reopen condition.
6. Major setpoint, CO2, nutrient-program, or irrigation-strategy changes remain recommendations until approved under facility authority.

When Python is unavailable, reproduce the documented formulas manually and mark arithmetic as manual/unverified until independently checked.

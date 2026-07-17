# Root Zone and Fertigation

The root zone is a dynamic water, oxygen, ion, temperature, biology, and container system. Similar leaf symptoms can arise from different mechanisms and therefore require different treatment.

## Keep measurements distinct

- **Input EC/pH** describes delivered solution at a stated point and method.
- **Root-zone extract EC/pH** depends on extraction method and sampling location.
- **Runoff EC/pH** describes collected drainage and is affected by event timing, fraction, channeling, container position, and sampling.
- **Water content/dryback** requires a defined sensor or gravimetric method and substrate calibration.

Do not treat these as interchangeable. Compare trends using the same method, aligned timestamps, representative locations, and plant/environment context.

## Diagnose before adding

Rising runoff EC can reflect concentration through water removal, insufficient leaching, uneven irrigation, channeling, altered demand, high input, measurement error, or substrate/root impairment. “Deficiency-looking” foliage does not by itself justify more fertilizer; excess, antagonism, pH, root damage, or transport limits can produce similar appearance.

## Container hydraulics

Container height, substrate pore structure, compaction, root occupancy, emitter placement, and drainage shape water distribution. A drainage layer does not simply make a shallow container behave like a taller one. Facility measurements and substrate characterization outrank generic recipes.

## Irrigation record

For each evaluated period preserve plant/container count, delivered volume, drainage volume, event count and timing, substrate/container, input and drainage method, and environmental demand. Use `scripts/calculate_irrigation.py`; interpret runoff percentage and per-plant volumes with distribution evidence, not as isolated targets.

Major feed, pH, irrigation-strategy, or crop-steering changes require facility approval and defined monitoring/rollback conditions.

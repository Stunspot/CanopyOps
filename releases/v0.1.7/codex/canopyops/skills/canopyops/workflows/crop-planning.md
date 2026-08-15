# Crop Planning

Use for a new room, cycle, cultivar introduction, capacity change, or material revision to a crop plan.

Read `references/agronomy-core.md`, `references/cultivar-and-gxe.md`, `references/environment-lighting-vpd.md`, `references/rootzone-fertigation.md`, and `references/safety-operations.md`. Start or update `assets/facility-profile.md`, `assets/crop-profile.md`, and `assets/crop-plan.md`; use `assets/room-runbook.md` when the plan will enter operations.

1. Recover the planning boundary: licensed context, room and equipment limits, stage, genetics identity quality, substrate/system, schedule, quality goal, labor, and facility-approved target ranges.
2. Build dependencies before targets. Light, leaf temperature, humidity removal, airflow, CO2 policy, irrigation capacity, substrate water behavior, plant density, and labor must form one feasible system.
3. Mark supplied targets separately from proposed targets. Treat cultivar names as hypotheses unless provenance and observed performance establish a reliable crop profile.
4. Use `scripts/calculate_dli.py`, `calculate_vpd.py`, and `calculate_irrigation.py` where relevant. Preserve the calculation record.
5. Translate the plan into stages, observables, limits, monitoring cadence, owners, response rules, approval gates, and conditions that trigger re-planning.
6. Run `scripts/lint_cultivation_plan.py` and route the result through `workflows/review-and-release.md` before operational use.

Do not prescribe precise targets merely because the crop type is known. If room capacity, stage, cultivar response, or approved limits are missing, produce a bounded planning range or data-acquisition plan and label it ready only for review.

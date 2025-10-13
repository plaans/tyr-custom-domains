# Rovers Hierarchical-Temporal-Numeric

## Source

Hierarchical variant of the `rovers_num` domain, based on the `rovers-time-automatic` domain from IPC 2002.

## Domain Description

Inspired by planetary rovers problems, this domain requires rovers to navigate a planet surface, finding samples and communicating them back to a lander. This hierarchical variant adds task decomposition using HDDL (Hierarchical Domain Definition Language), allowing for more structured and abstract planning with hierarchical task networks.

## Hierarchical Features

- **HDDL Format**: Uses hierarchical task networks with methods and tasks
- **Goal-to-Task Conversion**: Goals are converted to hierarchical tasks:
  - `(communicated_soil_data ?p)` → `(get_soil_data ?p)`
  - `(communicated_rock_data ?p)` → `(get_rock_data ?p)`
  - `(communicated_image_data ?o ?m)` → `(get_image_data ?o ?m)`
- **Freedom Predicates**: Adds `free_to_recharge` tasks for rover energy management
- **Dynamic Instance Generation**: Problem instances are generated on-the-fly by converting numeric PDDL instances to hierarchical HDDL format using the `goals_to_tasks` converter

## Variants

### base
Standard hierarchical variant with durative actions and numeric fluents:
- Energy-based constraints with recharge actions
- Duration: `(/ (- 80 (energy ?x)) (recharge-rate ?x))`
- Fixed durations for most actions (navigate: 5, sample_soil: 10, etc.)

### fix_dur
Variant with modified duration constraints:
- Adjusted timing for specific operations
- May have different duration calculations for certain actions

### no_div
Variant without division operations in duration calculations:
- Replaces division-based durations with static fluents
- Suitable for planners that don't support division in durations

## Instance Files

This domain does not contain static instance files. Instead, instances are dynamically generated from the `rovers_num` domain instances (instance-1.pddl through instance-20.pddl) by converting their goals to hierarchical tasks.

## Authors

*unknown*

## Related Domains

- Base domain: `rovers_num` (warm-up numeric variant)
- Original domain: `rovers-time-automatic` (IPC 2002)

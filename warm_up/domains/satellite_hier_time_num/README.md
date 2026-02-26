# Satellite Hierarchical-Temporal-Numeric

## Source

Hierarchical variant of the `satellite_num` domain, based on the `satellite-complex-automatic` domain from IPC 2002.

## Domain Description

The first of the domains inspired by space applications, this involves planning and scheduling observation tasks between multiple satellites, each equipped in slightly different ways. This hierarchical variant adds task decomposition using HDDL (Hierarchical Domain Definition Language), allowing for more structured and abstract planning with hierarchical task networks.

## Hierarchical Features

- **HDDL Format**: Uses hierarchical task networks with methods and tasks
- **Goal-to-Task Conversion**: Goals are converted to hierarchical tasks:
  - `(have_image ?r ?o ?m)` → `(do_observation ?r ?o ?m)`
  - `(pointing ?s ?d)` → `(turn_to_abs ?s ?d)`
- **Dynamic Instance Generation**: Problem instances are generated on-the-fly by converting numeric PDDL instances to hierarchical HDDL format using the `goals_to_tasks` converter

## Variants

### base
Standard hierarchical variant with durative actions and numeric fluents:
- Temporal constraints for satellite operations
- Numeric fluents for fuel, data storage, and other resources
- Complex scheduling of observations and data transmissions

## Instance Files

This domain does not contain static instance files. Instead, instances are dynamically generated from the `satellite_num` domain instances (instance-1.pddl through instance-20.pddl) by converting their goals to hierarchical tasks.

## Additional Notes

The hierarchical structure provides additional decomposition for complex satellite scheduling problems, making them more amenable to hierarchical planning approaches.

## Authors

*unknown*

## Related Domains

- Base domain: `satellite_num` (warm-up numeric variant)
- Original domain: `satellite-complex-automatic` (IPC 2002)

# Depots Hierarchical-Temporal-Numeric

## Source

Hierarchical variant of the `depots_num` domain, based on the `depots-numeric-automatic` domain from IPC 2002.

## Domain Description

This domain combines logistics and blocks world problems, where trucks transport crates and hoists stack them onto pallets. This hierarchical variant adds task decomposition using HDDL (Hierarchical Domain Definition Language), allowing for more structured and abstract planning.

The hierarchical structure decomposes high-level goals into task networks, providing additional structure for hierarchical planners.

## Hierarchical Features

- **HDDL Format**: Uses hierarchical task networks with methods and tasks
- **Goal-to-Task Conversion**: Goals like `(on ?c ?s)` are converted to hierarchical tasks `(do_put_on ?c ?s)`
- **Dynamic Instance Generation**: Problem instances are generated on-the-fly by converting numeric PDDL instances to hierarchical HDDL format using the `goals_to_tasks` converter

## Variants

### base
Standard hierarchical variant with durative actions and numeric fluents:
- Duration calculations use division: `(/ (distance ?y ?z) (speed ?x))`
- Duration calculations use division: `(/ (weight ?y) (power ?x))`

### no_div
Variant without division operations in duration calculations:
- Uses pre-computed static fluents instead: `(drive_duration ?x ?y ?z)`
- Uses pre-computed static fluents instead: `(load_duration ?x ?y)`
- Suitable for planners that don't support division in durations

## Instance Files

This domain does not contain static instance files. Instead, instances are dynamically generated from the `depots_num` domain instances (instance-1.pddl through instance-22.pddl) by converting their goals to hierarchical tasks.

## Authors

*unknown*

## Related Domains

- Base domain: `depots_num` (warm-up numeric variant)
- Original domain: `depots-numeric-automatic` (IPC 2002)

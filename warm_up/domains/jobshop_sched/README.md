# Jobshop Scheduling (Hierarchical Simulation)

## Source

Job Shop Scheduling Problem from classic benchmark instances.

## Domain Description

The Job Shop Scheduling Problem involves scheduling jobs on machines where:
- Each job consists of a sequence of operations
- Each operation requires a specific machine for a specific duration
- Machines can only process one operation at a time
- Additional operator resources are limited
- Objective to minimize the makespan

This variant maintains the **native scheduling representation** instead of converting to PDDL actions. This allows Aries to treat it as a scheduling problem with implicit hierarchical structure through:
- **Job decomposition**: Each job decomposes into sequential operations
- **Resource hierarchy**: Machine and operator constraints at different levels
- **Precedence constraints**: Operation ordering within jobs forms task hierarchies
- **Temporal relationships**: Complex machine-job interactions

## Key Differences from `warm-up-jobshop-num`

- **warm-up-jobshop-num**: Converts scheduling problem to PDDL with durative actions
- **warm-up-jobshop-sched**: Keeps native `SchedulingProblem` representation
- This enables Aries to use its scheduling-specific reasoning and hierarchical planning capabilities

## Variants

### base
Standard Jobshop scheduling problems with:
- 40 instances (20 problem instances × 2 operator configurations)
- Operator configurations: 3 and 5 concurrent operators
- Multiple machines with unit capacity
- Sequential job operations

## Instance Files

Instances use the `.jsp` format (shared with `warm-up-jobshop-num` via symlink).

## Authors

*Classic benchmark suite*

## Related Domains

- Base PDDL variant: `warm-up-jobshop-num`
- Pure scheduling: `scheduling-jobshop`

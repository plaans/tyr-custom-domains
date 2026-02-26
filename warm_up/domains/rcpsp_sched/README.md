# RCPSP Scheduling (Hierarchical Simulation)

## Source

Resource-Constrained Project Scheduling Problem (RCPSP) from PSPLIB benchmark instances.

## Domain Description

The Resource-Constrained Project Scheduling Problem (RCPSP) involves scheduling a set of activities subject to:
- Precedence constraints between activities
- Resource capacity constraints
- Objective to minimize the project makespan

This variant maintains the **native scheduling representation** instead of converting to PDDL actions. This allows Aries to treat it as a scheduling problem with implicit hierarchical structure through:
- **Resource management hierarchy**: Activities compete for limited resources
- **Precedence network**: Job dependencies form a hierarchical task decomposition
- **Temporal constraints**: Start/end timing relationships create scheduling layers

## Key Differences from `warm-up-rcpsp-num`

- **warm-up-rcpsp-num**: Converts scheduling problem to PDDL with durative actions
- **warm-up-rcpsp-sched**: Keeps native `SchedulingProblem` representation
- This enables Aries to use its scheduling-specific reasoning and hierarchical planning capabilities

## Variants

### base
Standard RCPSP scheduling problems with:
- 30 instances from PSPLIB benchmark
- Multiple resources with varying capacities
- Complex precedence networks
- Integer durations and resource demands

## Instance Files

Instances use the PSPLIB `.sm` format (shared with `warm-up-rcpsp-num` via symlink).

## Authors

*PSPLIB benchmark suite*

## Related Domains

- Base PDDL variant: `warm-up-rcpsp-num`
- Pure scheduling: `scheduling-rcpsp`

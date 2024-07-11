# Custom Instances

## Overview

This repository contains custom instances used by myself (Roland Godet) in a **consistent structure** for [Tyr](https://github.com/plaans/tyr).

## Format

This format is inspired by [the one used by the International Planning Competitions](https://github.com/potassco/pddl-instances/tree/master) (IPC).

Problem instances reside in the `instances` subdirectory and are of the form `instance-x.pddl` or `instance-x.hddl`, where `x` ≥ 1 (without leading zeros).

With most domains, there is only one domain description for all instances, `domain.pddl` or `domain.hddl`.
In some cases, a proper domain is provided for each instance, in which case the domain descriptions are stored in a `domains` subdirectory.

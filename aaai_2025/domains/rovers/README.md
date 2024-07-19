# Rovers

## Source

`rovers-time-automatic` domain of IPC 2002.

## Modifications

- Replace `(* ?duration (recharge-rate ?x))` in the effect of the `recharge` action by `(- 80 (energy ?x))` because the UPF parser do not support the `?duration` variable in effects.
- Replace all fluents present in a division by static fluents in order to remove the divisions from the domain.
- Reduce the number of goals. For the instance `i`, keep only the `i % 5 + 1` first goals.

## Domain Description

Inspired by planetary rovers problems, this domain requires that a collection of rovers navigate a planet surface, finding samples and communicating them back to a lander.

## Authors

*unknown*

## Original File Names

| file             | original name |
|------------------|---------------|
| domain.pddl      | CTRover.pddl  |
| instance-1.pddl  | pfile1        |
| instance-2.pddl  | pfile2        |
| instance-3.pddl  | pfile3        |
| instance-4.pddl  | pfile4        |
| instance-5.pddl  | pfile5        |
| instance-6.pddl  | pfile6        |
| instance-7.pddl  | pfile7        |
| instance-8.pddl  | pfile8        |
| instance-9.pddl  | pfile9        |
| instance-10.pddl | pfile10       |
| instance-11.pddl | pfile11       |
| instance-12.pddl | pfile12       |
| instance-13.pddl | pfile13       |
| instance-14.pddl | pfile14       |
| instance-15.pddl | pfile15       |
| instance-16.pddl | pfile16       |
| instance-17.pddl | pfile17       |
| instance-18.pddl | pfile18       |
| instance-19.pddl | pfile19       |
| instance-20.pddl | pfile20       |

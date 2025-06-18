# Drone

## Source

`drone-numeric` domain of IPC 2023.

## Modifications

- Add a duration of 1 time unit to each action.
- Add control parameters to choose by how much the increase/decrease is done for the three dimensions (*Done with UPF*).
- Cannot move if the drone is already in movement.

## Domain Description

This is a domain modeling a 3D-located UAV whose task is to visit a certain number of locations whose description is also given in terms of their exact 3D position.
A challenging aspect here is to account for the battery since the UAV cannot do all visit at once but needs to recharge at the starting location.
Therefore, multiple travels back and forth may be necessary to cover visit all locations.

## Authors

Enrico Scala <enricos83@gmail.com>

"""Shared RCPSP parsing and encoding logic for both PDDL and scheduling versions."""

from pathlib import Path
from typing import Dict, List

import unified_planning as up
from unified_planning.model.scheduling.scheduling_problem import SchedulingProblem
from unified_planning.shortcuts import LE


class Problem:
    def __init__(self) -> None:
        self.jobs: List[int] = []
        self.res: List[int] = []
        self.horizon = -1

        self.succs: Dict[int, List[int]] = {}
        self.durations: List[int] = []
        self.demands: List[List[int]] = []
        self.capacities: List[int] = []


def ints(strs):
    return [int(s) for s in strs]


def myset(cardinality):
    return list(range(1, cardinality + 1))


def index_of_line(lines, substr):
    return next(i for i, line in enumerate(lines) if substr in line)


def rhs_part(lines, prefix):
    return lines[index_of_line(lines, prefix)].split(":")[1]


def succs_from_line(line):
    return [int(j) for j in line.split()[3:]]


def column(lines, col, rowStart, rowCount):
    return [
        int(lines[rowIx].split()[col]) for rowIx in range(rowStart, rowStart + rowCount)
    ]


def PSPLIB_parser(filepath):
    """Python parser for PSPLIB files."""
    with open(filepath, encoding="utf-8") as fp:
        lines = fp.readlines()

    njobs = int(rhs_part(lines, "jobs (incl. supersource"))

    nres = int(rhs_part(lines, "- renewable").split()[0])
    nperiods = int(rhs_part(lines, "horizon"))
    prec_offset = index_of_line(lines, "PRECEDENCE RELATIONS:") + 2
    attrs_offset = index_of_line(lines, "REQUESTS/DURATIONS") + 3
    caps_offset = index_of_line(lines, "RESOURCEAVAILABILITIES") + 2

    problem = Problem()
    problem.jobs = myset(njobs)
    problem.res = myset(nres)
    problem.horizon = nperiods

    problem.succs = {
        j: succs_from_line(lines[prec_offset + ix]) for ix, j in enumerate(problem.jobs)
    }
    problem.durations = column(lines, 2, attrs_offset, njobs)
    problem.demands = [
        ints(lines[ix].split()[3:]) for ix in range(attrs_offset, attrs_offset + njobs)
    ]
    problem.capacities = ints(lines[caps_offset].split())

    return problem


# pylint: disable = too-many-locals
def encode_rcpsp(problem: Problem) -> SchedulingProblem:
    """Encode a PSPLIB problem as a SchedulingProblem."""
    u = SchedulingProblem("rcpsp")

    resources = {}
    for idx, r in enumerate(problem.res):
        capacity = problem.capacities[idx]
        resources[r] = u.add_resource(name=f"r{r}", capacity=capacity)

    activities = {}
    for idx, job in enumerate(problem.jobs):
        duration = problem.durations[idx]
        a = u.add_activity(f"a{job}", duration=duration)
        for res_idx, demand in enumerate(problem.demands[idx]):
            res = problem.res[res_idx]
            fluent = resources[res]
            if demand != 0:
                a.uses(fluent, demand)
        activities[job] = a

    for job, succs in problem.succs.items():
        act = activities[job]
        for succ_job in succs:
            succ_act = activities[succ_job]
            act.add_constraint(LE(act.end, succ_act.start))

    u.add_quality_metric(up.model.MinimizeMakespan())

    return u

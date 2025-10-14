"""Shared Jobshop parsing and encoding logic for both PDDL and scheduling versions."""

from pathlib import Path
from typing import List, Optional

from unified_planning.model.metrics import MinimizeMakespan
from unified_planning.model.scheduling.activity import Activity
from unified_planning.model.scheduling.scheduling_problem import SchedulingProblem
from unified_planning.shortcuts import LE


def _ints(line: str) -> List[int]:
    """Returns the list of integers stored in the given line."""
    return list(map(int, line.rstrip().split()))


# pylint: disable = too-many-locals
def parse_jobshop(filepath: Path, num_operators: int) -> SchedulingProblem:
    """Parses a jobshop instance and return the corresponding JobShop with operators."""
    lines = filepath.read_text("utf-8").splitlines()

    head = lines.pop(0)
    num_jobs, num_mach = _ints(head if not head[0].isalpha() else lines.pop(0))[:2]

    times = []
    for _ in range(num_jobs):
        line = lines.pop(0)
        times.append(_ints(line if not line.isalpha() else lines.pop(0)))

    machines = []
    for _ in range(num_jobs):
        line = lines.pop(0)
        machines.append(_ints(line if not line.isalpha() else lines.pop(0)))

    pb = SchedulingProblem(f"jobshop-{filepath.stem}-operators-{num_operators}")
    machine_objects = [pb.add_resource(f"m{i+1}", capacity=1) for i in range(num_mach)]
    operators = pb.add_resource("operators", capacity=num_operators)

    for j in range(num_jobs):
        prev_in_job: Optional[Activity] = None

        for m in range(num_mach):
            act = pb.add_activity(f"t_{j}_{m}", duration=times[j][m])
            machine = machine_objects[machines[j][m] - 1]
            act.uses(machine)
            act.uses(operators, amount=1)

            if prev_in_job is not None:
                pb.add_constraint(LE(prev_in_job.end, act.start))
            prev_in_job = act

    pb.add_quality_metric(MinimizeMakespan())
    return pb


OPERATORS = [3, 5]

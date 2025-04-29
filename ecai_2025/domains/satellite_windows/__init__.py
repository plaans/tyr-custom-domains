from math import ceil
from pathlib import Path
from typing import Optional

from unified_planning.shortcuts import AbstractProblem, Timing

from tyr.problems.model import FolderAbstractDomain, ProblemInstance


class Ecai2025SatelliteWindowsDomain(FolderAbstractDomain):
    def __init__(self) -> None:
        super().__init__()
        self.folder = Path(__file__).parent

    def build_problem_no_float(
        self, problem: ProblemInstance
    ) -> Optional[AbstractProblem]:
        # Get the base version of the problem.
        base = problem.versions["base"].value
        if base is None:
            return None

        # Round all real values to get integers
        no_float = base.clone()
        for sv, value in base.explicit_initial_values.items():
            if value.is_real_constant():
                no_float.set_initial_value(sv, ceil(value.real_constant_value()))

        # Round all time initial values time-point to get integers
        new_timed_effects = {}
        for t, e in no_float.timed_effects.items():
            new_timed_effects[Timing(ceil(t.delay), t.timepoint)] = e
        no_float._timed_effects = new_timed_effects  # pylint: disable=protected-access

        return no_float

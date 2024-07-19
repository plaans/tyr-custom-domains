from math import ceil
from pathlib import Path
from typing import Optional

from unified_planning.shortcuts import AbstractProblem

from tyr.problems.converter import reduce_problem
from tyr.problems.model import FolderAbstractDomain, ProblemInstance


class Aaai2025SatelliteDomain(FolderAbstractDomain):
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
        return reduce_problem(no_float, int(problem.uid) % 5 + 1)

from math import ceil
from pathlib import Path
from typing import Optional

from unified_planning.shortcuts import AbstractProblem, Problem

from tyr.problems.converter import reduce_problem
from tyr.problems.model import FolderAbstractDomain, ProblemInstance


class Aaai2025SatelliteTimeWindowsDomain(FolderAbstractDomain):
    def __init__(self) -> None:
        super().__init__()
        self.folder_base = Path(__file__).parent / "base"
        self.folder_compiled = Path(__file__).parent / "compiled"

    def get_num_problems(self) -> int:
        self.folder = self.folder_base
        return super().get_num_problems()

    def build_problem_base(self, problem: ProblemInstance) -> Optional[AbstractProblem]:
        self.folder = self.folder_base
        return super().build_problem_base(problem)

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

        # Round all timed-initial literals to get integers
        for timing, _eff in no_float.timed_effects.items():
            timing._delay = ceil(timing.delay)  # pylint: disable=protected-access

        return reduce_problem(no_float, int(problem.uid) % 5 + 1)

    def build_problem_compiled(
        self, problem: ProblemInstance
    ) -> Optional[AbstractProblem]:
        self.folder = self.folder_compiled
        return super().build_problem_base(problem)

    def build_problem_compiled_no_float(
        self, problem: ProblemInstance
    ) -> Optional[AbstractProblem]:
        # Get the compiled version of the problem.
        compiled = problem.versions["compiled"].value
        if compiled is None:
            return None

        # Round all action durations to get integers
        no_float: Problem = compiled.clone()
        for act in no_float.actions:
            if (
                act.duration.lower.is_real_constant()
                or act.duration.upper.is_real_constant()
            ):
                if act.duration.lower != act.duration.upper:
                    raise ValueError("Action duration is not constant.")
                act.set_fixed_duration(ceil(act.duration.lower.real_constant_value()))

        # Round all real values to get integers
        for sv, value in compiled.explicit_initial_values.items():
            if value.is_real_constant():
                no_float.set_initial_value(sv, ceil(value.real_constant_value()))

        # Round all timed-initial literals to get integers
        for timing, _eff in no_float.timed_effects.items():
            timing._delay = ceil(timing.delay)  # pylint: disable=protected-access

        return reduce_problem(no_float, int(problem.uid) % 5 + 1)

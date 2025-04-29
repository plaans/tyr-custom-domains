from math import ceil
from pathlib import Path
from typing import Optional

from unified_planning.shortcuts import AbstractProblem, FixedDuration, IntType

from tyr.problems.model import FolderAbstractDomain, ProblemInstance


class Ecai2025AirportDomain(FolderAbstractDomain):
    def __init__(self) -> None:
        super().__init__()
        self.folder = Path(__file__).parent

    def build_problem_no_mul(
        self, problem: ProblemInstance
    ) -> Optional[AbstractProblem]:
        # Get the base version of the problem.
        base = problem.versions["base"].value
        if base is None:
            return None

        # Create and initialize an engines60 fluent
        no_mul = base.clone()
        engines_fluent = no_mul.fluent("engines")
        engines60_fluent = no_mul.add_fluent(
            "engines60", IntType(), a=no_mul.user_type("airplane")
        )
        for sv, value in base.explicit_initial_values.items():
            no_mul.set_initial_value(sv, value)
            if sv.fluent() == engines_fluent:
                sv60 = engines60_fluent(sv.args[0])
                value60 = (value * 60).simplify().constant_value()
                no_mul.set_initial_value(sv60, value60)

        # Replace all durations (* 60 (engines ?a)) by (engines60 ?a)
        no_mul._actions = []  # pylint: disable=protected-access
        for action in base.actions:
            assert action.duration.lower == action.duration.upper  # nosec: B101
            dur = action.duration.lower
            if not dur.is_times():
                no_mul.add_action(action)
                continue
            assert dur.args[0].constant_value() == 60  # nosec: B101
            assert str(dur.args[1]) == "engines(a)"  # nosec: B101
            new_action = action.clone()
            new_action._duration = FixedDuration(  # pylint: disable=protected-access
                engines60_fluent(dur.args[1].args[0])
            )
            no_mul.add_action(new_action)
        assert len(no_mul.actions) == len(base.actions)  # nosec: B101

        return no_mul

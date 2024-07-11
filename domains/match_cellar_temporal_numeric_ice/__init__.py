from typing import Optional

from unified_planning.shortcuts import (
    GT,
    AbstractProblem,
    DurativeAction,
    EndTiming,
    Problem,
    StartTiming,
)

from tyr.problems.model.domain import AbstractDomain
from tyr.problems.model.instance import ProblemInstance


class CustomMatchCellarTemporalNumericIceDomain(AbstractDomain):
    def get_num_problems(self) -> int:
        from tyr.problems.domains.custom import (  # type: ignore[attr-defined] # noqa: E501 # pylint: disable=line-too-long
            CustomMatchCellarTemporalNumericDomain,
        )

        return CustomMatchCellarTemporalNumericDomain().get_num_problems()

    def build_problem_base(self, problem: ProblemInstance) -> Optional[AbstractProblem]:
        from tyr.problems.domains.custom import (  # type: ignore[attr-defined] # noqa: E501 # pylint: disable=line-too-long
            CustomMatchCellarTemporalNumericDomain,
        )

        base: Problem = (
            CustomMatchCellarTemporalNumericDomain().build_problem_base(problem).clone()
        )

        handfree = base.fluent("handfree")
        num_matches = base.fluent("num-matches")
        num_lit_matches = base.fluent("num-lit-matches")

        mend_fuse: DurativeAction = base.action("mend_fuse").clone()
        light_match = DurativeAction("light_match")
        light_match.set_fixed_duration(6)
        light_match.add_condition(StartTiming(), handfree)
        light_match.add_condition(StartTiming(), GT(num_matches, 0))
        light_match.add_effect(StartTiming(), handfree, False)
        light_match.add_decrease_effect(StartTiming(), num_matches, 1)
        light_match.add_effect(StartTiming(1), handfree, True)
        light_match.add_increase_effect(StartTiming(1), num_lit_matches, 1)
        light_match.add_decrease_effect(EndTiming(), num_lit_matches, 1)

        base.clear_actions()
        base.add_action(light_match)
        base.add_action(mend_fuse)

        return base

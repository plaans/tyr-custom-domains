from typing import Optional

from unified_planning.shortcuts import (
    GT,
    AbstractProblem,
    BoolType,
    DurativeAction,
    EndTiming,
    Problem,
    StartTiming,
)

from tyr.problems.model.domain import AbstractDomain
from tyr.problems.model.instance import ProblemInstance


class Aaai2025MatchCellarIceDomain(AbstractDomain):
    def get_num_problems(self) -> int:
        from tyr.problems.domains.custom import (  # type: ignore[attr-defined] # noqa: E501 # pylint: disable=line-too-long
            Aaai2025MatchCellarDomain,
        )

        return Aaai2025MatchCellarDomain().get_num_problems()

    def build_problem_base(self, problem: ProblemInstance) -> Optional[AbstractProblem]:
        from tyr.problems.domains.custom import (  # type: ignore[attr-defined] # noqa: E501 # pylint: disable=line-too-long
            Aaai2025MatchCellarDomain,
        )

        base: Problem = Aaai2025MatchCellarDomain().build_problem_base(problem).clone()

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

    def build_problem_pddl(self, problem: ProblemInstance) -> Optional[AbstractProblem]:
        base = self.build_problem_base(problem)
        if base is None:
            return None
        pddl = base.clone()

        a = pddl.add_fluent("a", BoolType(), default_initial_value=False)
        b = pddl.add_fluent("b", BoolType(), default_initial_value=False)
        c = pddl.add_fluent("c", BoolType(), default_initial_value=False)
        handfree = pddl.fluent("handfree")
        num_matches = pddl.fluent("num-matches")
        num_lit_matches = pddl.fluent("num-lit-matches")

        mend_fuse = pddl.action("mend_fuse").clone()

        light_match = DurativeAction("light_match")
        light_match.set_closed_duration_interval(6, 7)
        light_match.add_condition(EndTiming(), c)
        light_match.add_effect(StartTiming(), a, True)
        light_match.add_effect(EndTiming(), c, False)

        strike_match = DurativeAction("strike_match")
        strike_match.set_fixed_duration(1)
        strike_match.add_condition(StartTiming(), a)
        strike_match.add_condition(StartTiming(), handfree)
        strike_match.add_condition(StartTiming(), GT(num_matches, 0))
        strike_match.add_effect(StartTiming(), a, False)
        strike_match.add_effect(StartTiming(), handfree, False)
        strike_match.add_decrease_effect(StartTiming(), num_matches, 1)
        strike_match.add_effect(EndTiming(), b, True)
        strike_match.add_effect(EndTiming(), handfree, True)

        lit_match = DurativeAction("lit_match")
        lit_match.set_fixed_duration(5)
        lit_match.add_condition(StartTiming(), b)
        lit_match.add_effect(StartTiming(), b, False)
        lit_match.add_increase_effect(StartTiming(), num_lit_matches, 1)
        lit_match.add_effect(EndTiming(), c, True)
        lit_match.add_decrease_effect(EndTiming(), num_lit_matches, 1)

        pddl.clear_actions()
        pddl.add_action(light_match)
        pddl.add_action(strike_match)
        pddl.add_action(lit_match)
        pddl.add_action(mend_fuse)

        return pddl

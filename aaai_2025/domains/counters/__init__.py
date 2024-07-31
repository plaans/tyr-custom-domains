from pathlib import Path
from typing import Optional

from unified_planning.shortcuts import (
    GE,
    LE,
    AbstractProblem,
    DurativeAction,
    EndTiming,
    IntType,
    MinimizeActionCosts,
    Plus,
    StartTiming,
)

from tyr.problems.model import FolderAbstractDomain, ProblemInstance


class Aaai2025CountersDomain(FolderAbstractDomain):
    def __init__(self) -> None:
        super().__init__()
        self.folder = Path(__file__).parent

    def build_problem_ctrl_params(
        self, problem: ProblemInstance
    ) -> Optional[AbstractProblem]:
        # Load the base problem
        base = problem.versions["base"].value
        if base is None:
            return None

        # Create the problem and replace the actions
        pb = base.clone()
        pb.clear_actions()

        # Get the types
        counter_type = pb.user_type("counter")
        number = IntType(lower_bound=0, upper_bound=100)

        # Get the fluents
        value = pb.fluent("value")
        max_int = pb.fluent("max_int")
        total_cost = pb.fluent("total_cost")

        # Create the actions
        increment = DurativeAction("increment", c=counter_type, k=number)
        increment.set_fixed_duration(increment.k)
        increment.add_condition(
            StartTiming(), LE(Plus(value(increment.c), increment.k), max_int)
        )
        increment.add_increase_effect(EndTiming(), value(increment.c), increment.k)
        increment.add_increase_effect(EndTiming(), total_cost, increment.k)
        pb.add_action(increment)

        decrement = DurativeAction("decrement", c=counter_type, k=number)
        decrement.set_fixed_duration(decrement.k)
        decrement.add_condition(StartTiming(), GE(value(decrement.c), decrement.k))
        decrement.add_decrease_effect(EndTiming(), value(decrement.c), decrement.k)
        decrement.add_increase_effect(EndTiming(), total_cost, increment.k)
        pb.add_action(decrement)

        return pb

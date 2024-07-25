from pathlib import Path
from typing import Optional

from unified_planning.shortcuts import (
    GE,
    LE,
    AbstractProblem,
    InstantaneousAction,
    IntType,
    MinimizeActionCosts,
    Plus,
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

        # Create the actions
        increment = InstantaneousAction("increment", c=counter_type, k=number)
        increment.add_precondition(LE(Plus(value(increment.c), increment.k), max_int))
        increment.add_increase_effect(value(increment.c), increment.k)
        pb.add_action(increment)

        decrement = InstantaneousAction("decrement", c=counter_type, k=number)
        decrement.add_precondition(GE(value(decrement.c), decrement.k))
        decrement.add_decrease_effect(value(decrement.c), decrement.k)
        pb.add_action(decrement)

        # Create action costs
        costs = {
            increment: increment.k,
            decrement: increment.k,
        }
        pb.add_quality_metric(MinimizeActionCosts(costs, 1))

        return pb

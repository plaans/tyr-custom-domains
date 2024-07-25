from pathlib import Path
from typing import Optional

from unified_planning.shortcuts import (
    GE,
    LE,
    AbstractProblem,
    InstantaneousAction,
    IntType,
    MinimizeActionCosts,
    Minus,
    Plus,
)

from tyr.problems.model import FolderAbstractDomain, ProblemInstance


class Aaai2025DroneDomain(FolderAbstractDomain):
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
        visit = base.action("visit")
        recharge = base.action("recharge")
        pb.clear_actions()
        pb.add_actions([visit, recharge])

        # Get the types
        number = IntType(lower_bound=0, upper_bound=100)

        # Get the fluents
        x = pb.fluent("x")
        y = pb.fluent("y")
        z = pb.fluent("z")
        min_x = pb.fluent("min_x")
        max_x = pb.fluent("max_x")
        min_y = pb.fluent("min_y")
        max_y = pb.fluent("max_y")
        min_z = pb.fluent("min_z")
        max_z = pb.fluent("max_z")
        battery_level = pb.fluent("battery-level")

        # Create the actions
        increase = InstantaneousAction("increase", xc=number, yc=number, zc=number)
        increase_delta = Plus(increase.xc, increase.yc, increase.zc)
        increase.add_precondition(GE(battery_level, increase_delta))
        increase.add_precondition(LE(x, Minus(max_x, increase.xc)))
        increase.add_precondition(LE(y, Minus(max_y, increase.yc)))
        increase.add_precondition(LE(z, Minus(max_z, increase.zc)))
        increase.add_increase_effect(x, increase.xc)
        increase.add_increase_effect(y, increase.yc)
        increase.add_increase_effect(z, increase.zc)
        increase.add_decrease_effect(battery_level, increase_delta)
        pb.add_action(increase)

        decrease = InstantaneousAction("decrease", xc=number, yc=number, zc=number)
        decrease_delta = Plus(decrease.xc, decrease.yc, decrease.zc)
        decrease.add_precondition(GE(battery_level, decrease_delta))
        decrease.add_precondition(GE(x, Plus(min_x, decrease.xc)))
        decrease.add_precondition(GE(y, Plus(min_y, decrease.yc)))
        decrease.add_precondition(GE(z, Plus(min_z, decrease.zc)))
        decrease.add_decrease_effect(x, decrease.xc)
        decrease.add_decrease_effect(y, decrease.yc)
        decrease.add_decrease_effect(z, decrease.zc)
        decrease.add_increase_effect(battery_level, decrease_delta)
        pb.add_action(decrease)

        # Create action costs
        costs = {
            increase: increase_delta,
            decrease: decrease_delta,
        }
        pb.add_quality_metric(MinimizeActionCosts(costs, 1))

        return pb

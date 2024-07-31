from pathlib import Path
from typing import Optional

from unified_planning.plans import Plan
from unified_planning.shortcuts import (
    GE,
    LE,
    AbstractProblem,
    DurativeAction,
    EndTiming,
    FNode,
    IntType,
    Minus,
    Plus,
    StartTiming,
)

from tyr.problems.model import FolderAbstractDomain, ProblemInstance


class Aaai2025DroneDomain(FolderAbstractDomain):
    def __init__(self) -> None:
        super().__init__()
        self.folder = Path(__file__).parent

    def get_quality_of_plan(
        self, plan: Plan, version: AbstractProblem
    ) -> Optional[float]:
        cost = 0.0
        for _, a, _ in plan.timed_actions:
            if a.action.name in ["visit", "recharge"]:
                cost += 1
            else:
                cost += a.actual_parameters[0] if len(a.actual_parameters) > 0 else 1
        if isinstance(cost, FNode):
            return cost.simplify().constant_value()
        return cost

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
        total_cost = pb.fluent("total_cost")

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
        increase_x = DurativeAction("increase_x", k=number)
        increase_x.set_fixed_duration(increase_x.k)
        increase_x.add_condition(StartTiming(), GE(battery_level, increase_x.k))
        increase_x.add_condition(StartTiming(), LE(x, Minus(max_x, increase_x.k)))
        increase_x.add_increase_effect(EndTiming(), x, increase_x.k)
        increase_x.add_decrease_effect(EndTiming(), battery_level, increase_x.k)
        increase_x.add_increase_effect(EndTiming(), total_cost, increase_x.k)
        pb.add_action(increase_x)

        increase_y = DurativeAction("increase_y", k=number)
        increase_y.set_fixed_duration(increase_y.k)
        increase_y.add_condition(StartTiming(), GE(battery_level, increase_y.k))
        increase_y.add_condition(StartTiming(), LE(y, Minus(max_y, increase_y.k)))
        increase_y.add_increase_effect(EndTiming(), y, increase_y.k)
        increase_y.add_decrease_effect(EndTiming(), battery_level, increase_y.k)
        increase_y.add_increase_effect(EndTiming(), total_cost, increase_y.k)
        pb.add_action(increase_y)

        increase_z = DurativeAction("increase_z", k=number)
        increase_z.set_fixed_duration(increase_z.k)
        increase_z.add_condition(StartTiming(), GE(battery_level, increase_z.k))
        increase_z.add_condition(StartTiming(), LE(z, Minus(max_z, increase_z.k)))
        increase_z.add_increase_effect(EndTiming(), z, increase_z.k)
        increase_z.add_decrease_effect(EndTiming(), battery_level, increase_z.k)
        increase_z.add_increase_effect(EndTiming(), total_cost, increase_z.k)
        pb.add_action(increase_z)

        decrease_x = DurativeAction("decrease_x", k=number)
        decrease_x.set_fixed_duration(decrease_x.k)
        decrease_x.add_condition(StartTiming(), GE(battery_level, decrease_x.k))
        decrease_x.add_condition(StartTiming(), GE(x, Plus(min_x, decrease_x.k)))
        decrease_x.add_decrease_effect(EndTiming(), x, decrease_x.k)
        decrease_x.add_increase_effect(EndTiming(), battery_level, decrease_x.k)
        decrease_x.add_increase_effect(EndTiming(), total_cost, decrease_x.k)
        pb.add_action(decrease_x)

        decrease_y = DurativeAction("decrease_y", k=number)
        decrease_y.set_fixed_duration(decrease_y.k)
        decrease_y.add_condition(StartTiming(), GE(battery_level, decrease_y.k))
        decrease_y.add_condition(StartTiming(), GE(y, Plus(min_y, decrease_y.k)))
        decrease_y.add_decrease_effect(EndTiming(), y, decrease_y.k)
        decrease_y.add_increase_effect(EndTiming(), battery_level, decrease_y.k)
        decrease_y.add_increase_effect(EndTiming(), total_cost, decrease_y.k)
        pb.add_action(decrease_y)

        decrease_z = DurativeAction("decrease_z", k=number)
        decrease_z.set_fixed_duration(decrease_z.k)
        decrease_z.add_condition(StartTiming(), GE(battery_level, decrease_z.k))
        decrease_z.add_condition(StartTiming(), GE(z, Plus(min_z, decrease_z.k)))
        decrease_z.add_decrease_effect(EndTiming(), z, decrease_z.k)
        decrease_z.add_increase_effect(EndTiming(), battery_level, decrease_z.k)
        decrease_z.add_increase_effect(EndTiming(), total_cost, decrease_z.k)
        pb.add_action(decrease_z)

        return pb

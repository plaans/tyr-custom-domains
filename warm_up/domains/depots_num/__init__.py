from pathlib import Path
from typing import Optional

from unified_planning.plans import Plan, SequentialPlan, TimeTriggeredPlan
from unified_planning.shortcuts import AbstractProblem

from tyr.problems.model import FolderAbstractDomain


class WarmUpDepotsNumDomain(FolderAbstractDomain):
    def __init__(self) -> None:
        super().__init__()
        self.folder = Path(__file__).parent

    def get_quality_of_plan(
        self, plan: Plan, version: AbstractProblem
    ) -> Optional[float]:
        cost = 0.0
        if isinstance(plan, TimeTriggeredPlan):
            actions = [a[1] for a in plan.timed_actions]
        elif isinstance(plan, SequentialPlan):
            actions = plan.actions
        else:
            raise NotImplementedError(f"Plan type {type(plan)} not supported")
        for a in actions:
            if a.action.name == "drive":
                cost += 10
            elif a.action.name == "lift":
                cost += 1
        return cost

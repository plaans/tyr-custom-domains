from pathlib import Path
from typing import Optional

from unified_planning.shortcuts import AbstractProblem

from tyr.problems.converter import remove_user_typing
from tyr.problems.model import FolderAbstractDomain
from tyr.problems.model.instance import ProblemInstance


class WarmUpDriverlogTimeDomain(FolderAbstractDomain):
    def __init__(self) -> None:
        super().__init__()
        self.folder = Path(__file__).parent

    def build_problem_flat(self, problem: ProblemInstance) -> Optional[AbstractProblem]:
        # Load the base problem
        base = problem.versions["base"].value
        if base is None:
            return None
        return remove_user_typing(base)

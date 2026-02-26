from pathlib import Path
from typing import Optional

from unified_planning.shortcuts import AbstractProblem

from tyr.problems.domains.custom.warm_up.domains.jobshop_base import (
    OPERATORS,
    parse_jobshop,
)
from tyr.problems.model import AbstractDomain, ProblemInstance

FOLDER = Path(__file__).parent.resolve() / "base"


class WarmUpJobshopSchedDomain(AbstractDomain):
    """Jobshop domain keeping the scheduling representation (not converted to PDDL).

    This allows Aries to handle it as a scheduling problem with hierarchical structure,
    simulating a hierarchy through the resource constraints and job precedence.
    """

    def get_num_problems(self) -> int:
        return (
            len(OPERATORS)
            * len([f for f in FOLDER.iterdir() if "instance" in f.name])
            // 2
        )

    def build_problem_base(self, problem: ProblemInstance) -> Optional[AbstractProblem]:
        if int(problem.uid) > self.get_num_problems():
            return None

        uid = int(problem.uid) - 1
        div = self.get_num_problems() // len(OPERATORS)
        ope = OPERATORS[uid // div]
        jsp_num = uid % div + 1

        # Return the scheduling problem directly without converting to PDDL actions
        return parse_jobshop(FOLDER / f"instance-{jsp_num}.jsp", ope)

from pathlib import Path
from typing import Optional

from unified_planning.shortcuts import AbstractProblem

from tyr.problems.domains.custom.warm_up.domains.rcpsp_base import (
    PSPLIB_parser,
    encode_rcpsp,
)
from tyr.problems.model import AbstractDomain, ProblemInstance

FOLDER = Path(__file__).parent.resolve() / "base"


class WarmUpRcpspSchedDomain(AbstractDomain):
    """RCPSP domain keeping the scheduling representation (not converted to PDDL).

    This allows Aries to handle it as a scheduling problem with hierarchical structure,
    simulating a hierarchy through the resource constraints and precedence relations.
    """

    def get_num_problems(self) -> int:
        return len([f for f in FOLDER.iterdir() if "instance" in f.name])

    def build_problem_base(self, problem: ProblemInstance) -> Optional[AbstractProblem]:
        if int(problem.uid) > self.get_num_problems():
            return None

        # Return the scheduling problem directly without converting to PDDL actions
        return encode_rcpsp(PSPLIB_parser(FOLDER / f"instance-{problem.uid}.sm"))

from pathlib import Path
from typing import Optional

from unified_planning.shortcuts import AbstractProblem, CompilationKind, Compiler

from tyr.problems.converter import scheduling_to_actions
from tyr.problems.domains.custom.warm_up.domains.rcpsp_base import (
    PSPLIB_parser,
    encode_rcpsp,
)
from tyr.problems.model import AbstractDomain, ProblemInstance

FOLDER = Path(__file__).parent.resolve() / "base"


class WarmUpRcpspNumDomain(AbstractDomain):
    """RCPSP domain converted to PDDL actions (numeric planning)."""

    def get_num_problems(self) -> int:
        return len([f for f in FOLDER.iterdir() if "instance" in f.name])

    def build_problem_base(self, problem: ProblemInstance) -> Optional[AbstractProblem]:
        if int(problem.uid) > self.get_num_problems():
            return None

        # Convert scheduling problem to PDDL actions
        scheduling_problem = encode_rcpsp(
            PSPLIB_parser(FOLDER / f"instance-{problem.uid}.sm")
        )
        return scheduling_to_actions(scheduling_problem)

    def build_problem_no_neg_cond(
        self, problem: ProblemInstance
    ) -> Optional[AbstractProblem]:
        base = problem.versions["base"].value
        if base is None:
            return None
        with Compiler(
            problem_kind=base.kind,
            compilation_kind=CompilationKind.NEGATIVE_CONDITIONS_REMOVING,
        ) as compiler:
            return compiler.compile(base).problem  # pylint: disable=no-member

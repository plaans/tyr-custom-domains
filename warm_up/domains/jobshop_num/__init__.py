from pathlib import Path
from typing import Optional

from unified_planning.shortcuts import AbstractProblem, CompilationKind, Compiler

from tyr.problems.converter import scheduling_to_actions
from tyr.problems.domains.custom.warm_up.domains.jobshop_base import (
    OPERATORS,
    parse_jobshop,
)
from tyr.problems.model import AbstractDomain, ProblemInstance

FOLDER = Path(__file__).parent.resolve() / "base"


class WarmUpJobshopNumDomain(AbstractDomain):
    """Jobshop domain converted to PDDL actions (numeric planning)."""

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

        # Convert scheduling problem to PDDL actions
        scheduling_problem = parse_jobshop(FOLDER / f"instance-{jsp_num}.jsp", ope)
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

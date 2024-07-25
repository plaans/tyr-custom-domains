from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Optional

from unified_planning.io import PDDLReader
from unified_planning.shortcuts import AbstractProblem

from tyr.problems.converter import reduce_problem, remove_user_typing
from tyr.problems.model import FolderAbstractDomain, ProblemInstance


class Aaai2025RoversDomain(FolderAbstractDomain):
    def __init__(self) -> None:
        super().__init__()
        self.folder = Path(__file__).parent

    def build_problem_no_div(
        self, problem: ProblemInstance
    ) -> Optional[AbstractProblem]:
        # Get the base version of the problem.
        base = problem.versions["base"].value
        if base is None:
            return None

        # Load the domain of the no_div version from a PDDL file.
        no_div = PDDLReader().parse_problem(
            (Path(__file__).parent / "domain_no_div.pddl").as_posix()
        )

        # Add all objects.
        no_div.add_objects(base.all_objects)

        # Initialize all state variable not involved in a division
        # and save skipped one in a map for future access.
        saved_values: Dict[str, Dict[tuple, Any]] = defaultdict(dict)
        for sv, value in base.explicit_initial_values.items():
            fluent = sv.fluent()
            if fluent.name in ["energy", "recharge-rate"]:
                saved_values[fluent.name][tuple(map(str, sv.args))] = value
            else:
                no_div.set_initial_value(no_div.fluent(fluent.name)(*sv.args), value)

        # Replace state variables involved in a division by static ones.
        for x in no_div.objects(no_div.user_type("rover")):
            energy = saved_values["energy"][(x.name,)]
            rate = saved_values["recharge-rate"][(x.name,)]
            # pylint: disable=eval-used
            atom = int(round(eval(str(1 / rate * 100))))  # nosec: B307
            for multi, suffix in [
                (energy, ""),
                (80, "-max"),
                *((i, f"-{i}") for i in range(1, 9) if i != 7),
            ]:
                sv = no_div.fluent(f"recharge-duration{suffix}")(x)
                value = int(eval(str(atom * multi)))  # nosec: B307
                no_div.set_initial_value(sv, value)

        # Add all goals.
        for x in base.goals:
            no_div.add_goal(x)

        # Add the metrics.
        for x in base.quality_metrics:
            no_div.add_quality_metric(x)

        return reduce_problem(no_div, int(problem.uid) % 5 + 1)

    def build_problem_no_div_flat(
        self, problem: ProblemInstance
    ) -> Optional[AbstractProblem]:
        no_div = problem.versions["no_div"].value
        if no_div is None:
            return None
        return remove_user_typing(no_div)

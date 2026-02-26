from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Optional

from unified_planning.io import PDDLReader
from unified_planning.shortcuts import AbstractProblem

from tyr.problems.converter import reduce_version, remove_user_typing
from tyr.problems.model import FolderAbstractDomain, ProblemInstance

class WarmUpDepotsNumDomain(FolderAbstractDomain):
    def __init__(self) -> None:
        super().__init__()
        self.folder = Path(__file__).parent

    def build_problem_red(self, problem: ProblemInstance) -> Optional[AbstractProblem]:
        return reduce_version(problem, "base", int(problem.uid) % 5 + 1)

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
            if fluent.name in ["speed", "distance", "weight", "power"]:
                saved_values[fluent.name][tuple(map(str, sv.args))] = value
            else:
                no_div.set_initial_value(no_div.fluent(fluent.name)(*sv.args), value)

        # Replace state variables involved in a division by static ones.
        for x in no_div.objects(no_div.user_type("truck")):
            for y in no_div.objects(no_div.user_type("place")):
                for z in no_div.objects(no_div.user_type("place")):
                    sv = no_div.fluent("drive_duration")(x, y, z)
                    distance = saved_values["distance"][(y.name, z.name)]
                    speed = saved_values["speed"][(x.name,)]
                    value = int(distance.constant_value() / speed.constant_value() * 10)
                    no_div.set_initial_value(sv, value)

        for x in no_div.objects(no_div.user_type("hoist")):
            for y in no_div.objects(no_div.user_type("crate")):
                sv = no_div.fluent("load_duration")(x, y)
                weight = saved_values["weight"][(y.name,)]
                power = saved_values["power"][(x.name,)]
                value = int(weight.constant_value() / power.constant_value() * 10)
                no_div.set_initial_value(sv, value)

        # Add all goals.
        for x in base.goals:
            no_div.add_goal(x)

        # Add the metrics.
        for x in base.quality_metrics:
            no_div.add_quality_metric(x)

        return no_div

    def build_problem_red_no_div(
        self, problem: ProblemInstance
    ) -> Optional[AbstractProblem]:
        return reduce_version(problem, "no_div", int(problem.uid) % 5 + 1)

    def build_problem_flat(self, problem: ProblemInstance) -> Optional[AbstractProblem]:
        """Build flat version (no user typing) of the base problem.

        This version removes user-defined types, which is useful for planners
        that don't support typed PDDL or have issues with type hierarchies.
        """
        base = problem.versions["base"].value
        if base is None:
            return None
        return remove_user_typing(base)

    def build_problem_flat_no_div(
        self, problem: ProblemInstance
    ) -> Optional[AbstractProblem]:
        """Build flat version (no user typing) of the no_div problem.

        This combines both the no_div transformation (removing division operations)
        and the flat transformation (removing user-defined types).
        """
        no_div = problem.versions["no_div"].value
        if no_div is None:
            return None
        return remove_user_typing(no_div)

    def build_problem_red_flat(
        self, problem: ProblemInstance
    ) -> Optional[AbstractProblem]:
        """Build reduced flat version.

        This applies goal reduction to the flat (untyped) version of the problem.
        """
        return reduce_version(problem, "flat", int(problem.uid) % 5 + 1)

    def build_problem_red_flat_no_div(
        self, problem: ProblemInstance
    ) -> Optional[AbstractProblem]:
        """Build reduced flat version without divisions.

        This applies goal reduction to the flat_no_div version, combining all three
        transformations: reduced goals, no divisions, and no user types.
        """
        return reduce_version(problem, "flat_no_div", int(problem.uid) % 5 + 1)

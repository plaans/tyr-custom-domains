from pathlib import Path

from tyr.problems.model import FolderAbstractDomain

from .aaai_2025 import *


def is_domain_dir(p: Path) -> bool:
    return p.is_dir() and not p.name.startswith("__") and not p.name.startswith(".")


for paper in (Path(__file__).parent).iterdir():
    if is_domain_dir(paper):
        for dom in (paper / "domains").iterdir():
            if is_domain_dir(dom):
                register = True
                for file in dom.iterdir():
                    if file.name == "__init__.py":
                        register = False
                        break
                if not register:
                    continue

                name = (
                    (paper.name.title() + dom.name.title() + "Domain")
                    .replace("-", "")
                    .replace("_", "")
                )
                globals()[name] = type(
                    name,
                    (FolderAbstractDomain,),
                    {"folder": dom},
                )

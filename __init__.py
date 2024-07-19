from pathlib import Path

from tyr.problems.model import FolderAbstractDomain

from .aaai_2025 import *

for paper in (Path(__file__).parent).iterdir():
    if paper.is_dir() and paper.name != "__pycache__":
        for dom in (paper / "domains").iterdir():
            if dom.is_dir() and dom.name != "__pycache__":
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
                print(name)
                globals()[name] = type(
                    name,
                    (FolderAbstractDomain,),
                    {"folder": dom},
                )

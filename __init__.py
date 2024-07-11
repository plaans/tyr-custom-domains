from pathlib import Path

from tyr.problems.model import FolderAbstractDomain

from .domains import *

for dom in (Path(__file__).parent / "domains").iterdir():
    if dom.is_dir() and dom.name != "__pycache__":
        register = True
        for file in dom.iterdir():
            if file.name == "__init__.py":
                register = False
                break
        if not register:
            continue

        name = ("Custom" + dom.name.title() + "Domain").replace("-", "")
        globals()[name] = type(
            name,
            (FolderAbstractDomain,),
            {"folder": dom},
        )

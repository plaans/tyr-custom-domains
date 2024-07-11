from pathlib import Path

from tyr.problems.model import FolderAbstractDomain


for dom in (Path(__file__).parent / "domains").iterdir():
    if dom.is_dir():
        name = ("Custom" + dom.name.title() + "Domain").replace("-", "")
        globals()[name] = type(
            name,
            (FolderAbstractDomain,),
            {"folder": dom},
        )

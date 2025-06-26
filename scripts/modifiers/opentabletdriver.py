# .config/OpenTabletDriver

import json
from pathlib import Path

FILE = Path(__file__).parents[2] / ".config/OpenTabletDriver/settings.json"
MAPPING = {
    "OpenTabletDriver.Desktop.Output.LinuxArtistMode": "OpenTabletDriver.Desktop.Output.AbsoluteMode",
    "OpenTabletDriver.Desktop.Output.AbsoluteMode": "OpenTabletDriver.Desktop.Output.LinuxArtistMode",
}


def to():
    if not FILE.exists():
        return
    data = json.loads(FILE.read_text())
    for i in data.get("Profiles", []):
        if i["OutputMode"]["Path"] in MAPPING:
            i["OutputMode"]["Path"] = MAPPING[i["OutputMode"]["Path"]]
    FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False))

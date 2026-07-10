from pathlib import Path

import yaml

from github_profile.models import Profile


def load_profile(path: Path) -> Profile:
    if not path.exists():
        raise FileNotFoundError(f"Profile file not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        raw_data = yaml.safe_load(file)

    return Profile.model_validate(raw_data)
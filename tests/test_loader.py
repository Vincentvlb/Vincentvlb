from pathlib import Path

import pytest
from pydantic import ValidationError

from github_profile.loader import load_profile


def test_load_valid_profile(tmp_path: Path) -> None:
    config = tmp_path / "profile.yaml"
    config.write_text(
        """
identity:
  name: Vincent Lambert
  title: Robotics Engineer • AI • Embedded Systems
  tagline: Building products, not just software.
  location: La Rochelle, France
  languages:
    - French
    - English

robot_identity:
  enabled: true
  mission: Build complete robotic products.

engineering_domains:
  enabled: true
  robotics:
    - ROS 2
  computer_vision:
    - YOLOv26
  embedded_systems:
    - STM32
  software:
    - Python
  infrastructure:
    - Docker

learning:
  enabled: true
  topics:
    - SwiftUI

engineering_highlights:
  - title: NAVX
    description: High-precision GNSS receiver.
    impact: Complete product development.
    details:
      - PCB design
""",
        encoding="utf-8",
    )

    profile = load_profile(config)

    assert profile.identity.name == "Vincent Lambert"
    assert profile.identity.languages == ["French", "English"]
    assert profile.engineering_highlights[0].title == "NAVX"


def test_load_missing_profile() -> None:
    with pytest.raises(FileNotFoundError):
        load_profile(Path("missing-profile.yaml"))


def test_load_invalid_profile(tmp_path: Path) -> None:
    config = tmp_path / "profile.yaml"
    config.write_text(
        """
identity:
  name: Vincent Lambert
""",
        encoding="utf-8",
    )

    with pytest.raises(ValidationError):
        load_profile(config)
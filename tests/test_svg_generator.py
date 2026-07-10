from pathlib import Path

from github_profile.generators.svg import generate_svg
from github_profile.models import (
    EngineeringDomains,
    Identity,
    Learning,
    Profile,
    RobotIdentity,
)


def create_test_profile() -> Profile:
    return Profile(
        identity=Identity(
            name="Vincent Lambert",
            title="Robotics Engineer • AI • Embedded Systems",
            tagline="Building products, not just software.",
            location="La Rochelle, France",
            languages=["French", "English"],
        ),
        robot_identity=RobotIdentity(
            enabled=True,
            mission="Build complete robotic products.",
        ),
        engineering_domains=EngineeringDomains(
            enabled=True,
            robotics=[],
            computer_vision=[],
            embedded_systems=[],
            software=[],
            infrastructure=[],
        ),
        learning=Learning(
            enabled=True,
            topics=[],
        ),
        engineering_highlights=[],
    )


def test_generate_svg(tmp_path: Path) -> None:
    template = tmp_path / "hero.svg.j2"
    output = tmp_path / "generated" / "hero.svg"

    template.write_text(
        """<svg xmlns="http://www.w3.org/2000/svg">
  <text>{{ profile.identity.name }}</text>
</svg>
""",
        encoding="utf-8",
    )

    generate_svg(
        profile=create_test_profile(),
        template_path=template,
        output_path=output,
    )

    content = output.read_text(encoding="utf-8")

    assert output.exists()
    assert "<svg" in content
    assert "Vincent Lambert" in content
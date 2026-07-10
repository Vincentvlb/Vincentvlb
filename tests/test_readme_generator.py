from pathlib import Path

from github_profile.generators.readme import generate_readme
from github_profile.models import (
    EngineeringDomains,
    EngineeringHighlight,
    Identity,
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
            robotics=["ROS 2"],
            computer_vision=["YOLOv26"],
            embedded_systems=["STM32"],
            software=["Python"],
            infrastructure=["Docker"],
        ),
        engineering_highlights=[
            EngineeringHighlight(
                title="NAVX",
                description="High-precision GNSS receiver.",
                impact="Complete product development.",
                details=["PCB design", "Embedded firmware"],
                url="https://example.com/navx",
            )
        ],
    )


def test_generate_readme(tmp_path: Path) -> None:
    template = tmp_path / "README.md.j2"
    output = tmp_path / "README.md"

    template.write_text(
        """# {{ profile.identity.name }}

{{ profile.identity.tagline }}

{% for highlight in profile.engineering_highlights %}
## {{ highlight.title }}

{{ highlight.description }}
{% endfor %}
""",
        encoding="utf-8",
    )

    generate_readme(
        profile=create_test_profile(),
        template_path=template,
        output_path=output,
    )

    content = output.read_text(encoding="utf-8")

    assert "# Vincent Lambert" in content
    assert "Building products, not just software." in content
    assert "## NAVX" in content
    assert "High-precision GNSS receiver." in content


def test_generate_readme_creates_parent_directory(tmp_path: Path) -> None:
    template = tmp_path / "README.md.j2"
    output = tmp_path / "generated" / "README.md"

    template.write_text(
        "{{ profile.identity.name }}",
        encoding="utf-8",
    )

    generate_readme(
        profile=create_test_profile(),
        template_path=template,
        output_path=output,
    )

    assert output.exists()
    assert output.read_text(encoding="utf-8") == "Vincent Lambert"
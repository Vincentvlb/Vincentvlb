from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from github_profile.models import Profile


def generate_svg(
    profile: Profile,
    template_path: Path,
    output_path: Path,
) -> None:
    """Generate an SVG asset from a Jinja2 template."""

    if not template_path.exists():
        raise FileNotFoundError(f"SVG template file not found: {template_path}")

    environment = Environment(
        loader=FileSystemLoader(template_path.parent),
        undefined=StrictUndefined,
        autoescape=True,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    template = environment.get_template(template_path.name)
    rendered_content = template.render(profile=profile)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered_content, encoding="utf-8")
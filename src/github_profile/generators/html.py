from pathlib import Path
from shutil import copy2

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from github_profile.models import Profile


def generate_navx_viewer(
    profile: Profile,
    template_path: Path,
    model_path: Path,
    output_directory: Path,
) -> None:
    """Generate the NAVX 3D viewer and copy its GLB model."""

    if not template_path.exists():
        raise FileNotFoundError(
            f"HTML template file not found: {template_path}"
        )

    if not model_path.exists():
        raise FileNotFoundError(
            f"NAVX GLB model not found: {model_path}"
        )

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

    output_directory.mkdir(parents=True, exist_ok=True)

    html_output = output_directory / "index.html"
    model_output = output_directory / "navx.glb"

    html_output.write_text(rendered_content, encoding="utf-8")
    copy2(model_path, model_output)
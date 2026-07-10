from pathlib import Path

import typer
from jinja2 import TemplateError
from pydantic import ValidationError
from rich.console import Console

from github_profile.generators.readme import generate_readme
from github_profile.loader import load_profile
from github_profile.generators.svg import generate_svg
from github_profile.generators.html import generate_navx_viewer

app = typer.Typer(
    name="profile",
    help="Generate and validate Vincent's GitHub profile.",
    no_args_is_help=True,
)

console = Console()


def read_profile(config: Path):
    """Load and validate the profile or stop the CLI cleanly."""

    try:
        return load_profile(config)
    except FileNotFoundError as error:
        console.print(f"[red]✗[/red] {error}")
        raise typer.Exit(code=1) from error
    except ValidationError as error:
        console.print("[red]✗ Invalid profile configuration[/red]")
        console.print(error)
        raise typer.Exit(code=1) from error


@app.command()
def check(
    config: Path = typer.Option(
        Path("profile.yaml"),
        "--config",
        "-c",
        help="Path to the profile configuration file.",
    ),
) -> None:
    """Validate the profile configuration."""

    profile = read_profile(config)

    console.print("[green]✓[/green] Profile configuration is valid.")
    console.print(f"  Name: {profile.identity.name}")
    console.print(f"  Title: {profile.identity.title}")
    console.print(f"  Location: {profile.identity.location}")


@app.command()
def generate(
    config: Path = typer.Option(
        Path("profile.yaml"),
        "--config",
        "-c",
        help="Path to the profile configuration file.",
    ),
    template: Path = typer.Option(
        Path("templates/README.md.j2"),
        "--template",
        "-t",
        help="Path to the Jinja2 README template.",
    ),
    output: Path = typer.Option(
        Path("README.md"),
        "--output",
        "-o",
        help="Output path for the generated README.",
    ),
) -> None:
    """Generate the GitHub profile README."""

    profile = read_profile(config)

    try:
        generate_readme(
            profile=profile,
            template_path=template,
            output_path=output,
        )
        console.print(f"[green]✓[/green] Generated: {output}")
        generate_svg(
            profile=profile,
            template_path=Path("templates/hero.svg.j2"),
            output_path=Path("assets/generated/hero.svg"),
        )
        console.print("[green]✓[/green] Generated: assets/generated/hero.svg")
        generate_svg(
            profile=profile,
            template_path=Path("templates/engineering-profile.svg.j2"),
            output_path=Path("assets/generated/engineering-profile.svg"),
        )
        console.print(
            "[green]✓[/green] Generated: assets/generated/engineering-profile.svg"
        )
        generate_svg(
            profile=profile,
            template_path=Path("templates/engineering-cycle.svg.j2"),
            output_path=Path("assets/generated/engineering-cycle.svg"),
        )
        console.print(
            "[green]✓[/green] Generated: assets/generated/engineering-cycle.svg"
        )
        generate_svg(
            profile=profile,
            template_path=Path("templates/technical-stack.svg.j2"),
            output_path=Path("assets/generated/technical-stack.svg"),
        )
        console.print(
            "[green]✓[/green] Generated: assets/generated/technical-stack.svg"
        )
        generate_svg(
            profile=profile,
            template_path=Path("templates/highlights-header.svg.j2"),
            output_path=Path("assets/generated/highlights-header.svg"),
        )
        console.print(
            "[green]✓[/green] Generated: assets/generated/highlights-header.svg"
        )
        generate_svg(
            profile=profile,
            template_path=Path("templates/navx-card.svg.j2"),
            output_path=Path("assets/generated/navx-card.svg"),
        )
        console.print(
            "[green]✓[/green] Generated: assets/generated/navx-card.svg"
        )
        generate_svg(
            profile=profile,
            template_path=Path("templates/qfield-card.svg.j2"),
            output_path=Path("assets/generated/qfield-card.svg"),
        )
        console.print(
            "[green]✓[/green] Generated: assets/generated/qfield-card.svg"
        )
        generate_svg(
            profile=profile,
            template_path=Path("templates/vision-pipeline-card.svg.j2"),
            output_path=Path("assets/generated/vision-pipeline-card.svg"),
        )
        console.print(
            "[green]✓[/green] Generated: assets/generated/vision-pipeline-card.svg"
        )
        generate_navx_viewer(
            profile=profile,
            template_path=Path("templates/navx-viewer.html.j2"),
            model_path=Path("assets/navx/navx.glb"),
            output_directory=Path("docs/navx"),
        )
        console.print(
            "[green]✓[/green] Generated: docs/navx/index.html"
        )
        console.print(
            "[green]✓[/green] Copied: docs/navx/navx.glb"
        )
        
    except (FileNotFoundError, TemplateError) as error:
        console.print(f"[red]✗ Generation failed:[/red] {error}")
        raise typer.Exit(code=1) from error

@app.command()
def version() -> None:
    """Display the generator version."""

    console.print("GitHub Profile Generator 0.1.0")
import typer
from pathlib import Path

from dev_doctor.config import load_config
from dev_doctor.runner import run_checks
from dev_doctor.reporting import print_report

app = typer.Typer(help="Healthchecks-as-code for development environments.")


@app.command()
def init():
    """
    Create a sample .devdoctor.yml in the current directory.
    """
    target = Path(".devdoctor.yml")
    if target.exists():
        typer.echo("❌ .devdoctor.yml already exists.")
        raise typer.Exit(code=1)

    sample = Path(__file__).parent.parent / "examples" / ".devdoctor.yml"
    target.write_text(sample.read_text())
    typer.echo("✅ Created .devdoctor.yml")


@app.command()
def run(config: Path = Path(".devdoctor.yml")):
    """
    Run all configured checks.
    """
    if not config.exists():
        typer.echo(f"❌ Config not found: {config}")
        raise typer.Exit(code=1)

    cfg = load_config(config)
    results = run_checks(cfg["checks"])
    print_report(results)

    if any(r.required and not r.passed for r in results):
        raise typer.Exit(code=1)


@app.command()
def list(config: Path = Path(".devdoctor.yml")):
    """
    List configured checks.
    """
    cfg = load_config(config)
    for check in cfg["checks"]:
        typer.echo(f"- {check['name']} ({check['type']})")

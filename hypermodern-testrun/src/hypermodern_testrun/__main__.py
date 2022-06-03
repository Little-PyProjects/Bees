"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Hypermodern Testrun."""


if __name__ == "__main__":
    main(prog_name="hypermodern-testrun")  # pragma: no cover

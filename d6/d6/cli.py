import os
import click
import random


class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(os.path.join(os.path.dirname(__file__), "commands")):
            if filename.endswith(".py") and not filename.startswith("__"):
                rv.append(filename.replace('.py', ''))
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"d6.commands.{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli


@click.command(cls=ComplexCLI)
def cli():
    """ d6 - The CLI dice roll generator. Base usage d6 {number of}{sided dice}.
    e.g., d6 2d20 -- generates two 20 sided dice rolls
    """
    pass

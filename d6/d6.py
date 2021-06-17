import click
import random

@click.command()

@click.argument('num', nargs=1, default=1)
@click.argument('d', nargs=1, default=6)

def roll_em(num, d):
    """Random dice roll generator"""
    for _ in range(num):
        click.echo(f"{random.randint(1,d)}")

# @click.option("--sort", help="Return results in order from low to high")
# @click.option("--discard", help="discards lowest n rolls")
# @click.option("--number", help="number of dice to roll")

if __name__ == '__main__':
    roll_em()

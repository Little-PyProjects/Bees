import click
import random

# @click.group()
# def cli():
#     pass

@click.argument('ndx')

@click.command()
def parse(ndx):
    """CLI dice generator"""
    c = tuple(ndx.split('d'))
    num, d = c[0], c[1]
    click.echo(f"{num} {d}")

# @click.command()
# def gen(num, d):
#     """Random dice roll generator"""
#     for _ in range(num):
#         click.echo(f"{random.randint(1,d)}")

# cli.add_command(parse)
# cli.add_command(gen)

# @click.option('-s', '--sort', help="Return sorted results. Default: low to high")
# #@click.option('-d', "--discard", help="discards roll(s). Default: low roll(s)")

if __name__ == '__main__':
    parse()

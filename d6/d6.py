import click
import random


@click.argument('ndx')

@click.command()
def parse(ndx):
    """Parses input such that 3d6 becomes 3 rolls of 6 sided dice"""
    c = tuple(ndx.split('d'))
    num, d = c[0], c[1]
    print(num, d)


# def generate_rolls(num, d):
#     pass

if __name__ == '__main__':
    parse()
    
import click
import random

@click.command()


# @click.option('-s', '--sort', help="Return results in order from low to high")
# @click.option('-d', "--discard", help="discards lowest n rolls")

@click.argument('ndx')

def parse(ndx):
    c = tuple(ndx.split('d'))
    print(c)
    # c,d = ndx[0], ndx[1]

# def roll_em(num, d):
#     """Random dice roll generator"""
#     for _ in range(num):
#         click.echo(f"{random.randint(1,d)}")



if __name__ == '__main__':
    parse()

import click
import random

<<<<<<< HEAD

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
    
=======
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
>>>>>>> 9da0032a48153926bfa04aebf01cfff987fb1018

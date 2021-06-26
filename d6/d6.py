# import click
# import random

# @click.group(invoke_without_command=True, chain=True)
# def cli():
#     pass

# # @click.option('-s', '--sort', is_flag=True, help="Return sorted results. Default: low to high")
# # def sort(sort):
# #     if sort:
# #         pass
# #     click.echo(gen.sorted())

# # @click.option('-d', "--discard", default=None,  help="discards roll(s). Default: low roll(s)")

# @click.argument('ndx', default='1d6')

# @cli.command()
# def cli(ndx):
#     """ d6 - The CLI dice roll generator. Base usage d6 {number of}{sided dice}.
#     e.g., d6 2d20 -- generates two 20 sided dice rolls
#     """
#     click.echo(ndx)

# # @cli.command()
# # def parse(ndx):
# #     """CLI dice generator"""
# #     c = tuple(ndx.split('d'))
# #     num, d = c[0], c[1]
# #     # click.echo(f"{num} {d}")
# #     return num, d

# # @click.command(num, d)
# # def gen(num, d):
# #     """Random dice roll generator"""
# #     for _ in range(num):
# #         click.echo(f"{random.randint(1,d)}")

# # cli.add_command(parse)
# # cli.add_command(gen)


# if __name__ == '__main__':
#     cli()
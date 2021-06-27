import click

@click.group(invoke_without_command=True, chain=True)
def cli():
    """ d6 - The CLI dice roll generator. Base usage d6 {number of}{sided dice}.
    e.g., d6 2d20 -- generates two 20 sided dice rolls
    """
    #parse()
    click.echo(ndx)


@cli.command()
@click.argument('ndx')
def parse(ndx):
    """{number of rolls}d{dice sides} eg 2d20"""
    c = tuple(ndx.split('d'))
    num, d = c[0], c[1]
    # click.echo(f"{num} {d}")
    return num, d

@cli.command()
def sortin():
    pass

# # @click.option('-s', '--sort', is_flag=True, help="Return sorted results. Default: low to high")
# # def sort(sort):
# #     if sort:
# #         pass
# #     click.echo(gen.sorted())

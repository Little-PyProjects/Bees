import click

class Context:
    def __init__(self) -> None:
        self.ndx

@click.group(invoke_without_command=True, chain=True)
@click.option('-s', '--sort', is_flag=True, help="Return sorted results. Default: low to high")
# # def sort(sort):
# #     if sort:
# #         pass
# #     click.echo(gen.sorted())

@click.pass_context
def cli(ctx, sort):
    """ d6 - The CLI dice roll generator """
    # parse()
    ctx.obj = Context(ntx)


@cli.command()
@click.pass_context(ctx)
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

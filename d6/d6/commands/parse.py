import click

@click.group(invoke_without_command=True, chain=True)
def cli():
    pass

@cli.command()
@click.argument('ndx')
def parse(ndx):
    """CLI dice generator"""
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

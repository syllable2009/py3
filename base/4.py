import click

@click.command()
@click.option("--name", default="li", help="your name")
@click.option("--age", default=26,type=int, help="your age")
def hello_world(name, age):
    click.echo(name)
    print(age)
hello_world()

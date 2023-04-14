import click

from app.comands.configuration import configurations
from app.comands.home import home


@click.group()
def main():
    pass


if __name__ == '__main__':
    main.add_command(home)
    main.add_command(configurations)
    main()

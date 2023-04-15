import click

from app.comands.configuration import configurations
from app.comands.home import home
from app.domain.errors import AppError
from app.utils.config import AppConfig


@click.group()
def main():
    pass


if __name__ == '__main__':
    main.add_command(home)
    main.add_command(configurations)
    click.echo()
    try:
        main()
    except AppError as e:
        click.echo(f'An error occurred: {str(e)}\n', err=True)
        click.echo(
            f"For more information check the documentation at {AppConfig().config['DEFAULT']['DOCUMENTATIONLINK']}", err=True)

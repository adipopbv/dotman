import os

import click

from app.domain.errors import NotFoundError
from app.domain.validations import valid_dotfiles_home
from app.utils.config import AppConfig


@click.group(name='config', help='Configurations related commands')
def configurations():
    pass


@configurations.command(name='list', help='List all available configurations')
@valid_dotfiles_home
def list_all_configurations():
    """
    List all available configurations
    :return: None
    """
    click.echo('Listing all available configurations...\n')
    try:
        if len(os.listdir(os.path.expanduser(AppConfig().config['DEFAULT']['DOTFILESCONFIGS']))) == 0:
            click.echo('No configurations found')
            return
        [print(config_name) for config_name in
         os.listdir(os.path.expanduser(AppConfig().config['DEFAULT']['DOTFILESCONFIGS']))]
    except FileNotFoundError:
        raise NotFoundError('No configurations directory found')


@configurations.command(name='create', help='Create a new configuration')
@click.argument('name')
@valid_dotfiles_home
def create_new_configuration(name):
    """
    Create a new configuration
    :param name: The name of the new configuration
    :return: None
    """
    click.echo('Creating a new configuration...\n')
    if not os.path.exists(os.path.expanduser(f"{AppConfig().config['DEFAULT']['DOTFILESCONFIGS']}/{name}")):
        click.echo('Creating configuration directory...')
        os.makedirs(os.path.expanduser(f"{AppConfig().config['DEFAULT']['DOTFILESCONFIGS']}/{name}"))
    else:
        click.echo('A configuration with the same name already exists')
        click.echo('Do you want to overwrite it?')
        if click.confirm('Overwrite?'):
            click.echo('Overwriting configuration...')
            os.makedirs(os.path.expanduser(f"{AppConfig().config['DEFAULT']['DOTFILESCONFIGS']}/{name}"), exist_ok=True)

    click.echo('\nConfiguration created successfully')

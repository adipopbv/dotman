import os

import click

from app.utils.config import AppConfig


@click.group(name='config', help='Configurations related commands')
def configurations():
    pass


@configurations.command(name='list', help='List all available configurations')
def list_all_configurations():
    """
    List all available configurations
    :return: None
    """
    click.echo('Listing all available configurations...\n')
    try:
        print([config_name for config_name in
               os.listdir(os.path.expanduser(AppConfig().config['DEFAULT']['DOTFILESPATH'] + '/configs'))])
    except FileNotFoundError:
        if not os.path.exists(os.path.expanduser(AppConfig().config['DEFAULT']['DOTFILESPATH'])):
            click.echo('No dotfiles home directory structure found')
            click.echo('You can create a new dotfiles home with the command: dotman home init')
            click.echo(
                'Or you can get your already existent dotfiles home from git with the command: dotman home clone <url>')
        else:
            click.echo('No configurations found')
            click.echo('Create a new configuration with the command: config create <name>')

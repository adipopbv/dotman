import os

import click
import distro
import git

from app.domain.errors import DuplicateError, AppError
from app.utils.config import AppConfig


@click.group(name='home', help='Dotfiles home related commands')
def home():
    pass


@home.command(name='init', help='Initialize a new dotfiles home and git repository')
@click.option('--empty', is_flag=True, help='Initialize an empty dotfiles home')
def init_home_and_repo(empty=False):
    """
    Initialize a new dotfiles home and git repository
    :return: None
    """
    click.echo('Initializing a new dotfiles home and git repository...\n')

    if os.path.exists(os.path.expanduser(AppConfig().config['DOTFILES']['HomePath'])):
        raise DuplicateError('A dotfiles home already exists')
    click.echo('Creating dotfiles home directory...')
    os.makedirs(os.path.expanduser(AppConfig().config['DOTFILES']['HomePath']))
    if not empty:
        click.echo('Creating configurations directory...')
        os.makedirs(os.path.expanduser(AppConfig().config['DOTFILES']['ConfigsPath']))

        click.echo('Creating current configuration directory...')
        os.makedirs(os.path.expanduser(AppConfig().config['DOTFILES']['CurrentConfigPath']))

        click.echo('Creating packages directory...')
        os.makedirs(os.path.expanduser(AppConfig().config['DOTFILES']['PackagesPath']))
        open(os.path.expanduser(f"{AppConfig().config['DOTFILES']['PackagesPath']}/fedora-dnf.txt"), 'a').close()
        open(os.path.expanduser(f"{AppConfig().config['DOTFILES']['PackagesPath']}/flatpak.txt"), 'a').close()
        current_distro = distro.id()
        if current_distro not in AppConfig().config['PACKAGES']['SupportedDistros'].split(','):
            raise AppError(f'Unsupported distro: {current_distro}')
        # os.system('sudo dnf update -y')
        # os.system(
        #     "sudo dnf install -y $(cat {AppConfig().config['DOTFILES']['PackagesPath']}/fedora-dnf.txt) > /dev/null "
        #     "2>&1")

        click.echo('Creating scripts directory...')
        os.makedirs(os.path.expanduser(AppConfig().config['DOTFILES']['ScriptsPath']))

    click.echo('Initializing git repository...')
    git.Repo.init(os.path.expanduser(AppConfig().config['DOTFILES']['HomePath']))

    click.echo('\nDotfiles home initialized successfully')


@home.command(name='get', help='Get an existent dotfiles home from git')
@click.argument('url')
def get_home_from_git(url):
    """
    Get an existent dotfiles home from git
    :param url: The url of the git repository
    :return: None
    """
    click.echo('Getting an existent dotfiles home from git...\n')

    if os.path.exists(os.path.expanduser(AppConfig().config['DEFAULT']['DOTFILESHOME'])):
        raise DuplicateError('A dotfiles home already exists')
    click.echo('Cloning git repository...')
    git.Repo.clone_from(url, os.path.expanduser(AppConfig().config['DEFAULT']['DOTFILESHOME']))

    click.echo('\nDotfiles home cloned successfully')

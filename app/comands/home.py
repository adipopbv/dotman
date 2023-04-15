import os

import click
import git

from app.domain.errors import DuplicateError
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

    if os.path.exists(os.path.expanduser(AppConfig().config['DEFAULT']['DOTFILESHOME'])):
        raise DuplicateError('A dotfiles home already exists')
    click.echo('Creating dotfiles home directory...')
    os.makedirs(os.path.expanduser(AppConfig().config['DEFAULT']['DOTFILESHOME']))
    if not empty:
        click.echo('Creating configurations directory...')
        os.makedirs(os.path.expanduser(AppConfig().config['DEFAULT']['DOTFILESCONFIGS']))
    click.echo('Initializing git repository...')
    git.Repo.init(os.path.expanduser(AppConfig().config['DEFAULT']['DOTFILESHOME']))

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

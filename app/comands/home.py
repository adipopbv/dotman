import click


@click.group(name='home', help='Dotfiles home related commands')
def home():
    pass


@home.command(name='init', help='Initialize a new dotfiles home and git repository')
@click.option('--no-git', is_flag=False, help='Do not initialize a git repository')
def init_home_and_repo():
    """
    Initialize a new dotfiles home and git repository
    :return: None
    """
    click.echo('Initializing a new dotfiles home and git repository...\n')


@home.command(name='clone', help='Clone an existent dotfiles home from git')
@click.argument('url')
def clone_home_from_git(url):
    """
    Clone an existent dotfiles home from git
    :param url: The url of the git repository
    :return: None
    """
    click.echo('Cloning an existent dotfiles home from git...\n')

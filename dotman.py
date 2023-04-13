import os

import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--globally', '-g', is_flag=True, help='Install dotman globally')
def install(globally):
    """
    Install dotman on the current Unix-based system
    :param globally: should dotman be installed globally (in /usr/local/bin) or locally (in ~/.local/bin)
    :return: None
    """
    try:
        if globally:
            if os.path.exists('/usr/local/bin/dotman'):
                click.echo('dotman is already installed globally')
                return
            click.echo('Installing dotman globally')
            os.system('sudo cp ' + os.path.abspath('./dotman') + ' /usr/local/bin')
        else:
            if os.path.exists(os.path.expanduser('~/.local/bin/dotman')):
                click.echo('dotman is already installed locally')
                return
            click.echo('Installing dotman locally')
            os.symlink(os.path.abspath('./dotman'), os.path.expanduser('~/.local/bin/dotman'))
    except OSError as e:
        click.echo('Error: {}'.format(e))
        click.echo('Please run this command with sudo')


if __name__ == '__main__':
    cli()

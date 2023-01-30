import click

from notebook import notebookapp as app
import subprocess

from ape.cli import NetworkBoundCommand, ape_cli_context, network_option


@click.command(
    cls=NetworkBoundCommand,
    short_help="Run a notebook server"
)
@network_option()
@ape_cli_context()
def cli(cli_ctx, network):
    args = ["ipython", "kernel", "install", "--name", "ape", "--user"]
    subprocess.run(args)
    app.launch_new_instance()

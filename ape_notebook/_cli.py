import click
from notebook.app import launch_new_instance  # type: ignore


# %%
@click.command(short_help="Run a notebook server")
def cli():
    launch_new_instance()

import click

from notebook.notebookapp import launch_new_instance


# %%
@click.command(short_help="Run a notebook server")
def cli():
    launch_new_instance()

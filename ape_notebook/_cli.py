import click
from notebook import notebookapp  # type: ignore[attr-defined]


# %%
@click.command(short_help="Run a notebook server")
def cli():
    notebookapp.launch_new_instance()

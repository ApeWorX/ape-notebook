# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: elf-env
#     language: python
#     name: python3
# ---

# %%
import click

# %%
import notebook


# %%
@click.command(short_help="Run a notebook server")
def cli():
    notebook.notebookapp.app.launch_new_instance()

# %%

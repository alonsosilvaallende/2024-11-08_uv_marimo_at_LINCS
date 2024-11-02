# ---
# title: "uv+marimo"
# author: "Alonso Silva"
# format:
#   revealjs:
#     toc: true
#     toc-depth: 1
#     slide-number: true
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Introduction
#
# This is the introduction

# %% [markdown]
# ## Installation
#
# ### Standalone installer
# ```shell
# curl -LsSf https://astral.sh/uv/install.sh | sh
# ```

# %% [markdown]
# ## Common workflow
#
# Following the [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).
#
# ::: {.callout-tip}
# It is recommended to use a virtual environment when working with third party packages.
# :::
#
# ```shell
# python -m venv .venv
# source .venv/bin/activate
# python -m pip install numpy
# ```

# %% [markdown]
# ## Drop-in replacement for `venv`
#
# ~~python -m venv .venv~~
#
# - Create a virtual environment at `.venv`
# ```shell
# uv venv
# ```
#
# ::: {.callout-note}
# Create a virtual environment at `/path/to/venv/`
# ```shell
# uv venv /path/to/venv/
# ```
# :::

# %% [markdown]
# ## Drop-in replacement for `pip`
#
# - Install a package in the new virtual environment
# ```
# uv pip install numpy
# ```

# %% [markdown]
# ## Drop-in replacement for common `virtualenv` commands
#
#
# A Python version can be requested, e.g., to create a virtual environment with Python 3.11:
#

# %% [markdown]
#

# %%

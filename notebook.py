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

# %% [markdown]
# ## uv
# An extremely fast Python package and project manager, written in Rust.
#
# ![Introducing uv: 10-100x faster than pip](./assets/uv.png "uv"){ width=50% }

# %% [markdown]
# ## Python package management is a mess
#
# ![](./assets/xkcd_python_environment.png "xkcd Python environment joke"){ width=50% }

# %% [markdown]
# ## Python package management is a mess
#
# ![](./assets/Hamel.png "Python environment"){ width=50% }

# %% [markdown]
# ## There is a risk...
#
# ![](./assets/xkcd_standards.png "xkcd standards joke"){ width=50% }

# %% [markdown]
# ## Rust 🦀 is supercharging Python
#
# - Polars
# - Pydantic
# - Tantivy
# - Qdrant
# - LanceDB
# - Ruff
# - uv
# - ...
#
# ::: aside
# [How Rust 🦀 is supercharging Python from the ground up](https://thedataquarry.com/posts/rust-is-supercharging-python/)
# :::

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
# Following the [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
#
# ::: {.callout-tip}
# It is recommended to use a virtual environment when working with third party packages.
# :::

# %% [markdown]
# ## Common workflow
#
# Following the [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
#
# ```shell
# python -m venv .venv
# source .venv/bin/activate
# python -m pip install numpy
# ```

# %% [markdown]
# ## Common workflow
#
# Following the [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
#
# ```{.shell code-line-numbers="1-1"}
# python -m venv .venv
# source .venv/bin/activate
# python -m pip install numpy
# ```

# %% [markdown]
# ## Drop-in replacement for `venv`
#
# - Create a virtual environment at `.venv`
# ```shell
# uv venv
# ```
#
# ::: aside
# To create a virtual environment at `/path/to/venv/`:
# ```shell
# uv venv /path/to/venv/
# ```
# :::

# %% [markdown]
# ## Common workflow
#
# Following the [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
#
# ```{.shell code-line-numbers="2-2"}
# python -m venv .venv
# source .venv/bin/activate
# python -m pip install numpy
# ```

# %% [markdown]
# ## Drop-in replacement for `venv`
#
# - Activate a virtual environment
# ```{.shell code-line-numbers="2-2"}
# uv venv
# source .venv/bin/activate
# ```

# %% [markdown]
# ## Common workflow
#
# Following the [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
#
# ```{.shell code-line-numbers="3-3"}
# python -m venv .venv
# source .venv/bin/activate
# python -m pip install numpy
# ```

# %% [markdown]
# ## Drop-in replacement for `pip`
#
# - Install a package in the new virtual environment
# ```{.shell code-line-numbers="3-3"}
# uv venv
# source .venv/bin/activate
# uv pip install numpy
# ```

# %% [markdown]
# ## Drop-in replacement for `virtualenv`
#
#
# - Create a virtual environment with, e.g., Python 3.11:
# ```shell
# uv venv --python 3.11
# ```

# %% [markdown]
# ## Drop-in replacement for `pip-tools`
#
# - Given a `requirements.in`
# ```shell
# uv pip compile requirements.in > requirements.txt
# ```
# - Given a `requirements.txt`
# ```shell
# uv pip sync requirements.txt
# ```

# %% [markdown]
#

# %%

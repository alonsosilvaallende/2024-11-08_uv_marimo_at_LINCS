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
# ## 
#
# > "We shape our tools and thereafter **our tools shape us**."
# >
# > --*Marshall McLuhan*

# %% [markdown]
# ##
#
# ::: {.callout-note appearance="simple"}
# Most of this reflection is coming from Trevor Manz in
# [juv: Reproducible Jupyter Notebooks](https://github.com/manzt/juv)
# :::

# %% [markdown]
# ##
#
# ![I must admit it: [I like notebooks](https://www.youtube.com/watch?v=9Q6sLbz37gk)](./assets/I_like_notebooks.png "uv"){ width=50% }

# %% [markdown]
# ##
#
# ![Notebooks do have [reproducibility problems](https://leomurta.github.io/papers/pimentel2019a.pdf)](./assets/Reproducibility.png "uv"){ width=50% }

# %% [markdown]
# ## Reproducibility of Jupyter Notebooks
#
# - 1.16M notebooks
# - Most repositories don't declare their dependencies
# - Those that do don't declare all of them
# - Able to execute: 24%
# - Able to produce same results: 4%

# %% [markdown]
# ##
# In [Falling Into The Pit of Success](https://blog.codinghorror.com/falling-into-the-pit-of-success/), Jeff Atwood quotes:
#
# > "I often think of C++ as my own personal Pit of Despair Programming Language. Unmanaged C++ makes it so easy to fall into traps. Think buffer overruns, memory leaks, double frees, mismatch between allocator and deallocator, using freed memory, umpteen dozen ways to trash the stack or heap – and those are just some of the memory issues. There are lots more 'gotchas' in C++. C++ often throws you into the Pit of Despair and you have to climb your way up the Hill of Quality."
# >
# > --*Eric Lippert*

# %% [markdown]
# ##
#  - Wouldn't it be nice to use a tool designed to keep you from falling into *The Pit of Despair*?
#  - Wouldn't it be even better if you used a tool that let you effortlessly fall into *The Pit of Success*?
#  - We want users to simply fall into winning practices by using our tools. To the extent that we make it easy to get into trouble we fail.

# %% [markdown]
# ## 
#
# > "A well-designed system makes it **easy to do the right things** and annoying (but not impossible) to do the wrong things."
# > 
# > --*Jeff Atwood*

# %% [markdown]
# ##
#
# ![GitHub blog: AI leads Python to top language](./assets/GitHub-Octoverse-2024-top-programming-languages.webp "uv"){ width=50% }

# %% [markdown]
# ##
#
# ![GitHub blog: AI leads Python to top language](./assets/GitHub-Octoverse-2024-jupyter-notebooks-usage.webp "uv"){ width=50% }

# %% [markdown]
# ## Rethinking the *getting started*
# ---
# code-annotations: select
# ---
#
# ```python
# python -m venv venv # <1>
# source venv/bin/activate # <2>
# python -m pip install -r requirements.txt # or just pip install numpy pandas.. # <3>
# jupyter lab notebook.ipynb # <4>
# ```
# 1. Which python?
# 2. What happens if you forget to activate it?
# 3. Which versions of the packages? Which versions of their dependencies?
# 4. Which jupyterlab? In which order of the cells?

# %% [markdown]
# ## The Gold Standard of the *getting started* is a *single command* (no furthur guidance required)
#
# ```python
# <magic tool> notebook.ipynb
# ```

# %% [markdown]
# ## The Gold Standard of the *getting started* is a *single command* (no furthur guidance required)
#
# ```python
# <magic tool> notebook.ipynb
# ```
#
# ### uv + marimo help us do a huge jump towards that goal.

# %% [markdown]
# # uv: An extremely fast Python package and project manager

# %% [markdown]
# ## uv
# An extremely fast Python package and project manager, written in Rust.
#
# ![Introducing uv: 10-100x faster than pip](./assets/uv.png "uv"){ width=50% }

# %% [markdown]
# ## uv
#
# - Announced in February 15, 2024
# - Stars in GitHub: 25.4k
# - Downloads per month: 28.1M (October 2024)
# - PyPI share: 13.3% (October 2024)

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
# [How Rust 🦀 is supercharging Python from the ground up](https://thedataquarry.com/posts/rust-is-supercharging-python/) by Prashanth Rao
# :::

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
# ## Why is it a difficult problem?
#
# - No multi-version support -> SAT problem -> NP-hard -> CDCL-based SAT solver
# - Rich syntax for filtering requirements by platform -> SAT problem -> NP-hard -> Algebraic decision diagrams
#
# ::: aside
# [uv: An Extremely Fast Python Package Manager](https://www.youtube.com/watch?v=gSKTfG1GXYQ) by Charlie Marsh
# :::

# %% [markdown]
# ## Installation
#
# - Standalone installer
# ```shell
# curl -LsSf https://astral.sh/uv/install.sh | sh
# ```
#
# - PyPI
# ```shell
# pip install uv
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
# python -m pip install numpy pandas
# ```

# %% [markdown]
# ## Common workflow
#
# Following the [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
#
# ```{.shell code-line-numbers="1-1"}
# python -m venv .venv
# source .venv/bin/activate
# python -m pip install numpy pandas
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
# python -m pip install numpy pandas
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
# python -m pip install numpy pandas
# ```

# %% [markdown]
# ## Drop-in replacement for `pip`
#
# - Install a package in the new virtual environment
# ```{.shell code-line-numbers="3-3"}
# uv venv
# source .venv/bin/activate
# uv pip install numpy pandas
# ```

# %% [markdown]
# ## Workflow
# :::: {.columns}
#
# ::: {.column width="55%"}
# ```{.bash filename="Terminal"}
# python -m venv .venv
# source .venv/bin/activate
# python -m pip install numpy pandas
# ```
# :::
#
# ::: {.column width="45%"}
# ```{.bash filename="Terminal"}
# uv venv
# source .venv/bin/activate
# uv pip install numpy pandas
# ```
# :::
#
# ::::

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
# ## Drop-in replacement for `poetry`
#
# - Initialize a project
# ```
# mkdir hello-world
# cd hello-world
# uv init
# uv run hello.py
# ```
# - Add dependencies
# ```
# uv add numpy polars
# ```
# - Build distributions
# ```
# uv build
# ```
# - Publish a package
# ```
# uv publish
# ```

# %% [markdown]
# ## Running scripts with no dependencies
#
# ```{.python filename="example.py"}
# print("Hello World")
# ```
#
# ```{.bash filename="Terminal"}
# uv run example.py
# # Hello World
# ```

# %% [markdown]
# ## Running scripts with dependencies
#
# ```{.python filename="example.py"}
# import time
# from tqdm import tqdm
# from rich import print
#
# for i in tqdm(range(10)):
#     time.sleep(.1)
# print("hi :vampire:")
# ```
#
# ```{.bash filename="Terminal"}
# uv run --with tqdm --with rich example.py
# ```

# %% [markdown]
# ## Creating scripts with inline script metadata PEP 732
#
# ```{.bash filename="Terminal"}
# uv init --script example.py --python 3.12
# ```
#
# ```{.bash filename="Terminal"}
# uv add --script example.py 'tqdm' 'rich'
# ```
#
# ```{.bash filename="Terminal"}
# uv run example.py
# ```

# %% [markdown]
# ## Improving reproducibility
#
# ```{.python filename="example.py"}
# # /// script
# # dependencies = [
# #   "numpy",
# # ]
# # [tool.uv]
# # exclude-newer = "2024-11-07T00:00:00Z"
# # ///
#
# import numpy
#
# print(numpy.__version__)
# ```
#
# ```{.bash filename="Terminal"}
# #!/usr/bin/env -S uv run
# ```

# %% [markdown]
# ## Using tools
#
# ```{.bash filename="Terminal"}
# uvx ruff check example.py
# ```

# %% [markdown]
# # marimo: Rethinking the notebook to create reproducible notebooks

# %% [markdown]
# ## Getting started
#
# To install:
# ```{.bash filename="Terminal"}
# uv pip install marimo
# ```
#
# To start a marimo notebook:
# ```{.bash filename="Terminal"}
# marimo edit notebook.py
# ```
#
# To start a marimo tutorial:
# ```{.bash filename="Terminal"}
# marimo tutorial intro
# # marimo tutorial --help
# ```

# %% [markdown]
# ## Marimo notebooks are reactive {auto-animate=true}
#
# cell 1:
# ```python
# x = 1
# ```
#
# cell 2:
# ```python
# y = 1
# print(x + y)
# ```
#
# ## Marimo notebooks are reactive {auto-animate=true}
#
# cell 1:
# ```python
# x = 2
# ```
#
# cell 2:
# ```python
# y = 1
# print(x + y)
# ```

# %% [markdown]
# ## Marimo notebooks are executable as a script {auto-animate=true}
#
# ```{.python filename="Marimo notebook"}
# name = "World"
# print(f"Hello {name}!")
# ```
#
# ```{.bash filename="Terminal"}
# python notebook.py
# ```
#
# ## Marimo notebooks are executable as a script {auto-animate=true}
#
# ```{.python filename="Marimo notebook"}
# import marimo as mo
#
# name = mo.cli_args().get("name") or ""
# print(f"Hello {name}!")
# ```
#
# ```{.bash filename="Terminal"}
# python notebook.py --name="LINCS"
# ```

# %% [markdown]
# ## Marimo notebooks are git-friendly {auto-animate=true}
#
# ```python
# import numpy as np
# import matplotlib.pyplot as plt
#
# def plot(α):
#     fig = plt.figure(figsize=(4, 5))
#     xlim, ylim = [-np.pi, np.pi], [0, 10]
#     x = np.linspace(*xlim)
#     plt.plot(x, np.exp(x * α), label=r'$e^{\alpha x}$')
#     plt.xlabel('$x$')
#     plt.xlim(xlim)
#     plt.ylim(ylim)
#     plt.legend()
#     plt.show()
#
# α = 1
# plot(α)
# ```
#
# ## Marimo notebooks are git-friendly {auto-animate=true}
#
# ```python
# import numpy as np
# import matplotlib.pyplot as plt
#
# def plot(α):
#     fig = plt.figure(figsize=(4, 5))
#     xlim, ylim = [-np.pi, np.pi], [0, 10]
#     x = np.linspace(*xlim)
#     plt.plot(x, np.exp(x * α), label=r'$e^{\alpha x}$')
#     plt.xlabel('$x$')
#     plt.xlim(xlim)
#     plt.ylim(ylim)
#     plt.legend()
#     plt.show()
#
# α = 2
# plot(α)
# ```

# %% [markdown]
# ## Jupyter notebooks can be git-friendly but require more effort
#
# - [Jupytext](https://jupytext.readthedocs.io/en/latest/)
# - [nbdime](https://nbdime.readthedocs.io/en/latest/)

# %% [markdown]
# ## Reactive UI
#
# ```python
# import marimo as mo
#
# text = mo.ui.text("Hello")
# text
# ```
# ```python
# print(f"You entered: {text.value}")
# ```
#
# ```python
# number = mo.ui.number(0,1,.1)
# number
# ```
#
# ```python
# number = mo.ui.slider(0,1,.1)
# ```
#

# %% [markdown]
# ## Persistent cache
#
# ```python
# import time
#
# def my_expensive_function(number):
#     time.sleep(9)
#     return 42
#
# import marimo as mo
#
# with mo.persistent_cache(name="my_cache"):
#     x = my_expensive_function(10)
# ```

# %% [markdown]
# ## WebAssembly

# %% [markdown]
# - Deploy a marimo app as a stand-alone web application that fully runs in the frontend.
# - This website will then run your code in the browser via webassembly with [pyodide](https://pyodide.org/).
# - To start: [https://marimo.new/](https://marimo.new/)
# - Example: [Understanding tokenizers](https://marimo.app/?mode=read&include-code=false&slug=tj45k0)

# %% [markdown]
# ## Deployment in HuggingFace spaces
#
# [Chat is an abstraction](https://huggingface.co/spaces/alonsosilva/apply_chat_template)

# %% [markdown]
# ## Reproducible notebooks
#
# ```{.bash filename="Terminal"}
# uvx marimo edit --sandbox notebook.py
# ```

# %% [markdown]
# # Conclusions

# %% [markdown]
# - uv is an extremely fast Python package and project management
# - marimo is a reactive notebook with many nice features
# - Both of this tools help us drive towards more reproducible programs

# %% [markdown]
# ## References
#
# - [JUV: Reproducible Jupyter Notebooks](https://github.com/manzt/juv)

# %% [markdown]
# ## Asides
# - [uvtrick](https://simonwillison.net/2024/Sep/1/)
# - [sudoku](https://simonwillison.net/2024/Oct/21/)

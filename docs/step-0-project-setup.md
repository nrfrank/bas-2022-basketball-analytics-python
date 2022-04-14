# Step 0 - Project Setup

---

## Overview

When starting a new analysis it can be helpful to work from a consistent project template. This can make getting started
quicker and easier while also helping to ensure best practices and code quality. Absent a template of your own, which
you may arrive at over time, good starting point is the 
[Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) project template.

In this first step we set up a basic project structure using the Cookiecutter Data Science template. We then pare that 
down a bit and update the format of the README file using a format inspired by the 
[Amazing GitHub Template](https://github.com/dec0dOS/amazing-github-template). Finally, we update the setup script,
create a Python environment, and generate a [jupyter](https://jupyter.org/) notebook kernel for our work.

## Setup

Pull the project state relevant to this step by running

```copy
git checkout feature/stop-0-project-setup
```

## Walkthrough

### Create project skeleton
We can use the Cookiecutter Data Science template as follows:
1. Activate your virtual environment

```copy
conda activate basketball-analytics-summit
```

2. Install the `cookiecutter` Python package

```copy
python -m pip install cookiecutter
```

3. Run the `cookiecutter` command and follow the prompts

```copy
cookiecutter https://github.com/drivendata/cookiecutter-data-science
```

### Customize project

For our purposes, we do not need everything included in the Cookiecutter Data Science project template. In commit 
[3482519](https://github.com/nrfrank/bas-2022-basketball-analytics-python/commit/3482519b7359f2d352cb0eeb0d0ce558cbe99a4c)
we remove a number of files that are not relevant in the context of this tutorial.

### Create Python package

In commit [8bda23c](https://github.com/nrfrank/bas-2022-basketball-analytics-python/commit/8bda23c6ded4353b4767bbd46c487c7ac6520553)
we rename the package to something project specific and add some basic requirements to the `setup.py`.

### Define Jupyter kernel

Finally, in [d66c373](https://github.com/nrfrank/bas-2022-basketball-analytics-python/commit/d66c373adde0644f0a051acae68fc55bc6ef5568)
we document the steps to create a custom Jupyter kernel and add the necessary requirements to the `setup.py`.

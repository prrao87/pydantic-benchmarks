# Pydantic v2: Obtain a 5x speedup over v1

This repo contains code to reproduce the benchmark from a [blog post](https://thedataquarry.com/posts/why-pydantic-v2-matters/) showcasing a 5x performance improvement of Pydantic v2 over v1 (thanks to Rust 🦀). Read the blog post linked for more details!

## Setup

Note that this code base has been tested in Python 3.11, and requires a minimum of Python 3.10 to work. To run the benchmark for v1 and v2, we need two separate virtual environments.

First, set up the virtual environment for v1.

```sh
cd v1
python -m venv v1  # python -> python 3.10+
source v1/bin/activate
# Install dependencies
pip install -r requirements.txt
```

Next, set up the virtual environment for v2.

```sh
cd ../v2
python -m venv v2  # python -> python 3.10+
source v2/bin/activate
# Install dependencies
pip install -r requirements.txt
```

Next, navigate to the `v1/` and `v2/` directories to run each benchmark.
# Pydantic benchmarks

Benchmark performance and explore the new features of various releases of Pydantic.

The benchmarks and their implications are explored in more detail in the following blog posts: 

* The [first](https://thedataquarry.com/posts/why-pydantic-v2-matters/) blog post showed how simply changing a few lines of code from the v1 API to v2, yielded a **5x** speedup, thanks to the underlying [`pydantic-core`](https://github.com/pydantic/pydantic-core) being rewritten in Rust 🦀 💪🏽

* The [second](https://thedataquarry.com/posts/intermediate-pydantic/) blog post shows that, with the right knowledge of Pydantic v2's new features, it's possible to get **12x** performance improvement over v1. Additionally, each successive major release of Pydantic v2 has shown incremental improvements in performance, thanks to underlying optimizations and innovations at the Rust level. More such improvements to come in future versions!

## Setup

This code base has been tested in Python 3.11. It's recommended to set up a clean virtual environment to run the benchmarks.

```sh
python -m venv venv  # python -> python 3.11+
source venv/bin/activate
# Install dependencies
pip install -r requirements.txt
```

Install any subsequent versions of Pydantic as required by specifying their major and minor version numbers to benchmark each of them.

```sh
# pip install pydantic==2.0.3
# pip install pydantic==2.1.1
# pip install pydantic==2.2.1
# pip install pydantic==2.3.0
# pip install pydantic==2.4.2
pip install pydantic==2.5.2
```

Then, navigate to the respective directories `v1` and `v2` to run the benchmark for each version of Pydantic.

## Dataset

The dataset used for this benchmark is the [Wine Reviews](https://www.kaggle.com/zynicide/wine-reviews) dataset from Kaggle, containing ~130k reviews on wines along with other metadata. For convenience and ease of reproduction, the dataset is made available here as line-delimited JSON in the `data` directory.

## Benchmark results

The benchmark was run using `pytest-benchmark`. See the respective version directories for steps to reproduce the benchmark results.

> [!NOTE]
> * The timing numbers below are from a 2022 M2 Macbook Pro with 16GB RAM
> * The times reported are an average over 10 runs

### Basic validator

The basic validator's [schema](./v2/schemas.py) makes use of simple Pydantic models, with very minor changes between v1 and v2.

Version | Run time (sec) | Speedup factor over v1
---: | ---: | ---:
`1.10.13` | 3.262 | 1.0
`2.0.3` | 0.679 | 4.8
`2.1.1` | 0.679 | 4.8
`2.2.1` | 0.624 | 5.2
`2.3.0` | 0.651 | 5.0
`2.4.2` | 0.641 | 5.1
`2.5.2` | 0.626 | 5.2

### Improved validator

The improved validator's [schema](./v2/schemas_improved.py) makes use of intermediate concepts in Pydantic, using some of the new features available in v2. It produces results that are identical to the basic validator. Note that in this case, we cannot test v1 because the features used are available only in v2.

Version | Run time (sec) | Speedup factor over v1
---: | ---: | ---:
`2.0.3` | 0.314 | 10.4
`2.1.1` | 0.317 | 10.3
`2.2.1` | 0.305 | 10.7
`2.3.0` | 0.307 | 10.6
`2.4.2` | 0.291 | 11.2
`2.5.2` | 0.273 | 11.9

> [!Tip]
> With the right knowledge of Pydantic v2 features, it's possible to optimize and tune every workflow to get the most out of your validation workflows. This is due to underlying improvements to `pydantic-core` and `PyO3` at the Rust level, that have been having a noticeable impact at the Python level.

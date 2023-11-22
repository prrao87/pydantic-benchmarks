# Pydantic benchmarks

Benchmark performance and explore the new features of various releases of Pydantic.

The first [blog post](https://thedataquarry.com/posts/why-pydantic-v2-matters/) in this series showed how simply changing a few lines of code from the v1 logic to conform to the v2 API, yielded a **5x** performance improvement (thanks to the underlying [`pydantic-core`](https://github.com/pydantic/pydantic-core) being rewritten in Rust 🦀 💪🏽). 

With the right knowledge of Pydantic v2's new features, it's possible to get more than a **10x** performance improvement! This will be discussed in more detail in the second (upcoming) blog post.

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

## Results

The run times reported are for each validation over all 130k records of wine review data (JSON), reported as the average over 10 runs, amounting to ~1.3 million validations per version benchmarked.

### Basic validator

The basic validator makes use of simple Pydantic models, with very minor changes between v1 and v2.

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

The improved validator makes use of intermediate concepts in Pydantic, using some of the new features available in v2, and produces results that are identical to the basic validator. Note that in this case, we cannot test v1 because the features used are available only in v2.

Version | Run time (sec) | Speedup factor over v1
---: | ---: | ---:
`2.0.3` | 0.314 | 10.4
`2.1.1` | 0.317 | 10.3
`2.2.1` | 0.305 | 10.7
`2.3.0` | 0.307 | 10.6
`2.4.2` | 0.291 | 11.2
`2.5.2` | 0.273 | 11.9

It's clear that the underlying improvements to `pydantic-core` and `PyO3` at the Rust level have been having an ever-increasing impact at the Python level (as seen in the incremental improvement with each major release). With the right knowledge of Pydantic v2 features, it's possible to get blazing fast performance compared to v1. 🚀

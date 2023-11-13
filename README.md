# Pydantic benchmarks

Code to benchmark the performance of newer versions of Pydantic.

The first [blog post](https://thedataquarry.com/posts/why-pydantic-v2-matters/) in this series showcased how simply changing a few lines of code from the v1 logic over to align with the v2 API, yielded a **5x** performance improvement (thanks to the underlying [`pydantic-core`](https://github.com/pydantic/pydantic-core) being written in Rust 🦀 💪🏽). However, with a little more advanced knowledge of Pydantic's new features available in v2.x, it's possible to get more than 10x performance improvement! This will be discussed in more detail in the second blog post in this series.

## Setup

Note that this code base has been tested in Python 3.11.

It's recommended to set up a clean virtual environment for each version of Pydantic being tested.

```sh
cd v1_10
python -m venv venv1  # python -> python 3.11+
source venv1/bin/activate
# Install dependencies
pip install -r requirements.txt
```

Set up virtual environments for each subsequent directory (`v2_0`, `v2_4`, etc.) in the same way.

Then, navigate to the respective directories to run the benchmark for each version of Pydantic.

## Dataset

The dataset used for this demo is the [Wine Reviews](https://www.kaggle.com/zynicide/wine-reviews) dataset from Kaggle, containing ~130k reviews on wines along with other metadata. The dataset is converted to a ZIP archive, and the code for this as well as the ZIP data is provided here for reference.

## Results

The run times reported are for each validation over all 130k records of wine review data (JSON), reported as the average over 10 runs, amounting to ~1.3 million validations in total.

Pydantic version | Case | Run time (sec) | Speedup factor over v1
:---: | :---: | ---: | ---:
1.10 | Basic validator | 3.249 | 1.0
2.0 | Basic validator | 0.620 | 5.2
2.4 | Basic validator | 0.594 | 5.5
2.5 | Basic validator | 0.551 | 5.9
2.0 | Optimized validator | 0.329 | 9.9
2.4 | Optimized validator | 0.313 | 10.4
2.5 | Optimized validator | 0.286 | 11.4

A large fraction of the performance improvements in v2 came from the Rust layer, with a portion of it coming from Profile Guided Optimization (PGO) of `pydantic-code` compilation in v2.4 and above, see [this comment](https://github.com/prrao87/pydantic-v2-test-drive/pull/1#issuecomment-1617746688) and the linked GitHub PR for more details.

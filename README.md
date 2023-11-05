# Pydantic benchmarks

Code to benchmark the performance of Pydantic v2.x vs. v1.x.

The first [blog post](https://thedataquarry.com/posts/why-pydantic-v2-matters/) in this series showcased a 5x-10x performance improvement of Pydantic v2.x over v1.x (thanks to Rust 🦀). Simply changing a few lines of code from the v1 logic over to align with the v2 API yielded a **5x** performance improvement. WHowever, with a little more advanced knowledge of Pydantic and the tools available in v2.x, it's possible to get more than 10x performance improvement!

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
2.0 | Optimized validator | 0.329 | 9.9
2.4 | Basic validator | 0.594 | 5.5
2.4 | Optimized validator | 0.313 | 10.4

The performance improvements in v2 came from the Rust layer, with additional improvements coming from Profile Guided Optimization (PGO) of `pydantic-code` compilation in v2.4, see [this comment](https://github.com/prrao87/pydantic-v2-test-drive/pull/1#issuecomment-1617746688) and the linked GitHub PR for more details.
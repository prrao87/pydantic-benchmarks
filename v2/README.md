# Run benchmarks for v2.x

Activate the virtual environment that has the required version of Pydantic v2 installed. Then, run the benchmark as follows.

> [!NOTE]
> * 10 runs in total, 5 warmup runs, with the mean being reported as the average over 10 runs
> * The timing numbers shown are from an M2 Macbook Pro. Depending on your CPU, your mileage may vary

## 💡 What is the difference between the original and improved versions?

Per Samuel Colvin's feedback in [#1](https://github.com/prrao87/pydantic-v2-test-drive/pull/1), the improved validator modifies the `Wine` schema to subclass `TypedDict` instead of `BaseModel`, since in this case we're not actually using the Pydantic model, but use it as a Python dict downstream. With `TypedDict`, the excluding of `None` values can be done *during* validation, so for simple validations when we need a Python dict downstream, there's need for us to serialize the model to a Pydantic model and back to a Python dict.

See the `schemas_improved.py` for details.

### Caveats with improved version

* The `schemas_improved.py` is a little more verbose and not as readable as the original
* `TypedDict` doesn't allow methods to be defined under it (per PEP 589), and so the improved code which defines a validator under the `Wine` model that subclasses `TypedDict` will violate type checkers like `mypy` and `Pyright`.
  * Disabling the type checker via `# type: ignore` can help with passing type checker tests; however, this is a workaround and deviated from the original intended use of `TypedDict`
  * [See the discussion](https://github.com/pydantic/pydantic/discussions/6517) on the intention of Pydantic's maintainers to allow subclassing `TypedDict` for Pydantic use cases, even though it doesn't respect PEP 589.


## v2.0.3

```sh
$ pytest benchmark_validator.py --benchmark-sort=fullname --benchmark-warmup-iterations=5 --benchmark-min-rounds=10
========================================================================================================= test session starts =========================================================================================================
platform darwin -- Python 3.11.6, pytest-7.4.3, pluggy-1.3.0
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=10 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=5)
rootdir: /code/pydantic-benchmarks/v2
plugins: benchmark-4.0.0
collected 2 items                                                                                                                                                                                                                     

benchmark_validator.py ..                                                                                                                                                                                                       [100%]


-------------------------------------------------------------------------------------- benchmark: 2 tests --------------------------------------------------------------------------------------
Name (time in ms)                Min                 Max                Mean             StdDev              Median                IQR            Outliers     OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_validate               660.0767 (2.13)     712.5703 (2.21)     679.0992 (2.16)     15.7909 (4.07)     675.2681 (2.15)     18.3381 (5.35)          3;0  1.4725 (0.46)         10           1
test_validate_improved     309.8981 (1.0)      321.8660 (1.0)      314.0435 (1.0)       3.8809 (1.0)      313.6297 (1.0)       3.4279 (1.0)           4;1  3.1843 (1.0)          10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
========================================================================================================= 2 passed in 14.02s ==========================================================================================================
```

## v2.1.1

```sh
$ pytest benchmark_validator.py --benchmark-sort=fullname --benchmark-warmup-iterations=5 --benchmark-min-rounds=10
========================================================================================================= test session starts =========================================================================================================
platform darwin -- Python 3.11.6, pytest-7.4.3, pluggy-1.3.0
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=10 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=5)
rootdir: /code/pydantic-benchmarks/v2
plugins: benchmark-4.0.0
collected 2 items                                                                                                                                                                                                                     

benchmark_validator.py ..                                                                                                                                                                                                       [100%]


-------------------------------------------------------------------------------------- benchmark: 2 tests --------------------------------------------------------------------------------------
Name (time in ms)                Min                 Max                Mean             StdDev              Median                IQR            Outliers     OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_validate               662.8993 (2.14)     716.6063 (2.18)     679.1859 (2.14)     15.7958 (2.82)     677.6732 (2.14)     18.7485 (2.33)          2;1  1.4724 (0.47)         10           1
test_validate_improved     309.6179 (1.0)      328.0040 (1.0)      317.2860 (1.0)       5.5997 (1.0)      316.5052 (1.0)       8.0387 (1.0)           3;0  3.1517 (1.0)          10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
========================================================================================================= 2 passed in 14.01s ==========================================================================================================
```

## v2.2.1

```sh
$ pytest benchmark_validator.py --benchmark-sort=fullname --benchmark-warmup-iterations=5 --benchmark-min-rounds=10
========================================================================================================= test session starts =========================================================================================================
platform darwin -- Python 3.11.6, pytest-7.4.3, pluggy-1.3.0
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=10 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=5)
rootdir: /code/pydantic-benchmarks/v2
plugins: benchmark-4.0.0
collected 2 items                                                                                                                                                                                                                     

benchmark_validator.py ..                                                                                                                                                                                                       [100%]


-------------------------------------------------------------------------------------- benchmark: 2 tests -------------------------------------------------------------------------------------
Name (time in ms)                Min                 Max                Mean            StdDev              Median                IQR            Outliers     OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_validate               616.9860 (2.04)     636.5859 (2.06)     624.9668 (2.05)     7.8224 (3.82)     621.6646 (2.04)     16.0208 (18.86)         4;0  1.6001 (0.49)         10           1
test_validate_improved     302.5146 (1.0)      309.4921 (1.0)      305.0599 (1.0)      2.0500 (1.0)      304.7845 (1.0)       0.8495 (1.0)           4;4  3.2780 (1.0)          10           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
========================================================================================================= 2 passed in 13.27s ==========================================================================================================
```

## v2.3.0

```sh
$ pytest benchmark_validator.py --benchmark-sort=fullname --benchmark-warmup-iterations=5 --benchmark-min-rounds=10
========================================================================================================= test session starts =========================================================================================================
platform darwin -- Python 3.11.6, pytest-7.4.3, pluggy-1.3.0
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=10 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=5)
rootdir: /code/pydantic-benchmarks/v2
plugins: benchmark-4.0.0
collected 2 items                                                                                                                                                                                                                     

benchmark_validator.py ..                                                                                                                                                                                                       [100%]


------------------------------------------------------------------------------------- benchmark: 2 tests -------------------------------------------------------------------------------------
Name (time in ms)                Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_validate               635.5941 (2.10)     651.1366 (2.05)     641.1307 (2.08)     4.6512 (1.0)      640.5380 (2.09)     4.5161 (1.01)          3;1  1.5597 (0.48)         10           1
test_validate_improved     302.7391 (1.0)      317.0747 (1.0)      307.7056 (1.0)      4.7371 (1.02)     305.7871 (1.0)      4.4630 (1.0)           3;1  3.2499 (1.0)          10           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
========================================================================================================= 2 passed in 13.41s ==========================================================================================================
```

## v2.4.2

```sh
$ pytest benchmark_validator.py --benchmark-sort=fullname --benchmark-warmup-iterations=5 --benchmark-min-rounds=10
========================================================================================================= test session starts =========================================================================================================
platform darwin -- Python 3.11.6, pytest-7.4.3, pluggy-1.3.0
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=10 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=5)
rootdir: /code/pydantic-benchmarks/v2
plugins: benchmark-4.0.0
collected 2 items                                                                                                                                                                                                                     

benchmark_validator.py ..                                                                                                                                                                                                       [100%]


-------------------------------------------------------------------------------------- benchmark: 2 tests --------------------------------------------------------------------------------------
Name (time in ms)                Min                 Max                Mean             StdDev              Median                IQR            Outliers     OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_validate               632.0109 (2.19)     666.0196 (2.23)     641.7390 (2.20)     10.0093 (2.93)     637.0314 (2.19)     10.2967 (2.73)          1;1  1.5583 (0.45)         10           1
test_validate_improved     288.7004 (1.0)      298.5473 (1.0)      291.9331 (1.0)       3.4180 (1.0)      290.2840 (1.0)       3.7650 (1.0)           2;0  3.4254 (1.0)          10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
========================================================================================================= 2 passed in 13.21s ==========================================================================================================
```

## v2.5.2

```sh
$ pytest benchmark_validator.py --benchmark-sort=fullname --benchmark-warmup-iterations=5 --benchmark-min-rounds=10
========================================================================================================= test session starts =========================================================================================================
platform darwin -- Python 3.11.6, pytest-7.4.3, pluggy-1.3.0
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=10 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=5)
rootdir: /code/pydantic-benchmarks/v2
plugins: benchmark-4.0.0
collected 2 items                                                                                                                                                                                                                     

benchmark_validator.py ..                                                                                                                                                                                                       [100%]


-------------------------------------------------------------------------------------- benchmark: 2 tests --------------------------------------------------------------------------------------
Name (time in ms)                Min                 Max                Mean             StdDev              Median                IQR            Outliers     OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_validate               582.0348 (2.16)     772.4261 (2.77)     626.4144 (2.29)     58.8587 (19.44)    605.2190 (2.21)     41.6037 (9.17)          1;1  1.5964 (0.44)         10           1
test_validate_improved     270.0660 (1.0)      278.7582 (1.0)      273.7884 (1.0)       3.0280 (1.0)      273.6671 (1.0)       4.5390 (1.0)           4;0  3.6525 (1.0)          10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
========================================================================================================= 2 passed in 12.75s ==========================================================================================================
```

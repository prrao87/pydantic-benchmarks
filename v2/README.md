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
=================================================================================================== test session starts ====================================================================================================
platform darwin -- Python 3.11.7, pytest-7.4.4, pluggy-1.4.0
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=10 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=5)
rootdir: /Users/prrao/code/pydantic-benchmarks/v2
plugins: benchmark-4.0.0
collected 2 items                                                                                                                                                                                                          

benchmark_validator.py ..                                                                                                                                                                                            [100%]


------------------------------------------------------------------------------------- benchmark: 2 tests ------------------------------------------------------------------------------------
Name (time in ms)               Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_validate              561.4500 (2.30)     583.3301 (2.28)     566.5740 (2.27)     6.3012 (1.72)     565.2348 (2.26)     4.7669 (1.0)           1;1  1.7650 (0.44)         10           1
test_validate_improved     244.2450 (1.0)      256.1837 (1.0)      249.1313 (1.0)      3.6555 (1.0)      249.6172 (1.0)      5.3401 (1.12)          3;0  4.0139 (1.0)          10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
==================================================================================================== 2 passed in 11.85s ====================================================================================================
```

## v2.1.1

```sh
$ pytest benchmark_validator.py --benchmark-sort=fullname --benchmark-warmup-iterations=5 --benchmark-min-rounds=10
=================================================================================================== test session starts ====================================================================================================
platform darwin -- Python 3.11.7, pytest-7.4.4, pluggy-1.4.0
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=10 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=5)
rootdir: /Users/prrao/code/pydantic-benchmarks/v2
plugins: benchmark-4.0.0
collected 2 items                                                                                                                                                                                                          

benchmark_validator.py ..                                                                                                                                                                                            [100%]


------------------------------------------------------------------------------------- benchmark: 2 tests ------------------------------------------------------------------------------------
Name (time in ms)               Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_validate              591.5445 (2.39)     602.5615 (2.28)     595.3261 (2.35)     3.9631 (1.0)      594.1549 (2.35)     4.1485 (1.0)           2;0  1.6798 (0.43)         10           1
test_validate_improved     247.9506 (1.0)      264.3129 (1.0)      253.5298 (1.0)      4.5523 (1.15)     252.3699 (1.0)      4.3905 (1.06)          2;1  3.9443 (1.0)          10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
==================================================================================================== 2 passed in 12.21s ====================================================================================================
```

## v2.2.1

```sh
$ pytest benchmark_validator.py --benchmark-sort=fullname --benchmark-warmup-iterations=5 --benchmark-min-rounds=10                                                                           v2.6.0b1 ✱
=================================================================================================== test session starts ====================================================================================================
platform darwin -- Python 3.11.7, pytest-7.4.4, pluggy-1.4.0
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=10 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=5)
rootdir: /Users/prrao/code/pydantic-benchmarks/v2
plugins: benchmark-4.0.0
collected 2 items                                                                                                                                                                                                          

benchmark_validator.py ..                                                                                                                                                                                            [100%]


------------------------------------------------------------------------------------- benchmark: 2 tests ------------------------------------------------------------------------------------
Name (time in ms)               Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_validate              554.1266 (2.25)     574.5667 (2.18)     563.4871 (2.23)     5.6472 (1.14)     562.9366 (2.23)     4.4296 (1.0)           3;2  1.7747 (0.45)         10           1
test_validate_improved     246.5941 (1.0)      263.7369 (1.0)      252.7393 (1.0)      4.9548 (1.0)      251.9075 (1.0)      6.6780 (1.51)          3;0  3.9566 (1.0)          10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
==================================================================================================== 2 passed in 11.84s ====================================================================================================
```

## v2.3.0

```sh
$ pytest benchmark_validator.py --benchmark-sort=fullname --benchmark-warmup-iterations=5 --benchmark-min-rounds=10
=================================================================================================== test session starts ====================================================================================================
platform darwin -- Python 3.11.7, pytest-7.4.4, pluggy-1.4.0
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=10 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=5)
rootdir: /Users/prrao/code/pydantic-benchmarks/v2
plugins: benchmark-4.0.0
collected 2 items                                                                                                                                                                                                          

benchmark_validator.py ..                                                                                                                                                                                            [100%]


------------------------------------------------------------------------------------- benchmark: 2 tests ------------------------------------------------------------------------------------
Name (time in ms)               Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_validate              552.3091 (2.24)     561.1091 (2.16)     555.8923 (2.22)     2.8890 (1.0)      555.5913 (2.24)     5.3502 (1.20)          2;0  1.7989 (0.45)         10           1
test_validate_improved     246.2660 (1.0)      259.8622 (1.0)      250.0118 (1.0)      5.0420 (1.75)     247.6022 (1.0)      4.4582 (1.0)           2;2  3.9998 (1.0)          10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
==================================================================================================== 2 passed in 11.68s ====================================================================================================
```

## v2.4.2

```sh
$ pytest benchmark_validator.py --benchmark-sort=fullname --benchmark-warmup-iterations=5 --benchmark-min-rounds=10
=================================================================================================== test session starts ====================================================================================================
platform darwin -- Python 3.11.7, pytest-7.4.4, pluggy-1.4.0
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=10 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=5)
rootdir: /Users/prrao/code/pydantic-benchmarks/v2
plugins: benchmark-4.0.0
collected 2 items                                                                                                                                                                                                          

benchmark_validator.py ..                                                                                                                                                                                            [100%]


------------------------------------------------------------------------------------- benchmark: 2 tests ------------------------------------------------------------------------------------
Name (time in ms)               Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_validate              540.7102 (2.33)     552.6634 (2.29)     545.0725 (2.31)     4.1227 (1.28)     544.3835 (2.30)     8.1248 (1.49)          4;0  1.8346 (0.43)         10           1
test_validate_improved     232.0445 (1.0)      241.2557 (1.0)      236.3600 (1.0)      3.2189 (1.0)      236.6698 (1.0)      5.4353 (1.0)           3;0  4.2308 (1.0)          10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
==================================================================================================== 2 passed in 11.39s ====================================================================================================
```

## v2.5.3

```sh
$ pytest benchmark_validator.py --benchmark-sort=fullname --benchmark-warmup-iterations=5 --benchmark-min-rounds=10
=================================================================================================== test session starts ====================================================================================================
platform darwin -- Python 3.11.7, pytest-7.4.4, pluggy-1.4.0
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=10 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=5)
rootdir: /Users/prrao/code/pydantic-benchmarks/v2
plugins: benchmark-4.0.0
collected 2 items                                                                                                                                                                                                          

benchmark_validator.py ..                                                                                                                                                                                            [100%]


------------------------------------------------------------------------------------- benchmark: 2 tests -------------------------------------------------------------------------------------
Name (time in ms)               Min                 Max                Mean            StdDev              Median                IQR            Outliers     OPS            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_validate              499.8814 (2.35)     521.9392 (2.39)     509.9706 (2.35)     7.7924 (3.81)     508.0185 (2.34)     13.8335 (4.38)          3;0  1.9609 (0.42)         10           1
test_validate_improved     213.0340 (1.0)      218.7544 (1.0)      216.6876 (1.0)      2.0435 (1.0)      216.8415 (1.0)       3.1581 (1.0)           3;0  4.6149 (1.0)          10           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
==================================================================================================== 2 passed in 10.75s ====================================================================================================
```

## v2.6.0b1

```sh
$ pytest benchmark_validator.py --benchmark-sort=fullname --benchmark-warmup-iterations=5 --benchmark-min-rounds=10
=================================================================================================== test session starts ====================================================================================================
platform darwin -- Python 3.11.7, pytest-7.4.4, pluggy-1.4.0
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=10 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=5)
rootdir: /Users/prrao/code/pydantic-benchmarks/v2
plugins: benchmark-4.0.0
collected 2 items                                                                                                                                                                                                          

benchmark_validator.py ..                                                                                                                                                                                            [100%]


------------------------------------------------------------------------------------- benchmark: 2 tests ------------------------------------------------------------------------------------
Name (time in ms)               Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_validate              506.3975 (2.36)     516.6887 (2.37)     512.7655 (2.37)     3.2662 (3.30)     512.9130 (2.37)     5.1536 (3.74)          3;0  1.9502 (0.42)         10           1
test_validate_improved     214.8452 (1.0)      217.9454 (1.0)      216.2777 (1.0)      0.9898 (1.0)      216.1906 (1.0)      1.3787 (1.0)           4;0  4.6237 (1.0)          10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
==================================================================================================== 2 passed in 10.77s ====================================================================================================
```
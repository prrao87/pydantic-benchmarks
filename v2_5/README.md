# Run benchmark for v2.4

Activate the virtual environment that has the correct version of Pydantic installed. Then, run the benchmark as follows.

```sh
$ pytest benchmark_validator.py --benchmark-sort=fullname --benchmark-warmup-iterations=5 --benchmark-min-rounds=10
====================================================================================================== test session starts =======================================================================================================
platform darwin -- Python 3.11.6, pytest-7.4.3, pluggy-1.3.0
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=10 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=5)
rootdir: /code/pydantic-benchmarks/v2_5
plugins: benchmark-4.0.0
collected 2 items                                                                                                                                                                                                                

benchmark_validator.py ..                                                                                                                                                                                                  [100%]


-------------------------------------------------------------------------------------- benchmark: 2 tests -------------------------------------------------------------------------------------
Name (time in ms)                Min                 Max                Mean             StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_validate               543.6410 (1.91)     586.5970 (2.03)     550.7491 (1.92)     12.7235 (6.62)     546.8922 (1.92)     1.4635 (1.0)           1;3  1.8157 (0.52)         10           1
test_validate_optimized     284.6320 (1.0)      289.6503 (1.0)      286.1125 (1.0)       1.9225 (1.0)      285.1086 (1.0)      1.4929 (1.02)          2;2  3.4951 (1.0)          10           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
======================================================================================================= 2 passed in 11.96s =======================================================================================================
```

> [!NOTE]
> * 10 runs in total, 5 warmup runs, with the mean being reported as the average over 10 runs
> * The timing numbers shown are from an M2 Macbook Pro. Depending on your CPU, your mileage may vary
> * The basic validator (with serialization/deserialization in Python) takes 0.594 sec per run
> * The optimized validator (without serialization/deserialization in Python) takes 0.313 sec per run


## 💡 What is the optimized version?

Per Samuel Colvin's feedback in [#1](https://github.com/prrao87/pydantic-v2-test-drive/pull/1), the optimized validator modifies the `Wine` schema to subclass `TypedDict` instead of `BaseModel`, since in this case we're not actually using the Pydantic model, but use it as a Python dict downstream. With `TypedDict`, the excluding of `None` values can be done *during* validation, so for simple validations when we need a Python dict downstream, there's need for us to serialize the model to a Pydantic model and back to a Python dict.

See the `schemas_optimized.py` for details.

### Caveats with optimized version

* The `schemas_optimized.py` is a little more verbose and not as readable as the original
* `TypedDict` doesn't allow methods to be defined under it (per PEP 589), and so the optimized code which defines a validator under the `Wine` model that subclasses `TypedDict` will violate type checkers like `mypy` and `Pyright`.
  * Disabling the type checker via `# type: ignore` can help with passing type checker tests; however, this is a workaround and deviated from the original intended use of `TypedDict`
  * [See the discussion](https://github.com/pydantic/pydantic/discussions/6517) on the intention of Pydantic's maintainers to allow subclassing `TypedDict` for Pydantic use cases, even though it doesn't respect PEP 589. In the future, this may change, but for now, the readability of the optimized version is definitely not great compared to the v2 code that directly subcasses `BaseModel`.

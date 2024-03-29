# Run benchmark for v1.x

Activate the virtual environment that has the required version of Pydantic v1 installed. Then, run the benchmark as follows.

> [!NOTE]
> * 10 runs in total, 5 warmup runs, with the mean being reported as the average over 10 runs
> * The timing numbers shown are from an M2 Macbook Pro. Depending on your CPU, your mileage may vary


## v1.10

```sh
$ pytest benchmark_validator.py --benchmark-sort=fullname --benchmark-warmup-iterations=5 --benchmark-min-rounds=10
=================================================================================================== test session starts ====================================================================================================
platform darwin -- Python 3.11.7, pytest-7.4.4, pluggy-1.4.0
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=10 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=5)
rootdir: /Users/prrao/code/pydantic-benchmarks/v1
plugins: benchmark-4.0.0
collected 1 item                                                                                                                                                                                                           

benchmark_validator.py .                                                                                                                                                                                             [100%]


------------------------------------------- benchmark: 1 tests ------------------------------------------
Name (time in s)        Min     Max    Mean  StdDev  Median     IQR  Outliers     OPS  Rounds  Iterations
---------------------------------------------------------------------------------------------------------
test_validate        2.7904  2.8506  2.8286  0.0185  2.8373  0.0257       3;0  0.3535      10           1
---------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
==================================================================================================== 1 passed in 36.23s ====================================================================================================
```

# Run benchmark for v2

Activate the virtual environment that has Pydantic v2 installed. Then, run the validator code as follows.

```sh
$ python validator.py
Validated 129971 records in cycle 1 of 10
Single case: 0.644 sec
Validated 129971 records in cycle 2 of 10
Single case: 0.612 sec
Validated 129971 records in cycle 3 of 10
Single case: 0.614 sec
Validated 129971 records in cycle 4 of 10
Single case: 0.614 sec
Validated 129971 records in cycle 5 of 10
Single case: 0.617 sec
Validated 129971 records in cycle 6 of 10
Single case: 0.619 sec
Validated 129971 records in cycle 7 of 10
Single case: 0.680 sec
Validated 129971 records in cycle 8 of 10
Single case: 0.635 sec
Validated 129971 records in cycle 9 of 10
Single case: 0.625 sec
Validated 129971 records in cycle 10 of 10
Single case: 0.619 sec
All cases: 6.551 sec
```

Running ~1.3 million validations on this sample dataset using Pydantic v2 took ~6.5 sec, which is a ~5x improvement from v1. The timing numbers shown are from an M2 Macbook Pro. Depending on your CPU, your mileage may vary.

## 💡 Update: Optimized v2 version gives a 10x improvement over v1

Per Samuel Colvin's feedback in [#1](https://github.com/prrao87/pydantic-v2-test-drive/pull/1), we can optimize the v2 code by changing the `Wine` schema to inherit from `TypedDict` instead of `BaseModel`, since in this case we're not actually using the Pydantic model, but converting it straight to a dict. With `TypedDict`, the excluding of `None` values can be done during validation, so there's need for us to serialize the model to a dict -- the output of validation to dicts is all we need.

See the `schemas_optimized.py` and `validator_optimized.py` for details.


```sh
$ python validator_optimized.py
Validated 129971 records in cycle 1 of 10
Single case: 0.326 sec
Validated 129971 records in cycle 2 of 10
Single case: 0.313 sec
Validated 129971 records in cycle 3 of 10
Single case: 0.310 sec
Validated 129971 records in cycle 4 of 10
Single case: 0.310 sec
Validated 129971 records in cycle 5 of 10
Single case: 0.315 sec
Validated 129971 records in cycle 6 of 10
Single case: 0.318 sec
Validated 129971 records in cycle 7 of 10
Single case: 0.312 sec
Validated 129971 records in cycle 8 of 10
Single case: 0.310 sec
Validated 129971 records in cycle 9 of 10
Single case: 0.335 sec
Validated 129971 records in cycle 10 of 10
Single case: 0.327 sec
All cases: 3.386 sec
```

With the optimized version, running ~1.3 million validations on this sample dataset using Pydantic v2 took ~3.4 sec, which is almost a 10x improvement from v1! 

### Caveats with optimized version 

* The optimized code is a little more verbose and not as readable (i.e., "simple") as the original
* `TypedDict` doesn't allow methods to be defined in it (per PEP 589), and so the optimized code which defines a validator under the `Wine` model that subclasses `TypedDict` will violate type checkers like `mypy` and `Pyright`.
  * Disabling the type checker via `# type: ignore` can help with passing type checker tests; however, this is a workaround and deviated from the original intended use of `TypedDict`
  * [See the discussion](https://github.com/pydantic/pydantic/discussions/6517) on the intention of Pydantic's maintainers to allow subclassing `TypedDict` for Pydantic use cases, even though it doesn't respect PEP 589. In the future, this may change, but for now, the readability of the optimized version is definitely not great compared to the v2 code that directly subcasses `BaseModel`.

## Conclusions

The aim of this exercise is to highlight how understanding the available Pydantic v2 objects and using them appropriately can yield significant performance improvements over older versions. It makes sense to explore the Pydantic v2 docs in more detail and see how to improve the readability of code while also maximizing performance.

# Run benchmark for v2

Activate the virtual environment that has Pydantic v2 installed. Then, run the validator code as follows.

```sh
$ python validator.py
Validated 129971 records in cycle 1 of 10
Single case: 0.600 sec
Validated 129971 records in cycle 2 of 10
Single case: 0.573 sec
Validated 129971 records in cycle 3 of 10
Single case: 0.581 sec
Validated 129971 records in cycle 4 of 10
Single case: 0.588 sec
Validated 129971 records in cycle 5 of 10
Single case: 0.586 sec
Validated 129971 records in cycle 6 of 10
Single case: 0.586 sec
Validated 129971 records in cycle 7 of 10
Single case: 0.581 sec
Validated 129971 records in cycle 8 of 10
Single case: 0.580 sec
Validated 129971 records in cycle 9 of 10
Single case: 0.586 sec
Validated 129971 records in cycle 10 of 10
Single case: 0.596 sec
All cases: 6.076 sec
```

Running ~1.3 million validations on this sample dataset using Pydantic v2 took ~6 sec. The timing numbers shown are from an M2 Macbook Pro. Depending on your CPU, your mileage may vary.

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

With the optimized version, running ~1.3 million validations on this sample dataset using Pydantic v2 took ~3.4 sec, which is almost a 10x improvement from the v1 code! The optimized code is a little more verbose than the original, but understanding how to use Pydantic objects appropriately can yield great dividends in terms of performance.

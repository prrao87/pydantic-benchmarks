# Run benchmark for v1

Activate the virtual environment that has Pydantic v1 installed. Then, run the validator code as follows.

```sh
$ python validator.py
Validated 129971 records in cycle 1 of 10
Single case: 3.010 sec
Validated 129971 records in cycle 2 of 10
Single case: 2.982 sec
Validated 129971 records in cycle 3 of 10
Single case: 2.974 sec
Validated 129971 records in cycle 4 of 10
Single case: 2.977 sec
Validated 129971 records in cycle 5 of 10
Single case: 2.999 sec
Validated 129971 records in cycle 6 of 10
Single case: 2.982 sec
Validated 129971 records in cycle 7 of 10
Single case: 2.988 sec
Validated 129971 records in cycle 8 of 10
Single case: 3.016 sec
Validated 129971 records in cycle 9 of 10
Single case: 3.012 sec
Validated 129971 records in cycle 10 of 10
Single case: 2.994 sec
All cases: 30.149 sec
```

Running ~1.3 million validations on this sample dataset using Pydantic v1 took ~30 sec. The timing numbers shown are from an M2 Macbook Pro. Depending on your CPU, your mileage may vary.

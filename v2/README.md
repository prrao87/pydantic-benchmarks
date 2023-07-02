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

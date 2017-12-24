# testdome_rewards_points
The following RewardPoint class tracks the points every customer has earned.

### Conditions
Class must comply with following requirements:

* When a customer earn points for first time, will receive an additional 500 bonus points.
* _spend points_ show always return the points that customer has earned. If customer doest no exist, zero must be returned.
* If 0 or less points is passed to _earn_points_ the custmer's point should be unaffected.
* If more points are passwd to _spend_points_ than the customer has available then their current balance should be returned unaffected.

### Example

```python
rewardPoints = RewardPoints()
rewardPoints.earn_points('John', 520)
print(rewardPoints.spend_points('John', 200)
```

Should display: _820_

### Run Tests

```sh 
$ python -m unittest test_rewardspoints.py
```

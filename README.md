# stlbs
`stlbs` is a simple, happy little Python library  which has only one class: `StLb`. An instance of `StLb` represents a weight in the form of stones and pounds (lbs). It allows arithmatic with weights in stones and pounds in a very nautural and easy to use way.

## Basic usage

### The StLb object - initialisation

The `StLb()` class is a data type to hold weights in stones and lbs.
```python
>>> from stlbs import StLb
```

`StLb()` is initialised with either a list or a tuple to represent whole stones and the remainder lbs:
```
>>> my_weight = StLb([10, 7])
>>> my_weight
StLb object: 10st and 7 lb [147 lb]
```
As you can see, we get a nice textual representation of the object.

You can also initialise `StLb` by passing only lbs:
```
>>> my_weight = StLb([0, 147])
>>> my_weight
StLb object: 10st and 7 lb [147 lb]
```
When initialised with lbs only, such as in the example above, the `StLb` object will correctly convert to stones and lbs.

### `StLb` attributes

An instance of `StLb` has a number of useful attributes:
```
>>> my_weight = StLb([10, 7])

>>> my_weight.whole_stones
10

>>> my_weight.remainder_lbs
7

>>> my_weight.in_lbs
147

>>> my_weight.text
'10st and 7 lb [147 lb]'
```

## Doing sums with `StLb` objects

### Addition

You can add two instances of `StLb` together:
```
>>> my_first_weight = StLb((4, 7))
>>> my_second_weight = StLb((1, 0))
>>> my_first_weight + my_second_weight
StLb object: 5st and 7 lb [77 lb]
```

You can also add in place to a single `StLb` object:
```
>>> my_weight = StLb((4, 7))
>>> my_weight
StLb object: 4st and 7 lb [63 lb]

>>> my_weight += (1, 0)  # Add 1st and zero lbs
>>> my_weight
StLb object: 5st and 7 lb [77 lb]
```
### Subtraction
Subtraction works in the same way as addition. You can subtract one instance of `StLb` from another:
```
>>> my_first_weight = StLb((4, 7))
>>> my_second_weight = StLb((1, 0))
>>> my_first_weight - my_second_weight
StLb object: 3st and 7 lb [49 lb]
```
You can also subtract in place:
```
>>> my_weight = StLb([4, 7])
>>> my_weight -= (1, 0)
>>> my_weight
StLb object: 3st and 7 lb [49 lb]
```
Note that the result of subtraction from an instance of `StLb` cannot be negative. Any matematical operation that would result in a negative number raises a `SubtractionBelowZeroError` exception.
### Multiplication

You can multiply two `StLb` objects together:
```
>>> weight_1 = StLb((2, 0))
>>> weight_2 = StLb((2, 0))
>>> weight_1 * weight_2
StLb object: 56st and 0 lb [784 lb]
```
That answer might look surprising if you were expecting `2st * 2st` to equal `4st`. Multiplying two `StLb` objects together multiplies their `in_lbs` values and converts back to stones and lbs. Our example of `2st * 2st` is the same as saying `28lbs * 28lbs`, which gives `784lbs` or `56st`.

If you just want to multiply a StLb object by a number (rather than another `StLb instance), you can:
```
>>> my_weight = StLb((2, 0))
>>> my_weight * 2
StLb object: 4st and 0 lb [56 lb]
```
### Division 

Lastly, it is also possible to divide instances of `StLb`:
```
>>> weight_1 = StLb((10, 0))
>>> weight_2 = StLb((5, 0))
>>> weight_1 / weight_2
2.0
```

You can also divide a `StLb` object by a number:
```
>>> weight_1 = StLb((4, 0))
>>> weight_1
StLb object: 4st and 0 lb [56 lb]
>>> weight_1 / 2
StLb object: 2.0st and 0.0 lb [28.0 lb]
```

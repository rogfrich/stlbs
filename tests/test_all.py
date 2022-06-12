import pytest
from exceptions import SubtractionBelowZeroError


def test_stlb_class_is_importable():
    """
    Given that the StLbs package is installed
    as a user of the package
    I want to be able to import it.
    """
    from stlbs import StLb


def test_input_weight_correctly_assigned():
    """
    Given that I have created an instance of StLb and passed it the correct parameters for stones and lbs
    as a user of the package
    I want the values of instance.whole_stones and instance.remainder_lbs to be correct
    """
    from stlbs import StLb

    x = StLb([10, 1])
    assert x.whole_stones == 10
    assert x.remainder_lbs == 1


def test_in_lbs():
    """
    Given that I have created an instance of StLb and passed it the correct parameters for stones and lbs
    as a user of the package
    I want the value of instance.in_lbs to be (stones * 14) + remainder lbs
    """
    from stlbs import StLb

    test1 = StLb([10, 1])
    assert test1.in_lbs == 141

    test2 = StLb([0, 4])
    assert test2.in_lbs == 4

    test3 = StLb([1, 0])
    assert test3.in_lbs == 14

    test4 = StLb([0, 281])
    assert test4.in_lbs == 281


def test_weight_in_lbs_only():
    """
    Given that an instance of StLb is instantiated with a "lbs only" value >= 14 (i.e [0, 280])
    as a user of the package
    I want the "lbs only" value to be correctly converted into stones and lbs and whole_stones and remainder_lbs to be set
    """
    from stlbs import StLb

    test1 = StLb([0, 281])  # 20 stones and 1 lb
    assert test1.whole_stones == 20
    assert test1.remainder_lbs == 1
    assert test1.in_lbs == 281

    test2 = StLb([0, 15])
    assert test2.whole_stones == 1
    assert test2.remainder_lbs == 1
    assert test2.in_lbs == 15

    test3 = StLb([0, 14])
    assert test3.whole_stones == 1
    assert test3.remainder_lbs == 0
    assert test3.in_lbs == 14


def test_add():
    """
    Given that I have StLb objects called spam and eggs, and the expression (foo = spam + eggs)
    as a user of the package
    I want foo to be an instance of StLb with its whole_stones, remainder_lbs and in_lbs values equal to the total of
    the corresponding values in spam and eggs
    """
    from stlbs import StLb

    test1_spam = StLb([1, 0])
    test1_eggs = StLb([0, 7])
    test1_foo = test1_spam + test1_eggs
    assert test1_foo.whole_stones == 1
    assert test1_foo.remainder_lbs == 7
    assert test1_foo.in_lbs == 21

    test2_spam = StLb([10, 7])
    test2_eggs = StLb([1, 8])
    test2_foo = test2_spam + test2_eggs
    assert test2_foo.whole_stones == 12
    assert test2_foo.remainder_lbs == 1
    assert test2_foo.in_lbs == 169


def test_subtract():
    """
    Given that I have StLb objects called spam and eggs, and the expression (foo = spam - eggs)
    as a user of the package
    I want foo to be an instance of StLb with its whole_stones, remainder_lbs and in_lbs values equal to the value of
    the corresponding values in spam minus the corresponding value in eggs
    """
    from stlbs import StLb

    test1_spam = StLb([1, 0])
    test1_eggs = StLb([0, 7])
    test1_foo = test1_spam - test1_eggs
    assert test1_foo.whole_stones == 0
    assert test1_foo.remainder_lbs == 7
    assert test1_foo.in_lbs == 7

    test2_spam = StLb([10, 7])
    test2_eggs = StLb([1, 8])
    test2_foo = test2_spam - test2_eggs
    assert test2_foo.whole_stones == 8
    assert test2_foo.remainder_lbs == 13
    assert test2_foo.in_lbs == 125


def test_add_iteratble():
    """
    Given that I have an StLb object
    As a user of the package
    I want to add the value of an iterable, (1, 7) for example, to whole_stones and remainder_lbs
    in_lbs should be updated accordingly
    """
    from stlbs import StLb

    spam = StLb([1, 0])
    spam += (1, 0)
    assert spam.whole_stones == 2 and spam.remainder_lbs == 0 and spam.in_lbs == 28

    spam = StLb([1, 0])
    spam += (0, 15)
    assert spam.whole_stones == 2 and spam.remainder_lbs == 1 and spam.in_lbs == 29
    assert spam.__str__() == "StLb object: 2 stones and 1 lbs [29 lbs]"


def test_subtract_iterable():
    """
    Given that I have an StLb object
    As a user of the package
    I want to subtract the value of an iterable, (1, 7) for example, from whole_stones and remainder_lbs
    in_lbs should be updated accordingly
    If the final value is negative, raise a SubtractionBelowZeroError (but not if the value is zero)
    """
    from stlbs import StLb

    spam = StLb([3, 7])
    spam -= (1, 1)
    assert spam.whole_stones == 2 and spam.remainder_lbs == 6 and spam.in_lbs == 34

    spam = StLb([2, 0])
    spam -= (0, 7)
    assert spam.whole_stones == 1 and spam.remainder_lbs == 7 and spam.in_lbs == 21

    # result is exactly zero: should not raise SubtractionBelowZeroError
    spam = StLb((2, 0))
    spam -= [2, 0]
    assert spam.in_lbs == 0


def test_subtraction_below_zero_raises_exception():
    """
    Given that the result of (StLb1 - StLb2) cannot be below zero
    as a user of the package
    I want a SubtractionBelowZeroError exception to be raised if (StLb1 - StLb2) < 0
    An error should not be raised if the total == 0
    """
    from stlbs import StLb

    spam = StLb([1, 0])
    eggs = StLb([1, 1])

    with pytest.raises(SubtractionBelowZeroError):
        foo = spam - eggs

    with pytest.raises(SubtractionBelowZeroError):
        spam = StLb([1, 0])
        spam -= (1, 1)

    # Test that subtraction resulting in zero does not raise error
    spam = StLb([1, 0])
    eggs = StLb([1, 0])
    foo = spam - eggs
    assert foo.in_lbs == 0


def test_str():
    """
    Given that I have a StLb object
    As a user of the package
    I want its __str__() method to return a meaningful message
    """
    from stlbs import StLb

    foo = StLb([0, 277.5])
    correct = "StLb object: 19.0 stones and 11.5 lbs [277.5 lbs]"
    assert foo.__str__() == correct


def test_repr():
    """
    Given that I have a StLb object
    As a user of the package
    I want its __repr__() method to return a meaningful message
    """
    from stlbs import StLb

    foo = StLb([0, 277.5])
    correct = "StLb object: 19.0 stones and 11.5 lbs [277.5 lbs]"
    assert foo.__repr__() == correct


def test_convert_stones_and_lbs_to_lbs():
    """
    Given that have multiple places in the code where a (stones, lbs) format needs to be converted to (0, value_in_lbs)
    As the maintainer of the package
    I want a single function that does this calculation
    """
    from stlbs import StLb

    foo = StLb(
        [1, 0]
    )  # Value of foo is irrelevant to the test - just need to instantiate an instance, and have to give it some initial params
    correct = 15
    assert foo._convert_stones_and_lbs_to_lbs((1, 1)) == correct

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
    as a user of the system
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

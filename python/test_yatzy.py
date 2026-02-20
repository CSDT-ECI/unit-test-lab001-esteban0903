from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual        


def test_should_return_result():
        chance = Yatzy.chance(2, 3, 4, 5, 1)
        expected = 15
        assert expected == chance

def test_should_return_50_for_yatzy():
        assert 50 == Yatzy.yatzy([4, 4, 4, 4, 4])

def test_should_return_0_for_non_yatzy():
        assert 0 == Yatzy.yatzy([6, 6, 6, 6, 3])

def test_should_return_sum_of_ones():
        assert 5 == Yatzy.ones(1, 1, 1, 1, 1)

def test_should_return_sum_of_twos():
        assert 10 == Yatzy.twos(2, 2, 2, 2, 2)

def test_should_return_sum_of_threes():
        assert 15 == Yatzy.threes(3, 3, 3, 3, 3)

def test_should_return_sum_of_fours():
        assert 20 == Yatzy(4, 4, 4, 4, 4).fours()

def test_should_return_sum_of_fives():
        assert 25 == Yatzy(5, 5, 5, 5, 5).fives()

def test_should_return_sum_of_sixes():
        assert 30 == Yatzy(6, 6, 6, 6, 6).sixes()

def test_should_return_score_for_small_straight():
        assert 15 == Yatzy.smallStraight(1, 2, 3, 4, 5)

def test_should_return_score_for_large_straight():
        assert 20 == Yatzy.largeStraight(2, 3, 4, 5, 6)

def test_should_return_score_for_full_house():
        assert 18 == Yatzy.fullHouse(6, 2, 2, 2, 6)

def test_should_return_0_for_non_full_house():
        assert 0 == Yatzy.fullHouse(2, 3, 4, 5, 6)



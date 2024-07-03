import random
from All_classes.Card_class import Card

def test_Card():
    x = random.sample(range(0, 105), 5)
    for i in range(len(x)):
        a = Card(x[i])
        print(a)
        assert a.value == x[i]

def test_hand_point():
    values = [1, 5, 10, 15, 55, 66, 104]
    needed_points = [1, 2, 3, 2, 7, 5, 1]
    actual_points = []
    for number in values:
        a = Card(number)
        actual_points.append(a.point)
    assert actual_points == needed_points



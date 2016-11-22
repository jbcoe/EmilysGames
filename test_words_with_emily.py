import words_with_emily


def test_complete_match_scores_world_length_points():
    w = "hello"
    p, matches = words_with_emily.calculate_points(w, w)

    assert p == len(w)
    assert matches == [x for x in w]


def test_no_match_scores_zero_points():
    w = "hello"
    m = "buggy"
    p, matches = words_with_emily.calculate_points(w, m)

    assert p == 0
    assert matches == []

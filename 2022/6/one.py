"""2022, day 6, part 1"""


def first_unique(chars):
    for idx in range(0, len(chars) - 4):
        part = chars[idx : (idx + 4)]
        if len(set(part)) == 4:
            return idx + 4

    return 0


def test_first_unique():
    assert first_unique("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert first_unique("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert first_unique("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert first_unique("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert first_unique("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_solution():
    input = "..."
    assert first_unique(input) == None

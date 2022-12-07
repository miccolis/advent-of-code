"""2022, day 6, part 1"""


def first_unique(chars):
    plen = 14
    for idx in range(0, len(chars) - plen):
        part = chars[idx : (idx + plen)]
        if len(set(part)) == plen:
            return idx + plen

    return 0


def test_first_unique():
    assert first_unique("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert first_unique("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert first_unique("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert first_unique("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert first_unique("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26


def test_solution():
    input = "..."
    assert first_unique(input) == None

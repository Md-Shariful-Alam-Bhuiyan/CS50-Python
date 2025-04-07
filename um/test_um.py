from um import count

def main():
    test_upper_and_lower_case()
    test_with_word()
    test_with_space()


def test_upper_and_lower_case():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_with_word():
    assert count("Yummy") == 0
    assert count("Yum") == 0


def test_with_space():
    assert count("Hello um Here") == 1
    assert count(" UM ?") == 1


if __name__ == "__main__":
    main()

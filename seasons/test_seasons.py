from seasons import check_birthday

def main():
    test_check_birthday()


def test_check_birthday():
    assert check_birthday("1989-06-31") == ("1989","06","31")
    assert check_birthday("2005-05-30") == ("2005","05","30")
    assert check_birthday("1987-5-8") == ("1987","5","8")
    assert check_birthday("January 2, 1995") == None


if __name__ == "__main__":
    main()

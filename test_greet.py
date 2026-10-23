from greet import greet


def main():
    message = greet('Ada')
    assert 'Ada' in message, "FAIL: greet() output must include the caller's name"
    print("PASS: greet() output includes the caller's name")


if __name__ == '__main__':
    main()

def main():
    print('hello')
    return 'hello'

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5

def test_main():
    assert main() == 'hello'

if __name__ == "__main__":
    # execute only if run as a script
    main()

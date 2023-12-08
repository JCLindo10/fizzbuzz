if __name__ == "__main__":
    print(*map(lambda x: 'Fizz'*(not x%3) + 'Buzz'*(not x%5) or x, range(100)), sep='\n')

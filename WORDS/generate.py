import itertools

def generate_words():
    characters = 'abcdefghijklmnopqrstuvwxyz'
    min_length = 8
    max_length = 10

    for length in range(min_length, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            word = ''.join(combination)
            print(word)

if __name__ == "__main__":
    generate_words()



from itertools import permutations

def genwords(*iterables):
    return [''.join(letters) for letters in permutations(*iterables)]

if __name__ == "__main__":
    print("start")
    chars = ['K', 'T', 'K', 'T', 'R', 'O', 'L', 'D', 'E', 'R', 'A', 'I']
    # chars = ["KTKTROLDERAI"]
    print(genwords(chars))
    print("end")


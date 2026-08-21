def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    vowels = "aeiouAEIOU"
    short = ""
    for letter in word:
        if letter not in vowels:
            short = short + letter
    return short

if __name__ == "__main__":
    main()

def convert(text):
    return text.replace(":)","🙂").replace(":(","🙁")
def main():
    mood = input("Wpythohat's your mood today? ")
    result = convert(mood)
    print(result)
main()

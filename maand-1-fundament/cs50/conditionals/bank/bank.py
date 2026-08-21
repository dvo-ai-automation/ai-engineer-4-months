greeted = input ("Greeting: ")
greeted = greeted.lower().strip()
if greeted.startswith("hello"):
    print("$0")
elif greeted.startswith("h"):
    print("$20")
else:
    print("$100")

def main():
    time = input("What time is it? ")
    hours = convert(time)
    if hours >= 7 and hours <= 8:
        print("breakfast time")
    elif hours >= 12 and hours <= 13:
        print("lunch time")
    elif hours >= 18 and hours <= 19:
        print("dinner time")

def convert(time):
    if time.endswith("a.m."):
        time = time.replace("a.m.","")
        period = "a.m."
    elif time.endswith ("p.m."):
        time = time.replace("p.m.","")
        period = "p.m."
    else:
        period = ""
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    if period == "a.m." and hours == 12:
        hours = hours - 12
    if period == "p.m." and hours != 12:
        hours = hours + 12
    result = hours + minutes / 60
    return result

if __name__ == "__main__":
    main()

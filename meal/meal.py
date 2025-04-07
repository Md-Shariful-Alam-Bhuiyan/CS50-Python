

def main():
    time = input("Please Enter time in 12 or 24 hours format: ")
    time = time.strip()
    time = convert(time)
   

# Determine the meal time
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")

# Convert input to corresponding number of hours as a float
def convert(t:str):

# Check if the input contains "a.m." or "p.m."
    if "a.m." in t.lower():
        t = t.replace("a.m.","").strip()
        is_pm = False
    elif "p.m." in t.lower():
        t = t.replace("p.m.","").strip()
        is_pm = True
    else:
        is_pm = None



    hours, minutes = t.split(":")
    hours = float(hours)

    #Convert to 24 hours format
    if is_pm:
        hours += 12

    minutes = float(minutes)/60

    return hours + minutes

main()

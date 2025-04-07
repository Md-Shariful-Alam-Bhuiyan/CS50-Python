months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    # Taking user input
    date = input("Date: ")
    try:
        # Spliting the input into month, date & year
        month, date, year = date.split("/")
        # Checking the condition if the values of month & date are within the boundary
        if (int(month) >= 1 and int(month) <=12 and int(date) >= 1 and int(date) <= 31):
            break


    except:
        try:
            month, date, year = date.split()
            # checking months' position from the list months
            for i in range(len(months)):
                if month == months[i]:
                    month = i+1
            date = date.replace(",","")
            # Checking the condition if the values of month & date are within the boundary
            if (int(month) >= 1 and int(month) <=12 and int(date) >= 1 and int(date) <= 31):
                break

        except:
            print()
            pass
print(f"{year}-{int(month):02}-{int(date):02}")



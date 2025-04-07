def main():
    plate = input("plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s: str):
    # Check if the string length is within the valid range
    if len(s) < 2 or len(s)> 6:
        return False
    #Check the First two letter is Alphabet Character
    if not s[0:2].isalpha():
        return False
    # Check if the string contains only letters and numbers
    if not s[0:6].isalnum():
        return False
    #The first number used cannot be zero
    for i in range(len(s)):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
               break
    # Numbers cannot be used in the middle of the plate, meaning letters cannot come after number
    for i in range(len(s)):
        if s[i].isalpha() == False:
            while i < len(s)-1:
                if s[i+1].isalpha() == True:
                    return False
                else:
                    break



    # Check for any invalid characters (periods, spaces, punctuation marks)

    p = ['.', ' ', ',', ';', ':', '-', '+','*' '=', '!', '?','/','"','>','<']

    for i in s:
        if i in p:
            return False


    return True

main()

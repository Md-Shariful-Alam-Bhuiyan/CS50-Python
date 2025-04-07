from validator_collection import validators

def main():
    e_mail = input("What's your email address ? ")
    try:
        if validators.email(e_mail):
            print("Valid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()

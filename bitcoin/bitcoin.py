import sys
import requests



if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
        try:
            r =  requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            response = r.json()
            rate = response["bpi"]["USD"]["rate_float"]
            amount = rate * value
            print(f"${amount:,.4f}")

        except requests.RequestException:
            print("Request Exception Occured")
            sys.exit(1)

    except:
        print("Command line argument is not a number")
        sys.exit(1)
else:
    print("Missing command line argument")
    sys.exit(1)



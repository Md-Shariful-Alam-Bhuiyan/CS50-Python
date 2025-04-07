def convert(txt: str):
    txt = txt.replace(":)","🙂")
    txt = txt.replace(":(","🙁")
    return txt

def main():
    x = input("Enter your text : ")
    y = convert(x)

    print(y)

main()

def main():
    #input form user
    x = input("Enter text: ").strip()
    print(shorten(x))

def shorten(word:str):
    vowels = ["a","e","i","o","u"]
    for i in word:
        if i.lower() in vowels:
            word = word.replace(i,"")
        else:
            pass
    return word

if __name__=="__main__":
    main()



def first():
    hello("World")
    goodbye("World")

def hello(name:str):
    print(f"Hello {name}")

def goodbye(name:str):
    print(f"Goodbye {name}")

if __name__ == "__main__":
    first()

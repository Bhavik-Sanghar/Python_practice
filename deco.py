def deco(fun):
    print("Hii..")
    return fun

@deco
def main():
    print("Hiii.. there")

main()
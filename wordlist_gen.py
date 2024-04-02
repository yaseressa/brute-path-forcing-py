
def main():
    try:
        rg = list(map(int, input("Enter the range: ").split(",")))
        with open("wordlist.txt", 'w') as file:
            for i in range(rg[0], rg[1]):
                file.write(str(i) + "\n")
    except OSError:
        print("File doesn't exist")




if __name__ == "__main__":
    main()
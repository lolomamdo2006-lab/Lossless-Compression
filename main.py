from lz77 import compress as lz77_compress
def main():
    print("===== Lossless Compression =====")
    print("1. LZ77")
    print("2. LZ78")
    print("3. LZW")
    print("4. Exit")

    choice = input("Choose an algorithm: ")
    text = input("Enter text to compress: ")
    match choice:
        case 1:
            #Lz77
            pass
        case 2:
            #Lz88
            pass
        case 3:
            #lwz
            pass
        case 4:
            print("Goodbye!")

        case _:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
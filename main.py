from menu import *
def main():
    while True:
        print("\n===== Lossless Compression =====")
        print("1. Compress")
        print("2. Decompress")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            compression_menu()

        elif choice == "2":
            decompression_menu()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
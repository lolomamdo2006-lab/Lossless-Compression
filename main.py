import lz77
from lz78 import compress_to_lz78
from lz78 import decompress_lz78
from lzw import lzw_compress_fuc, lzw_decompress_fuc


def compression_menu():
    print("\n===== Compression =====")
    print("1. LZ77")
    print("2. LZ78")
    print("3. LZW")
    print("4. Back")

    choice = input("Choose an algorithm: ")

    if choice == "1":
        text = input("Enter text to compress: ")
        tags=lz77.compress(text)
        print("Tags: ",tags)
        lz77.compression_ratio(text,tags)

    elif choice == "2":
        text = input("Enter text to compress: ")
        compress_to_lz78(text)

    elif choice == "3":
        text = input("Enter text to compress: ")
        lzw_compress_fuc(text)
        

    elif choice == "4":
        return

    else:
        print("Invalid choice!")


def decompression_menu():
    print("\n===== Decompression =====")
    print("1. LZ77")
    print("2. LZ78")
    print("3. LZW")
    print("4. Back")

    choice = input("Choose an algorithm: ")

    if choice == "1":
        data = input("Enter tags like 0 0 A, 0 0 B, 2 1 A : ")
        tags = lz77.read_tags(data)
        text = lz77.decompress(tags)
        print("Text:", text)
        lz77.compression_ratio(text, tags)

    elif choice == "2":
        data = input("Enter compressed data like 00A00B")
        text=lz77.read_tags(data)
        print("compressed data : ", text)

    elif choice == "3":
        compressed_data = input("Enter compressed data: ")
        lzw_decompress_fuc(compressed_data)

    elif choice == "4":
        return

    else:
        print("Invalid choice!")


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
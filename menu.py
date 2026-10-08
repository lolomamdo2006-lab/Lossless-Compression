from handling_files import *
from lz78 import *
from lz77 import *
from lzw import *
def getInput_compresion():
    while True:
        print("\n===== File or Text =====")
        print("1. File")
        print("2. Text")

        choice = input("Choose an option: ")

        if choice == "1":
            filename = input("Enter filename: ")
            data = read_file(filename)
            return data

        elif choice == "2":
            text = input("Enter text: ")
            return text

        else:
            print("Invalid choice! Please choose 1 or 2.")
def getInput_decompresion(choice):
    while True:
        print("\n===== Decompression Input =====")
        print("1. Enter Compressed Data")
        print("2. Read from File")

        input_choice = input("Choose Input Type: ")

        if input_choice == "1":
            if choice == "1":
                return input("Enter tags like 0 0 A, 0 0 B, 2 1 A : ")

            elif choice == "2":
                return input("Enter tags like 0 A, 0 B, 1 A : ")

            elif choice == "3":
                return input("Enter codes like 65 66 128 : ")

        elif input_choice == "2":
            filename = input("Enter file name: ")
            return read_file(filename)

        else:
            print("Invalid choice! Please choose 1 or 2.")
def compression_menu():
    print("\n===== Compression =====")
    print("1. LZ77")
    print("2. LZ78")
    print("3. LZW")
    print("4. Back")

    choice = input("Choose an algorithm: ")
    compressed_data = ""


    if choice == "1":
        file_or_text = getInput_compresion()
        tags=compress_lz77(file_or_text)
        print("Tags: ",tags)
        compression_ratio_lz77(file_or_text,tags)
        compressed_data = lz77_to_text(tags)

    elif choice == "2":
        file_or_text = getInput_compresion()
        tags = compress_to_lz78(file_or_text)
        compressed_data = parse_string(tags)

    elif choice == "3":
        file_or_text = getInput_compresion()
        compressed_data = lzw_compress_fuc(file_or_text)

    elif choice == "4":
        return

    else:
        print("Invalid choice!")
    save_choice = input("Do you want to save the compressed data? (y/n): ")
    if save_choice.lower() == "y":
        file_save(compressed_data) 
    if save_choice.lower() == "n":
        print("Data not saved.")
def decompression_menu():
    print("\n===== Decompression =====")
    print("1. LZ77")
    print("2. LZ78")
    print("3. LZW")
    print("4. Back")

    choice = input("Choose an algorithm: ")
    decompressed_data = ""

    if choice == "1":
        file_or_text = getInput_decompresion(choice)
        tags = read_tags(file_or_text)
        decompressed_data = decompress_lz77(tags)
        print("Text:", decompressed_data)

    elif choice == "2":
        
        file_or_text = getInput_decompresion(choice)
        decompressed_data = decompress_lz78(file_or_text)
        

    elif choice == "3":
        file_or_text = getInput_decompresion(choice)
        clean_data = lzw_clean_fuc(file_or_text)
        decompressed_data = lzw_decompress_fuc(clean_data)

    elif choice == "4":
        return

    else:
        print("Invalid choice!")
    save_choice = input("Do you want to save the decompressed data? (y/n): ")
    if save_choice.lower() == "y":
        file_save(decompressed_data)
    elif save_choice.lower() == "n":
        print("Data not saved.")
def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


def write_file(filename, data):
    with open(filename, "w") as file:
        file.write(data)


def file_save(data):
    filename = input("Enter filename to save: ")
    filepath= input("Enter file path to save: ")
    filename = filepath + "/" + filename

    with open(filename, "w") as file:
        file.write(str(data))
    print(f"Data saved to {filename}")
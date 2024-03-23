def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line here with some numbers: 67890\n")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    finally:
        print("File creation completed.")


def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Content of my_file.txt:")
            print(content)
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")


def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    finally:
        print("Appending completed.")


if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()

def read_full_file(filename):
    with open(filename, "r") as f_input:
        return f_input.read()

def read_file_lines(filename):
    with open(filename, "r") as f_input:
        return f_input.readlines()

def print_full_file(filename):
    print(read_full_file(filename))

def write_in_file(filename, text):
    with open(filename, "r+") as f_output:
        f_output.write(f"{text}\n")

if __name__ == "__main__":
    # file_lines = read_file_lines("text.txt")
    # print(file_lines)

    write_in_file("text.out", "Salut, acesta este un output!")

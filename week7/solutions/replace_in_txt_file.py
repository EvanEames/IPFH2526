def replace_in_txt_file(txt_file, word_to_be_replaced, replacement):
    with open(txt_file, "r") as reader_file:
        data = reader_file.read()
        new_string = data.replace(word_to_be_replaced, replacement)
    with open(txt_file, "w") as writing_file:
        writing_file.write(new_string)

replace_in_txt_file("output.txt", "seventh", "eight")
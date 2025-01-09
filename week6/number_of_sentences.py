import re

def number_of_sentences_no_reg(string):
    characters = list(string)
    # ["H","."," ","W","?"]
    total = 0
    total = total + characters.count(".")
    total = total + characters.count("!")
    total = total + characters.count("?")
    return total

def number_of_sentences_no_reg2(string):
    end = [".", "?", "!"]
    total = 0
    for character in string:
        if character in end:
            total += 1
    return total

print(number_of_sentences_no_reg("I am Bruno. I am a computer scientist! What is your name?!"))


def number_of_sentences(string):
    sentence_separator_list = re.findall(r"[.!?]+", string)
    return len(sentence_separator_list)

print(number_of_sentences("My name is Bruno. I am a computer scientist!!! What is your name?"))

def number_of_sentences2(string):
    # "Hi!!! What is your name?!"
    string = string.replace("!",".")
    # "Hi... What is your name?."
    string = string.replace("?", ".")
    # "# "Hi... What is your name.."
    string = re.sub(r"[.]+", ".", string)
    # "Hi. What is your name."
    sentences = string.split(".")
    # ["Hi", " What is your name", ""]
    sentences.remove("")
    # ["Hi", " What is your name"]
    return len(sentences)
    #2

print(number_of_sentences2("My name is Bruno. I am a computer scientist!!! What is your name?"))


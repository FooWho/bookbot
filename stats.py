def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_helper(element):
    return element["num"]

def sorted_list(char_count):
    result_list = list()

    for element in char_count:
        result_list.append({"char": element, "num": char_count[element]})

    result_list.sort(reverse=True, key=sort_helper)

    return result_list


    
    

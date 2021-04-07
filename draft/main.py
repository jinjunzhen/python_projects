

def alphabet_position(input_str):
    alph = "abcdefghijklmnopqrstuvwxyz"
    dict_aplh = {letter: (ord(letter) - 96) for letter in alph}

    answer = [dict_aplh[char.lower()] for char in input_str if char.isalpha()]
    answer_str = ""
    for ele in answer:
        answer_str += str(ele)
        answer_str += ' '
    return answer_str.strip()




print(alphabet_position("The sunset sets at twelve o' clock."))

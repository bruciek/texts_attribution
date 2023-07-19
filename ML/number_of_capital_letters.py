import re
def number_of_capital_letter(sentences:list[str], beginning_of_sentences:bool) -> int:
    full_pattern = re.compile('[^АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ]')
    cap_letters_from_text = re.sub(full_pattern, '', ''.join(sentences))
    return len(cap_letters_from_text) if beginning_of_sentences else len(cap_letters_from_text) - len(sentences)

#https://stackoverflow.com/questions/23531997/how-to-replace-all-characters-except-letters-numbers-forward-and-back-slashes

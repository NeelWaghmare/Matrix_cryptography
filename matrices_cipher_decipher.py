#!/usr/bin/python

""" 
        Encypting words using matrices. 
        Algorithm works with words not sentences.
        
        Author: Neel Waghmare
"""

column_matrix = []
coding_matrix = [1, 3, 3, 12]
determinant = (coding_matrix[0] * coding_matrix[3]) - (coding_matrix[1] * coding_matrix[2])
mod = 26
reciporal_modulo_of_26 = 19
letters = ["Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]

# Makes the word have an even length, when it doesn't
def make_even(word):
    if len(word) % 2 != 0:
        word = list(word)
        word.append(word[-1])
    return word

# 
def matrix_multiplication(matrix1, matrix2):
    temp = []
    for x in range(len(matrix1)):
        number = (matrix2[-x - x] * matrix1[0]) + (matrix2[(-x - x) + 1] * matrix1[1])
        while number >= mod:
            number -= mod
        temp.append(letters[number])
    return temp

def cipher(word):
    result = []
    for i in word:
        column_matrix.append(letters.index(i))
        if len(column_matrix) == 2:
            result.append(''.join(matrix_multiplication(column_matrix, coding_matrix)))
            column_matrix.clear()
        else: continue
    return ''.join(result)

def decipher(encrypted_word):
    # Inverse of column matrix
    coding_matrix_inverse = [coding_matrix[3], -coding_matrix[1], -coding_matrix[2], coding_matrix[0]]
    for number in coding_matrix_inverse:
        number_index = coding_matrix_inverse.index(number)
        number *= reciporal_modulo_of_26
        while number < 0 and number < mod:
            number += mod
        else:
            while number > mod:
                number -= mod
        coding_matrix_inverse[number_index] = number

    # Deciphering via the inverse coding matrix
    message = []
    for i in encrypted_word:
        column_matrix.append(letters.index(i))
        if len(column_matrix) == 2:
            message.append(''.join(matrix_multiplication(column_matrix, coding_matrix_inverse)))
            column_matrix.clear()
        else: continue
    return ''.join(message).capitalize()

while True:
    try:
        word = input("Enter a word: ").upper().strip()
        mode = input("Cipher of Decipher text: ").lower().strip()
        if mode == "cipher": print(cipher(make_even(word)))
        elif mode == "decipher": print(decipher(word))
        else: raise Exception
    except Exception:
        print("\n'{}' is not valid\n".format(mode))
        continue
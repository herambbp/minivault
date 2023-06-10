import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers = ['0','1','2','3','4','5','6','7','8','9']
def key():
    return random.randrange(0,999999)

def caesar(password, cipher_direction,code=key()):
    end_text = ""
    shift_amount = key()
    if cipher_direction == "decode":
        shift_amount = code
        shift_amount *= -1
    for char in password:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount)%len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += char
    return end_text,shift_amount


# def digit_encrypt(number,cipher_direction,code):
#     number = str(number)
#     end_text = ""
#     shift_amount = code
#     if cipher_direction == "decode":
#         shift_amount = code
#         shift_amount *= -1
#     for digit in number:
#         if digit in number:
#             position = numbers.index(digit)
#             new_position = (position + shift_amount)%len(numbers)
#             end_text += numbers[new_position]
#         else:
#             end_text += digit
#     return int(end_text)


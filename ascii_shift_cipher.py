# Create a Python program that encodes and decodes messages using the shift cipher described
# in this section. The amount of shift must be configurable.
import string

shift = 2


def create_encode_dict():
    encode_dict = {}
    alphabet_len = len(string.ascii_uppercase)
    for i in range(0, alphabet_len):
        letter = string.ascii_uppercase[i]
        upper_num = (i+shift) % alphabet_len
        letter_encoded = string.ascii_uppercase[upper_num]

        encode_dict[letter] = letter_encoded
    return encode_dict


if __name__ == "__main__":
    ed = create_encode_dict()
    print(ed)

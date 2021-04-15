# Create a Python program that encodes and decodes messages using the shift cipher described
# in this section. The amount of shift must be configurable.

message = "HELLO WORLD"
shift = 1
top_position = 90
low_position = 65
message_shifted = ""

diff_position = top_position - low_position
backward_move = diff_position + 1

for i in message:
    i_ascii = ord(i)
    if low_position <= i_ascii <= top_position:
        i_ascii_shifted = i_ascii + shift
        if i_ascii_shifted > top_position:
            i_ascii_shifted -= backward_move
    else:
        i_ascii_shifted = i_ascii
    i_shifted = chr(i_ascii_shifted)
    message_shifted += i_shifted
    pass
print(message_shifted)

def get_key(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key

# Decoded word and corresponding encoded word
dec_word = "RADIO"
enc_word = "UDGLR"

# Check if both words are of the same length
if len(dec_word) == len(enc_word):
    print("Matched")
    
    # Dictionary for mapping letters to numbers
    data = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
            'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19,
            'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

    # Get the shift difference between first letters
    dec_value = data[dec_word[0]]
    enc_value = data[enc_word[0]]
    dif = enc_value - dec_value
    print(f"Shift difference: {dif}")

    # Input a new word to encode
    new_word = input("Enter the word to encode: ").upper()

    new_encode = []

    # Encode each letter using the shift difference
    for i in new_word:
        new_value = (data[i] + dif) % 26  # To handle wrapping of letters
        if new_value == 0:  # Handle 'Z' wrapping case
            new_value = 26
        new_encode.append(get_key(data, new_value))

    # Join the encoded letters into a string
    encoded_word = ''.join(new_encode)
    print(f"Encoded word: {encoded_word}")

else:
    print("Words do not match in length.")

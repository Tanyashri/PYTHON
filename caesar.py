alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))
    
def caesar(original_text,shift_amount,encode_or_decode):
    output_text=""
    for letter in original_text:
        if encode_or_decode=="decode":
            shift_amount*=-1
        shifted_position=alphabets.index(letter) + shift_amount
        shifted_position%=len(alphabets)
        output_text+=alphabets[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")
caesar(text,shift,direction)

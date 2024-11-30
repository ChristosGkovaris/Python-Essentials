import string

def generate_combinations(sentence):
    # All lowercase letters a-z
    alphabet = string.ascii_lowercase
    
    # Split the sentence into words  
    words = sentence.split()  
    current_sentence = ""
    
    for word in words:
        # Add a space between words if it's not the first one
        if current_sentence:  
            current_sentence += " "
        current_sentence += word

        print(f"\nProcessing sentence: {current_sentence}")
        
        # Iterate through prefixes of increasing length
        for length in range(1, len(current_sentence) + 1):  
            # Take a prefix of the current sentence
            prefix = current_sentence[:length]  
            # Append each letter from the alphabet to the prefix
            for char in alphabet:  
                print(prefix + char)
    
    print(f"\nFinal sentence: {current_sentence}")


# Main Program
user_input = input("Enter your sentence: ").strip()

# Ensure input is not empty
if user_input:  
    generate_combinations(user_input)
else:
    print("Input cannot be empty.")
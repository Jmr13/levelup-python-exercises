import secrets

def generate_passphrase(num_words, wordlist_path="diceware.wordlist.asc"):
    # Open the wordlist file in read mode with UTF-8 encoding
    with open(wordlist_path, "r", encoding="utf-8") as file:
        # Read all lines from the file, skipping the first two and stopping before line 7778
        lines = file.readlines()[2:7778]
        # Extract the second element (the actual word) from each line and store in a list
        word_list = [line.split()[1] for line in lines]
        
    # Randomly select 'num_words' words from the word list using a secure random generator
    words = [secrets.choice(word_list) for i in range(num_words)]
    # Join the selected words with spaces to form the final passphrase
    return " ".join(words)

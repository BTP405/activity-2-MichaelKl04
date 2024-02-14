def wordCount(t):
    word_dict = {}
    
    with open(t, 'r') as file:
        for line_num, line in enumerate(file, 1):
            # Split the line into words and normalize them
            words = line.strip().lower().split()
            
            for word in words:
                # If the word is already in the dictionary, append the current line number
                if word in word_dict:
                    word_dict[word].append(line_num)
                else:
                    # Otherwise, create a new entry with the current line number
                    word_dict[word] = [line_num]
    
    return word_dict

words = wordCount('words.txt')
print(words)

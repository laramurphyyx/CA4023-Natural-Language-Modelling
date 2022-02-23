import sys
import re

##
## Accessing the text file provided in the command line
##

filename = sys.argv[1]
file = open(filename, "r", encoding="utf8")
contents = file.read()

##
## Creating method to distinguish sentence boundaries
##

def split_sentences(document):
    
    keywords = set(['Mr.', 'Mrs.', 'Miss.',
                         'Dr.', 'Prof.', 'eg.'])
    
    sentences = []
    words = document.split(' ')

    for word in words:
        
        # If there's a period that is part of an ellipsis, this is ignored
        if len(re.findall("\.\.+", word)):
            sentences.append(word + ' ')
            continue
            
        # If there's a period...
        elif '.' in word:
            
            # If the period is not at the end of the word, this is ignored
            if word[-1] != '.':
                sentences.append(word + ' ')
                continue
                
            # If the period is not part of the abbreviations, this is identified as sentence boundary
            elif word not in keywords:
                sentences.append(word + '\n')
                continue
        
        # If there is an exclamation mark or a question mark, this is identified as a sentence boundary
        elif '!' in word or '?' in word:
            sentences.append(word + '\n')
            continue
        
        # If the word has no ellipsis, or other punctuation as listed above, then it is ignored
        sentences.append(word + ' ')

    # Returning a list of the different sentences
    return ''.join(sentences).split("\n")

##
## Returning output to user
##

output_filename = filename[:-4] + '_sentences.txt'
output_file = open(output_filename, "w")
output_file.write("\n".join(split_sentences(contents)))
output_file.close()

print("Output file saved to '" + output_filename + "'")
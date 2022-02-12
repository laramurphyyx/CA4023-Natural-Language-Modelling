import sys

##
## Functions to create dictionaries for unigram counts and bigram counts
##
            
def make_unigram_dictionary(corpus):
    
    # Assigning an empty dictionary for the counts of each unigram
    unigram_dict = {}
    
    for sentence in corpus:
        
        # Splitting the sentence into a list of unigrams
        sentence_list = sentence.split()
        
        # Adjusting counts for each unigram
        for unigram in sentence_list:
            if unigram in unigram_dict:
                unigram_dict[unigram] += 1
            else:
                unigram_dict[unigram] = 1
                
    return unigram_dict
                
def make_bigram_dictionary(corpus):
    
    # Assigning an empty dictionary for the counts of each bigram
    bigram_dict = {}
    
    for sentence in corpus:
        
        # Splitting the sentence into a list of unigrams
        sentence_list = sentence.split()

        # Grouping unigrams into bigrams (matching each unigram with the one before) and adjusting counts
        for position in range(1, len(sentence_list)):
            if (sentence_list[position - 1], sentence_list[position]) in bigram_dict:
                bigram_dict[(sentence_list[position - 1], sentence_list[position])] += 1
            else:
                bigram_dict[(sentence_list[position - 1], sentence_list[position])] = 1
    
    return bigram_dict

##
## Writing function to calculate probability of sentence
##

def calculate_probability(question, training_corpus=None):
    
    # Assigning the toy training corpus unless another has been provided
    if not training_corpus:
        training_corpus = [
            '<s> a b </s>',
            '<s> b b </s>',
            '<s> b a </s>',
            '<s> a a </s>',
        ]
        
    # Creating dictionaries for unigram and bigram counts
    unigrams = make_unigram_dictionary(training_corpus)
    bigrams = make_bigram_dictionary(training_corpus)
    
    # Splitting the question string, assigning the max probability and assigning previous as a null value
    question_list = question.split()
    probability = 1
    previous = None
    
    for unigram in question_list:
        
        # Accomodating for unigrams/bigrams that do not exist in the unigram/bigram dictionary
        if unigram not in unigrams:
            unigrams[unigram] = 0
        if (previous, unigram) not in bigrams:
            bigrams[(previous, unigram)] = 0

        # Matching each unigram to the one before it, unless it's the first unigram
        if previous:
            probability *= ( bigrams[(previous, unigram)] / unigrams[previous] )
        else:
            probability *= ( unigrams[unigram] / sum(unigrams.values()) )

        # Resetting the previous unigram
        previous = unigram
        
    return probability * 100

question = input("Enter a sentence: ") 

if len(sys.argv) > 1:
    filename = sys.argv[1]
    file = open(filename, "r")
    contents = file.read()
    corpus = contents.split("\n")
    print("The probability of '" + question + "' is " + str(calculate_probability(question, corpus)) + "%")
else:
    print("The probability of '" + question + "' is " + str(calculate_probability(question)) + "%")

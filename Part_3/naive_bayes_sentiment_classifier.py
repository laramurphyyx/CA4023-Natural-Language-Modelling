import os
import math

## - - - - -
## Defining different functions needed for classifier
## - - - - -

def create_reviews_list(directory_path):
    
    reviews_list = []
    
    # For each file that exists in the directory...
    for filename in os.listdir(directory_path):
        
        # Assign the file path as a variable
        file_path = directory_path + "/" + filename
        
        # Open the file
        file = open(file_path, "r")
        
        # Append each line in the review to a list
        review = []
        for line in file.readlines():
            # Strip each line of newline characters
            review.append(line.rstrip())
            
        # Join the lines again and append to review list
        reviews_list.append(" ".join(review))
    
    return reviews_list
        
def create_frequency_dictionary(list_of_reviews):
    
    review_dictionary = {}
    
    # Iterating each word that appears in each review
    for review in list_of_reviews:
        words = review.split()
        
        # Adding the word to the dictionary or increasing it's frequency by 1
        for word in words:
            if word in review_dictionary:
                review_dictionary[word] += 1
            else:
                review_dictionary[word] = 1

    return review_dictionary

def result_for_class(review, training_data):
    
    # Assigning a list for punctuation, the default probability of each class and a dictionary of words in the training data of a certain class
    punctuation = ['.', ',', ':', '"', '&', '?', '-', '(', ')', "'", '/']
    class_result = math.log(0.5)
    dictionary = create_frequency_dictionary(training_data)
    
    for word in review.split():
        
        # Ignore punctuation
        if word in punctuation:
            continue
            
        # If the word is not in the dictionary, treat dictionary[word] as 0
        elif word not in dictionary:
            class_result += math.log(1 / (sum(dictionary.values()) + 1))
        
        # Adding the log probability of the word to the total probability of the class
        else:
            class_result += math.log((dictionary[word] + 1) / (sum(dictionary.values()) + 1))

    return class_result
        
## - - - - -
## Identifying the review datasets
## - - - - -

positive_reviews_directory = input("Enter a path to a directory containing positive reviews (Leave empty to use default Cornell dataset): ")
if not positive_reviews_directory:
    positive_reviews_directory = '../Part_3/review_polarity/txt_sentoken/pos'

negative_reviews_directory = input("Enter a path to a directory containing negative reviews (Leave empty to use default Cornell dataset): ")
if not negative_reviews_directory:
    negative_reviews_directory = '../Part_3/review_polarity/txt_sentoken/neg'

## - - - - -
## Assigning the training/testing datasets
## - - - - -

# Create a list of the reviews contained in each directory
positive_reviews_list = create_reviews_list(positive_reviews_directory)
negative_reviews_list = create_reviews_list(negative_reviews_directory)

# Identifying the 90/10 split for both positive and negative reviews 
positive_90_split = len(positive_reviews_list) * 90 // 100
negative_90_split = len(negative_reviews_list) * 90 // 100

# Splitting the dataset into training and testing sets on a 90/10 split
negative_training_data = negative_reviews_list[:negative_90_split]
positive_training_data = positive_reviews_list[:positive_90_split]
negative_test_data = negative_reviews_list[negative_90_split:]
positive_test_data = positive_reviews_list[positive_90_split:]

## - - - - -
## Testing the Model and identifying Accuracy
## - - - - -

positive_accuracy = 0

for review in positive_test_data:
    positive_result = result_for_class(review, positive_training_data)
    negative_result = result_for_class(review, negative_training_data)
    if positive_result > negative_result:
        positive_accuracy += 1

negative_accuracy = 0

for review in negative_test_data:
    positive_result = result_for_class(review, positive_training_data)
    negative_result = result_for_class(review, negative_training_data)
    if positive_result < negative_result:
        negative_accuracy += 1
        
print("The model's accuracy in identifying positive reviews is " + str(positive_accuracy/len(positive_test_data)*100) + "%")
print("The model's accuracy in identifying negative reviews is " + str(negative_accuracy/len(negative_test_data)*100) + "%")
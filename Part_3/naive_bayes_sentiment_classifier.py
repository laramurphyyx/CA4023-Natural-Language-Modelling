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
## Testing the Model and Identifying Accuracy
## - - - - -

# Creating an initial list to store model results
output_result_list = []

# Creating an initial accuracy score of 0
positive_accuracy = 0
negative_accuracy = 0

# For each review in the positive dataset...
for review_id in range(0, len(positive_test_data)):
    
    # Assign the review as a variable and calculate the scores for positive and negative
    review = positive_test_data[review_id]
    positive_result = result_for_class(review, positive_training_data)
    negative_result = result_for_class(review, negative_training_data)
    
    # If positive has a higher score than negative, then increase the accuracy and add the result to the output list
    if positive_result > negative_result:
        positive_accuracy += 1
        output_result_list.append("The positive test document " + str(review_id) + " has been classified as positive")
    # If positive is less likely than negative, then leave the accuracy and add the result to the output list
    else:
        output_result_list.append("The positive test document " + str(review_id) + " has been classified as negative")

# For each review in the negative dataset...
for review_id in range(0, len(negative_test_data)):
    
    # Assign the review as a variable and calculate the scores for positive and negative
    review = negative_test_data[review_id]
    positive_result = result_for_class(review, positive_training_data)
    negative_result = result_for_class(review, negative_training_data)
    
    # If negative has a higher score than positive, then increase the accuracy and add the result to the output list
    if positive_result < negative_result:
        negative_accuracy += 1
        output_result_list.append("The negative test document " + str(review_id) + " has been classified as negative")
    
    # If negative is less likely than positive, then leave the accuracy and add the result to the output list
    else:
        output_result_list.append("The negative test document " + str(review_id) + " has been classified as positive")

# Calculating Overall Accuracy and Changing Accuracy Figures to Percentages
overall_accuracy = ((positive_accuracy + negative_accuracy) / (len(positive_test_data) + len(negative_test_data))) * 100
positive_accuracy = (positive_accuracy / len(positive_test_data)) * 100
negative_accuracy = (negative_accuracy / len(negative_test_data)) * 100
        
## - - - - -
## Script Output
## - - - - -

# Printing the accuracy of the model
print("The model's accuracy in identifying positive reviews is " + str(positive_accuracy) + "%")
print("The model's accuracy in identifying negative reviews is " + str(negative_accuracy) + "%")
print("The model's overall accuracy is " + str(overall_accuracy) + "%")

# Creating output file if the user accepts
output_preference = input("Would you like an output file containing the classification for each review? (y/n):")
if output_preference.lower() == 'y':
    text_file = open("naive_bayes_classifier_output.txt", "w")
    text_file.write("\n".join(output_result_list))
    text_file.close()

# Giving the user the option to test the model on their own sentences/reviews
extra_review = input("You can test this model by typing your own review (Leave empty to skip): ")
while extra_review:
    
    # Calculating the positive and negative scores
    positive_result = result_for_class(extra_review, positive_training_data)
    negative_result = result_for_class(extra_review, negative_training_data)
    
    # Identifying if the sentence is more likely positive or negative
    if positive_result > negative_result:
        print("This model has identified your review as positive")
    else:
        print("This model has identified your review as negative")
        
    # Giving the option to test another sentence
    extra_review = input("You can test this model again by typing your own review (Leave empty to skip): ")
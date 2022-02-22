# Assignment 1: Part 3

## Task Description

This task involved writing a polarity classifier which uses the Naive Bayes algorithm. This involves training a sentiment polarity classifier which assigns a sentiment of either 'positive' or 'negative' to a review.

The [training data](https://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz) used to train this classifier is described in this [paper by Pang and Lee](https://www.aclweb.org/anthology/P04-1035/). This data consists of 1,000 positive reviews and 1,000 negative reviews. The split should be 9:1 (900 reviews for training and 100 reviews for testing). 

The program should accept the positive and negative reviews as input and should output the predictions of your classifier for each review in the test files.

As part of this task, it is also required to analyse the output of the classifier on 5 misclassified reviews for both positive and negative reviews.

## Task Implementation

This model can be implemented using the command line, simply by running the [naive_bayes_sentiment_classifier.py script](https://github.com/laramurphyyx/CA4023_Assignment1/blob/main/Part_3/naive_bayes_sentiment_classifier.py). Which can be accessed by running in your terminal:

```
python naive_bayes_sentiment_classifier.py
```

The python script will give the user the option to provide a path to a directory containing the positive reviews and another path for the negative reviews, if no path is provided the model will be trained using the default cornell dataset as outlined above.

Once the model is trained, it well test the model on the test dataset and will print the overall accuracy, the accuracy in identifying positive models and the accuracy in identifying negative models. 

At this point, users have the option to download the results as a .txt file, by typing 'y' or 'n' into the input bar. If this is left empty, no output file will be produced.

The user also has the ability to test the model with their own sentences, and the model will predict whether the sentence has positive or negative sentament. 

The screenshot below shows the full process of using this model. Different aspects are highlighted different colours to make it easier to differentiate the different processes. Text that is highlighted yellow is the model requesting the user to provide some information, and text that is highlighted blue is the information provided by the user. The white text is the model output.

![Screenshot of Command Line](https://github.com/laramurphyyx/CA4023_Assignment1/blob/main/Part_3/Output%20Screenshots/Customized_Reviews_Screenshot.png)
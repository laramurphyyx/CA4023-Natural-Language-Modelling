# Assignment 1: Part 1

## Task Description

This is a sentence boundary detection task. We are required to create a model that accepts a text file as input, and outputs a new file with the text split by sentence.

The following is example input for the program:

```
With all the fawning end-of-the-year kudos currently circulating, it’s easy to forget that a sizable number of actual bad movies came out in 2012. Well, consider this a refresher! From failed blockbuster tentpoles (”Battleship”) to would-be hilarious comedies (“The Watch”) to lame scare-challenged horror flicks (“The Apparition”) to...uh, well, pretty much anything involving Mr. Tyler Perry, there’s no doubt that the last 366 days have come with a heaping helping of truly heinous cinematic stinkers. So what better time for an accounting of the year’s most outrageous big-screen abominations than on the eve of the coming apocalypse?
```

The program should output a file with the following text:

```
With all the fawning end-of-the-year kudos currently circulating, it’s easy to forget that a sizable number of actual bad movies came out in 2012.
Well, consider this a refresher!
From failed blockbuster tentpoles (”Battleship”) to would-be hilarious comedies (“The Watch”) to lame scare-challenged horror flicks (“The Apparition”) to...uh, well, pretty much anything involving Mr. Tyler Perry, there’s no doubt that the last 366 days have come with a heaping helping of truly heinous cinematic stinkers.
So what better time for an accounting of the year’s most outrageous big-screen abominations than on the eve of the coming apocalypse?
```

## Task Implementation

This model is contained in the [sentence_boundary_detection.py script]() and can be used through the command line by using the following code:

```
python sentence_boundary_detection.py example_input.txt
```

The code will then return an output file with the same name as the input file with the suffix 'sentences'. In the above example, the model would return a file of the name 'example_input_sentences.txt', as seen below:

![Screenshot of Command Line](https://github.com/laramurphyyx/CA4023_Assignment1/blob/main/Part_1/Output%20Screenshots/Output.png)

The below screenshot shows the contents of the output file for the above example:

![Screenshot of Output File](https://github.com/laramurphyyx/CA4023_Assignment1/blob/main/Part_1/Output%20Screenshots/Output_file.png)
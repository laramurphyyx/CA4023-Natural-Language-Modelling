# Assignment 1: Part 2

## Task Description

This is a language modelling exercise, which will implement an unsmoothed bigram language model.

The model should be trained on the following toy corpus:

```
'<s> a b </s>'
'<s> b b </s>'
'<s> b a </s>'
'<s> a a </s>'
```

The model should be tested against the following sentences:

```
<s> b </s>
<s> a </s>
<s> a b </s>
<s> a a </s>
<s> a b a </s>
```

## Task Implementation

This model can be implemented by using the [bigram_model.py python file](https://github.com/laramurphyyx/CA4023_Assignment1/blob/main/Part_2/bigram_model.py). This python file, when run on the command line, will request the user to enter a sentence, and will print out the probability of this sentence. 

This process can be seen in the below screenshot:

![Screenshot of Command Line](https://github.com/laramurphyyx/CA4023_Assignment1/blob/main/Part_2/Output%20Screenshots/Question1_Screenshot.png)

This python script also allows users to provide a command line argument (the name of a file) which contains a custom corpus. The custom corpus takes each line as a sentence and uses these to train the bigram language model.

This process can be seen in the below screenshot:

![Screenshot of Command Line when customised](https://github.com/laramurphyyx/CA4023_Assignment1/blob/main/Part_2/Output%20Screenshots/Custom_Corpus_Screenshot.png)

## Repository Structure

The files contained in this directory are as follows:

* <b>Output Screenshots/</b> : This is a directory containing screenshots of the model running (from the python script). There are five screenshots to show the output from running the above test sentences, and there is a screenshot to show the output from running a customised training corpus.

* <b>README.md</b> : This markdown file, which gives an introduction to the task description and outlines the implementation process.

* <b>Bigram Model Notebook.ipynb</b> : A python notebook containing the workings behind the final python script.

* <b>bigram_model.py</b> : A python script containing the bigram model.
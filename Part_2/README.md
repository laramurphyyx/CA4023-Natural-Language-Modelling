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

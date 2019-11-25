# Capstone Project 

# Machine Learning Algorithms from Scratch using Python

## Tools

* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [Numpy](https://numpy.org/)
* [Anaconda](https://www.anaconda.com/)
* [Jupyter Notebook](https://jupyter.org/)

## About

Some fundamental machine learning algorithms from scratch to understand their inner workings and maths.

## Algorithms
- K-Nearest Neighbors
- Decision Tree
- K-Means

## Datasets from UCI Machine Learning Repository
- [Breast Cancer Wisconsin](https://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+(original))
- [MONK'S problem](https://archive.ics.uci.edu/ml/datasets/MONK's+Problems)

### 1. KNN

### 2. Decision Tree
Notable Decision Tree algorithms:
* ID3 : creates multiway tree
* C4.5 : converts trained trees into if -else
* C5.0 : latest , uses less memory
* CART: support regression

###### Attribute selection at root node:
* Information Gain
* Gini Index

###### Information Gain
* Information theory:
  
  Shannon entropy: measure of uncertainty

###### Based on Probability distributions
E.g. out of 14 instances, yes=9 and no=5

    p(yes)= - (9/14) *log2(9/14) =0.41
    p(no)= - (5/14) *log2(5/14) =0.53
    E(S)=p (yes) +p(no) =0.96

Information gain is difference in entropy before and after splitting 
	                 
             = Entropy(S) - [(weighted average * Entropy(each feature)]
             = Entropy(S) - I(Attribute)

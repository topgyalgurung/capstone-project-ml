### Decision Trees - Machine Learning : IN PROGRESS 

###### Notable Decision Tree algorithms:
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
    

### Dataset: MONK dataset UCI Machine Learning Repository

* Comparison of learning algorithm: 
* Each has properties which make them hard to learn?
* Which of three problems most difficult to learn?
* Binary classification problem (class 0 or 1)

Three problems

    monk1
    monk2
    monk3 ( 5% misclassified)

##### Summary of dataset: 

dataset            | train size| class 1:class0| test size| class 1: class 0
------------------|-----------|----------|-------|------
MONK-1   | 124  | 62 : 62 |432 | 216 : 216
MONK-2   | 169 | 105 : 64 | 332 | 190 : 142
MONK-3   | 122 | 62 : 60 | 432 | 204 : 228

#### Two phase:

    1.Tree Construction
    2.Tree pruning
        a. Pre-pruning
        b. Post-pruning

#### Shannon's Information Theory: Entropy & Information Gain

Dataset                | Entropy
----------------------------|-----------------------------
MONK-1        | 1.0
MONK-2 | 0.957117428264771
MONK-3 | 0.9998061328047111

##### Information Gain for Each Attribute:
...

#### Resources: 
* [r3d3](http://www.r2d3.us/)
	1. [R3D3 - Decision Tree (Visual Introduction to ML)](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)
	2. [Bias and Variance Tradeoffs](http://www.r2d3.us/visual-intro-to-machine-learning-part-2/)

### Decision Trees - Machine Learning 

#### Dataset: MONK dataset UCI Machine Learning Repository

    Comparison of learning algorithm: 
    Which of three problems most difficult to learn?
    Binary classification problem (class 0 or 1)

Three problems

    monk1
    monk2
    monk3 ( 5% misclassified)

##### Summary of dataset: 

dataset            | train size| class 1:class0| test size| class 1: class 0
------------------|-----------|----------|-------|------
MONK-1   | 124  | 62:62 |432 | 216:216
MONK-2   | 169 | 105:64 | 332 | 190:142
MONK-3   | 122 | 62:60 | 432 | 204:228

#### Two phase:

    1.Tree Construction
    2.Tree pruning

#### Splitting Criteria

    1. Pre-pruning
    2. Post- pruning


#### Shannon's Information Theory
Entropy 
Information Gain

Dataset                | Entropy
----------------------------|-----------------------------
MONK-1        | 1.0
MONK-2 | 0.957117428264771
MONK-3 | 0.9998061328047111

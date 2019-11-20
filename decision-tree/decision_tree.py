# Topgyal Gurung
# Decision Tree Algorithm from scratch on monk dataset
import pandas as pd
import numpy as np
from pprint import pprint

# base case 
def check_purity(data):
    label_column=data[:,0]
    unique_classes=np.unique(label_column)
    if len(unique_classes)==1:
        return True
    else:
        return False

def classify_data(data):
    label_column=data[:,0]
    unique_classes,counts_unique_classes=np.unique(label_column,return_counts=True) # [0 1] , [62 62]
    index=counts_unique_classes.argmax()  # use max class as index 
    classification=unique_classes[index]
    return classification

def get_potential_splits(data):
    potential_splits={}
    _,n_columns=data.shape  #iterate over column
    for column_i in range(1,n_columns):  # column index exclude class
        values = data[:, column_i]
        unique_values = np.unique(values)
        potential_splits[column_i]=unique_values
    return potential_splits 

# split data to data equal if equal and data_not for not equal
def split_data(data,split_column,split_value):
    #random.shuffle(data)
    split_column_values=data[:,split_column]
    true_data=data[split_column_values==split_value]
    false_data=data[split_column_values!=split_value]
    return true_data,false_data  

# entropy: measure of uncertainty
def entropy(data):
    label_column=data[:,0]
    _,counts=np.unique(label_column,return_counts=True)
    
    probability=counts/counts.sum()
    entropy=sum(probability*-np.log2(probability))
    return entropy

def overall_entropy(true_data, false_data):
    n=len(true_data)+len(false_data)
    p_true_data=len(true_data)/n
    p_false_data=len(false_data)/n
    overall_entropy=(p_true_data * entropy(true_data) + p_false_data * entropy(false_data))
    return overall_entropy

def best_split(data,potential_splits):
    temp_entropy=999  #arbitary large num
    for column_index in potential_splits:
        for value in potential_splits[column_index]:
            true_data,false_data=split_data(data,split_column=column_index,split_value=value)
            #info_gain
            current_overall_entropy=overall_entropy(true_data,false_data)
            #print(current_overall_entropy)
            if current_overall_entropy<=temp_entropy:
                temp_entropy=current_overall_entropy
                best_split_column=column_index
                best_split_value=value
    return best_split_column, best_split_value

# recursive decision_tree algorithm
def decision_tree(train_set,counter=0):
    if counter==0:
        global column_headers
        column_headers=train_set.columns
        data=train_set.values  # numpy array
    else:
        data= train_set   # pandas dataframe
    
    # base case
    if check_purity(data):
        classification=classify_data(data)
        return classification
    # recursive
    else:
        counter+=1
        # run helper functions
        potential_splits=get_potential_splits(data)
        split_column,split_value=best_split(data,potential_splits)
        true_data,false_data=split_data(data,split_column,split_value)

        # sub_tree
        feature_name=column_headers[split_column]
        question="{} == {}".format(feature_name,split_value)
        sub_tree={question:[]} #empty list
        # find ans (recursive part)
        yes_ans=decision_tree(true_data,counter)
        no_ans=decision_tree(false_data,counter)
        
        if yes_ans==no_ans:
            sub_tree=yes_ans
        else:
            sub_tree[question].append(yes_ans)
            sub_tree[question].append(no_ans)

        return sub_tree

if __name__=="__main__":

    # load and prepare dataset
    # train_set
    monk1_train=pd.read_csv("/Users/topgyalgurung/Desktop/monk-dataset/train1.csv")
    monk2_train=pd.read_csv("/Users/topgyalgurung/Desktop/monk-dataset/train2.csv")
    monk3_train=pd.read_csv("/Users/topgyalgurung/Desktop/monk-dataset/train3.csv")
    # test_set
    monk1_test=pd.read_csv("/Users/topgyalgurung/Desktop/monk-dataset/test1.csv", header=None)
    monk2_test=pd.read_csv("/Users/topgyalgurung/Desktop/monk-dataset/test2.csv", header=None)
    monk3_test=pd.read_csv("/Users/topgyalgurung/Desktop/monk-dataset/test3.csv", header=None)
    monk1_tree=decision_tree(monk1_train)
    monk2_tree=decision_tree(monk2_train)
    monk3_tree=decision_tree(monk3_train)

    # drop Id 
    monk1_train=monk1_train.drop("Id", axis=1)
    monk2_train=monk2_train.drop("Id",axis=1)
    monk3_train=monk3_train.drop("Id",axis=1)

    monk1_test=monk1_test.drop([7],axis=1)
    monk2_test=monk2_test.drop([7],axis=1)
    monk3_test=monk3_test.drop([7],axis=1)

    # dataframe into numpy array
    monk1_data=monk1_train.values
    monk2_data=monk2_train.values
    monk3_data=monk3_train.values

    print("entropy of monk1:",entropy(monk1_data))
    print("entropy of monk2:",entropy(monk2_data))
    print("entropy of monk3:",entropy(monk3_data))
    
    print("MONK1 TREE:")
    pprint(monk1_tree)
    print("MONK2 TREE:")
    pprint(monk2_tree)
    print("MONK2 TREE:")
    pprint(monk3_tree)
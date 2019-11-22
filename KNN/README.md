### K Nearest Neighbor

#### Algorithm

* Prepare data, normalize first
* For splitting, data needs to be stratified
* Inverse distance: votes for test data point will be  
   weighted by inverse distance of k points closest to it.
* Split dataset for k-optimization
* Split data into train, test and validation set
* Start with k=1 and keep increasing and find accuracy
   on validation set
* Test k on validation set then use k to find accuracy
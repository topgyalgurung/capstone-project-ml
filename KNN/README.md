### K Nearest Neighbor

#### Steps

* Load data and split into train,test and valid datasets
* Calculate distance between two instances using any distance metrics that satisfies [distance function](https://en.wikipedia.org/wiki/Metric_(mathematics))
* Find k most similar instances
* Check accuracy of predictions

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

##### Misc

[Voronoi Diagram- Basic Concepts Visual Introduction](https://www.youtube.com/watch?time_continue=1&v=7eCrHAv6sYY&feature=emb_logo)

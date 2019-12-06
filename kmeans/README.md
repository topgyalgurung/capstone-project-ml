# Kmeans -  unsupervised clustering algorithm:
                    
* used in graph clustering classify similar data in groups
* pre-determined no of clusters (hyperparameter) within an unlabeled multidimensional dataset 
* use distance from center of each cluster to classify data

* k-means problem is to find cluster centers that minimize the intra-class variance,i.e. the sum of squared distances from each data point being clustered to its cluster center (the center that is closest to it)

### Assumptions:
* cluster center is arithmetic mean of all points belonging to the cluster
* each point is closer to its own cluster center than to other cluster centers

### Data preparation:
* remove class (diagnosis, last column) 
* stratify data (split into train, test and valid)
* normalize data to ensure equal weight (min-max formula)

### Steps:
* randomly pick k instances as prototypes
* pick i+1 prototype as on farthest from the first i prototypes
* use hierarchical clustering on a random sample of n instances, and use result as initial seeds
k-means ++

#### Notes:
* to avoid exhaustive search, better approach involves using expectation-maximization iterative procedure:
* E-M:
  1. guess cluster center
  2. repeat until converges:
* E- step: assign points to nearest cluster center
* M- step: set the cluster centers to the mean

### Implementations:
initialize k centroids (use mean or random)
keep split until get k
iterate through every row of data and use euclidean distance
to improve accuracy, attributes can be optimized e.g. using Pearson's Correlation Coefficient

#### Extra:

* finding optimal clustering with given k is NP-hard
* PCA-ing the data first down to a smaller dimension

* k-means++ initialization, the algorithm is guaranteed to find a solution that is O(log k) competitive to the optimal k-means solution.

* Euclidean distance is used as a metric and variance is used as a measure of cluster scatter.
* The result of k-means can be seen as the Voronoi cells of the cluster means
* K-means is closely related to nonparametric Bayesian modeling

* consider ball trees or KD-trees to speed new centroid computation
* MDL - minimum distance length stopping criteria or set k based on a knee or elbow

* tell how many clusters you expect , it can not learn no of clusters from data
* kmeans limited to linear cluster boundaries because each iteration of k-means must access every point in the dataset, the algorithm can be relatively slow as the number of samples grows.
O(n2) 

* note: kernelized k-means in Scikit-learn within SpectralClustering. 

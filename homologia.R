library(TDA)
X <- runif(200)
dim(X) <- c(100, 2)
persistence <- ripsDiag(X, maxdimension = 1, maxscale = 0.2, dist = "euclidean", library = "Dionysus", location = TRUE)


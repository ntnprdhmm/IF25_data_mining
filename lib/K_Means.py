import numpy as np
from random import randint

class K_Means:

    """ tol : how much that centroide is gona moove (tolerance)
        max_iter : how many times we wan't to run it before it's ok
    """
    def __init__(self, k=2, tol=0.001, max_iter=300):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter
        self.centroids = {}

    """ run K-Means on the given data
    """
    def fit(self, data):
        # init the centroids
        self._init_centroids_randomly(data)

        # for each iteration
        for i in range(self.max_iter):
            self.classifications = {}

            # init the classification object
            for i in range(self.k):
                self.classifications[i] = []

            # populate the list
            for feature_set in data:
                # calculate the distance between the point and each centroids
                distances = [np.linalg.norm(feature_set - self.centroids[centroid]) for centroid in self.centroids]
                # get the closest centroid
                classification = distances.index(min(distances))
                # attach the point to this centroid
                self.classifications[classification].append(feature_set)

            # save the old positions of each centroids
            prev_centroids = dict(self.centroids)

            # recalculate the position of each centroid
            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)

            optimized = True

            # for each centroid, check if it has moved
            for centroid in self.centroids:
                original_centroid = prev_centroids[centroid]
                current_centroid = self.centroids[centroid]
                if np.sum((current_centroid - original_centroid)/original_centroid * 100.0) > self.tol:
                    optimized = False

            # if nothing moved, stop
            if optimized:
                break

    """ Pick self.k points randomly in the dataset
        These points are the centroids
    """
    def _init_centroids_randomly(self, data):
        previous_random = []
        while len(self.centroids) < self.k:
            r = randint(0, len(data))
            if r not in previous_random:
                self.centroids[len(previous_random)] = data[r]
                previous_random.append(r)

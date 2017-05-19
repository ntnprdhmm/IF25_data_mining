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

    def fit(self, data):
        self._init_centroids(data)

        # for each iteration
        for i in range(self.max_iter):
            self.classifications = {}

            # for each clusters
            for i in range(self.k):
                self.classifications[i] = []

            # populate the list
            for feature_set in data:
                distances = [np.linalg.norm(feature_set - self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(feature_set)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)

            optimized = True

            for centroid in self.centroids:
                original_centroid = prev_centroids[centroid]
                current_centroid = self.centroids[centroid]
                if np.sum((current_centroid - original_centroid)/original_centroid * 100.0) > self.tol:
                    optimized = False

            if optimized:
                break


    def _init_centroids(self, data):
        previous_random = []
        while len(self.centroids) < self.k:
            r = randint(0, len(data))
            if r not in previous_random:
                self.centroids[len(previous_random)] = data[r]
                previous_random.append(r)
			
			
			
			
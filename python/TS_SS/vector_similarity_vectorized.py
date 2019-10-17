import math
import numpy as np
import torch

class TS_SS:
    
    def Cosine(self, vec1: np.ndarray, vec2: np.ndarray):
        return np.dot(vec1, vec2.T)/(np.linalg.norm(vec1) * np.linalg.norm(vec2))

    def VectorSize(self, vec: np.ndarray):
        return np.linalg.norm(vec)

    def Euclidean(self, vec1: np.ndarray, vec2: np.ndarray):
        return np.linalg.norm(vec1-vec2)

    def Theta(self, vec1: np.ndarray, vec2: np.ndarray):
        return np.arccos(self.Cosine(vec1, vec2)) + np.radians(10)

    def Triangle(self, vec1: np.ndarray, vec2: np.ndarray):
        theta = np.radians(self.Theta(vec1, vec2))
        return (self.VectorSize(vec1) * self.VectorSize(vec2) * np.sin(theta))/2

    def Magnitude_Difference(self, vec1: np.ndarray, vec2: np.ndarray):
        return abs(self.VectorSize(vec1) - self.VectorSize(vec2))

    def Sector(self, vec1: np.ndarray, vec2: np.ndarray):
        ED = self.Euclidean(vec1, vec2)
        MD = self.Magnitude_Difference(vec1, vec2)
        theta = self.Theta(vec1, vec2)
        return math.pi * (ED + MD)**2 * theta/360


    def __call__(self, vec1: np.ndarray, vec2: np.ndarray):
        return self.Triangle(vec1, vec2) * self.Sector(vec1, vec2)

# Usage
v1 = np.random.random_sample((6000, 80))
v2 = np.random.random_sample((200, 80))
similarity = TS_SS()
print(similarity(v1,v2))

# to convert to tensor
torch.tensor(similarity(v1,v2))
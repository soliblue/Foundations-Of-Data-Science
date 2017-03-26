from NearestNeighbourAlgorithm.nearestNeighbour import *


S= [([4, 4, 4], 1), ([4, -4, 4], 1), ([4.2, 3.1, 4.9], 1), ([4.6, 4.8, 3.4], 1), ([4.6, 4.8, 2.8], -1), ([0, 4.2, 3.7], -1), ([4, -1, 4.1], -1), ([6.3, 5.1, 4.2], -1), ([5, 5, 5], 1),
([4, 3, 4], 1), ([4.2, -3.1, 3.6], 1), ([2.5, 3.6, 2.5], -1), ([4.1, 4.3, -1], -1), ([-4, -4, -4], -1), ([2, 2, 2.2], -1),
([7, 4, 3], -1), ([12, 15, 6], -1), ([3.6, -4.1, 5.6], -1), ([3.1, -4.8, 4.9], 1), ([2.8, 4.6, 3.1], -1)];

D = [[4,3,3],[4,-1,1],[-2,4,5],[-2,-6,-1],[6,0,2]];

print("k = 2 & Manhattan");
print(nearest_neighbour_manhattan(2,S,D));
print("k = 3 & Manhattan");
print(nearest_neighbour_manhattan(3,S,D));
print("k = 2 & Euclidian");
print(nearest_neighbour_euclidean(2,S,D));
print("k = 3 & Euclidian")
print(nearest_neighbour_euclidean(3,S,D));


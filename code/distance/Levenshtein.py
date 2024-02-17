import numpy as np

class LevenshteinDistance:
    def __init__(self) -> None:
        raise NotImplementedError('Use as Static Class, Call Methods by Class Name')

    def calculateDistance(str1, str2):
        LEN_1 = len(str1) + 1
        LEN_2 = len(str2) + 1
        distance_matrix = LevenshteinDistance._build_distance_matrix(LEN_1, LEN_2)
        for i in range(1, LEN_1, 1):
            for j in range(1, LEN_2, 1):
                local_min = min(distance_matrix[i-1, j], distance_matrix[i, j-1],distance_matrix[i-1][j-1])
                distance_matrix[i, j] = distance_matrix[i-1][j-1] if str1[i-1] == str2[j-1] else local_min + 1
        return (distance_matrix[LEN_1 - 1][LEN_2 - 1], distance_matrix)

    def _build_distance_matrix(LEN_1, LEN_2):
        dm = np.full((LEN_1, LEN_2), max(LEN_1, LEN_2))
        for i in range(LEN_1):
            dm[i][0] = i
        for j in range(LEN_2):
            dm[0][j] = j
        return dm
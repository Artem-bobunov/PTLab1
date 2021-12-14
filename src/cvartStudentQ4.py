import numpy as np
from typing import Dict, List

RatingType = Dict[str, float]


class GetStudents4Q():

    def __init__(self, rating: RatingType) -> None:
        self.rating: RatingType = rating
        self.studetsq4: RatingType = {}

    def get(self) -> RatingType:
        rating_list = list(self.rating.values())
        four_quartile = np.quantile(rating_list, 1)
        median = np.quantile(rating_list, 0.75)
        for key in self.rating:
            if median <= self.rating[key] <= four_quartile:
                self.studetsq4[key] = float(self.rating[key])
        return self.studetsq4
    #люблю сосать
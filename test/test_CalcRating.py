from typing import Dict, Tuple
from Types import DataType
from CalcRating import CalcRating
import pytest
RatingsType = Dict[str, float]


class TestCalcRating():
    @pytest.fixture()
    def input_data(self) -> Tuple[DataType, RatingsType]:
        data: DataType = {
            "Иванов Иван Иванович":
            [
                ("математика", 100),
                ("русский язык", 100),
                ("программирование", 100)
            ],
            "Петров Петр Петрович":
            [
                ("математика", 61),
                ("русский язык", 76),
                ("программирование", 76),
                ("литература", 76)
            ]
        }
        rating_scores: RatingsType = {
            "Иванов Иван Иванович": 100.0,
            "Петров Петр Петрович": 72.25
        }
        return data, rating_scores

    def test_init_calc_rating(self, input_data:
                              Tuple[DataType, RatingsType]) -> None:
        calc_rating = CalcRating(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data:
                  Tuple[DataType, RatingsType]) -> None:
        rating = CalcRating(input_data[0]).calc()
        for student in rating.keys():
            rating_score = rating[student]
            assert pytest.approx(
                rating_score, abs=0.001) == input_data[1][student]
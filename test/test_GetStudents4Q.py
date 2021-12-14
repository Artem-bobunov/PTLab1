from typing import Dict, Tuple
from Types import DataType
from CalcRating import CalcRating
from cvartStudentQ4 import GetStudents4Q
import pytest
RatingsType = Dict[str, float]


class TestStudents3Q():
    @pytest.fixture()
    def input_data(self) -> Tuple[DataType, RatingsType]:
        rating_scores: RatingsType = {
            'Иванов Иван Иванович': 82.0,
            'Бобунов1 Петр Петрович': 63.333333333333336,
            'Бобунов2 Петр Петрович': 76.0,
            'Бобунов3 Петр Петрович': 89.33333333333333,
        }
        student_list: RatingsType = {
            'Иванов Иван Иванович': 82.0,
            'Бобунов3 Петр Петрович': 89.33333333333333
        }
        return rating_scores, student_list

    def test_init_get_students_3q(self, input_data:
                                  Tuple[RatingsType, RatingsType]) -> None:
        rating_scores = GetStudents4Q(input_data[0])
        assert input_data[0] == rating_scores.rating

    def test_get(self, input_data:
                 Tuple[DataType, RatingsType]) -> None:
        student_list = GetStudents4Q(input_data[0]).get()
        for student in student_list.keys():
            rating = student_list[student]
            assert pytest.approx(
                rating, abs=0.001) == input_data[1][student]

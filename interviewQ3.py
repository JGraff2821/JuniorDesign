from random import uniform
from typing import Tuple


# Function gives a random coordinate within a circle of radius one.
def random_coordinate() -> Tuple[float, float]:
    return uniform(0, 1), uniform(0, 1)


def calculate_pi(number_of_points: int):
    # Variable to track in/out of circle.
    points_in_circle: int = 0

    for point in range(number_of_points):

        # Find a point, within the given quadrant
        new_point = random_coordinate()

        # Check to see if that point is within the circle.
        # This is done by using the distance formula (in circle if distance is less than equal one)
        in_circle = new_point[0] * new_point[0] + new_point[1] * new_point[1] <= 1
        # Keep track of which points are in, which are out.
        if in_circle:
            points_in_circle += 1
    # Points in divided by the total points is an estimate of the area of the quarter circle divided by the area of
    # the quadrant (in/total)  estimates to (PI/4 *r^2)/(r^2) **Side length of square is r.
    points_in_over_total: float = points_in_circle/number_of_points
    # from algebra, PI estimates to 4(in/out)
    pi: float = 4*points_in_over_total
    return pi


if __name__ == '__main__':
    print(calculate_pi(10000000))


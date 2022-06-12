from exceptions import SubtractionBelowZeroError


class StLb:

    def __init__(self, stones_lbs):
        self.in_lbs = self._convert_stones_and_lbs_to_lbs(stones_lbs)
        self.whole_stones, self.remainder_lbs = self._convert_lbs_to_stones_and_lbs(
            self.in_lbs
        )

    def _convert_lbs_to_stones_and_lbs(self, lbs):
        whole_stones = lbs // 14
        remainder_lbs = lbs % 14
        return whole_stones, remainder_lbs

    def _convert_stones_and_lbs_to_lbs(self, stones_and_lbs):
        in_lbs = (stones_and_lbs[0] * 14) + stones_and_lbs[1]
        return (in_lbs)

    def __add__(self, other):
        """
        Accepts another StLb object, or a tuple / list in the format (whole_stones, remainder_lbs).
        """
        if not isinstance(other, StLb):
            other_in_lbs = self._convert_stones_and_lbs_to_lbs(other)
            new_in_lbs = other_in_lbs + self.in_lbs
            return StLb([0, new_in_lbs])

        else:
            total = self.in_lbs + other.in_lbs
            return StLb([0, total])

    def __sub__(self, other):
        """
        Accepts another StLb object, or a tuple / list in the format (whole_stones, remainder_lbs).
        """
        if not isinstance(other, StLb):
            other_in_lbs = self._convert_stones_and_lbs_to_lbs(other)
        else:
            other_in_lbs = other.in_lbs

        # Check that the new value is not negative, which isn't allowed
        updated_in_lbs = self.in_lbs - other_in_lbs
        if updated_in_lbs < 0:
            raise SubtractionBelowZeroError

        return StLb(self._convert_lbs_to_stones_and_lbs(updated_in_lbs))

    def __str__(self):
        return f"StLb object: {self.whole_stones} stones and {self.remainder_lbs} lbs [{self.in_lbs} lbs]"

    def __repr__(self):
        return f"StLb object: {self.whole_stones} stones and {self.remainder_lbs} lbs [{self.in_lbs} lbs]"

class StLb:
    def __init__(self, stones_lbs):
        if stones_lbs[0] == 0 and stones_lbs[1] >= 14:
            self.whole_stones, self.remainder_lbs = self._convert_lbs_to_stones_and_lbs(stones_lbs[1])
        else:
            self.whole_stones = stones_lbs[0]
            self.remainder_lbs = stones_lbs[1]
        self.in_lbs = (self.whole_stones * 14) + self.remainder_lbs

    def _convert_lbs_to_stones_and_lbs(self, lbs):
        whole_stones = lbs // 14
        remainder_lbs = lbs % 14
        return whole_stones, remainder_lbs

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        def calc(start1, duration1, start2, duration2):
            min_end = min(s + d for s, d in zip(start1, duration1))

            return min(
                max(s, min_end) + d
                for s, d in zip(start2, duration2)
            )

        land_to_water = calc(
            landStartTime, landDuration,
            waterStartTime, waterDuration
        )

        water_to_land = calc(
            waterStartTime, waterDuration,
            landStartTime, landDuration
        )

        return min(land_to_water, water_to_land)
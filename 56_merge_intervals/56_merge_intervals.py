class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # First, sort the intervals by their start times
        intervals.sort(key=lambda x: x[0])

        merged_intervals = [intervals[0]]  # Initialize the answer list with the first interval

        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            previous_interval = merged_intervals[-1]  # Get the last interval in the answer list

            # Check if the current interval overlaps with the last interval in the answer list
            if current_interval[0] <= previous_interval[1]:
                # If there is an overlap, merge the intervals
                merged_intervals[-1] = [previous_interval[0], max(previous_interval[1], current_interval[1])]
            else:
                # If there is no overlap, add the current interval to the answer list
                merged_intervals.append(current_interval)

        return merged_intervals

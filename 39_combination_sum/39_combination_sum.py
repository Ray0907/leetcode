class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backTrack(remain, current, start):
            if remain < 0:
               return 
            elif remain == 0:
                result.append(list(current))
            else:
                for i in range(start, len(candidates)):
                    current.append(candidates[i])
                    backTrack(remain - candidates[i], current, i)
                    # 條件不符合所以把最後一個拿掉
                    current.pop()
        backTrack(target, [], 0)
        return result

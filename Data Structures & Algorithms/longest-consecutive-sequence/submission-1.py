class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = sorted(list(set(nums)))

        max = 0
        current = 1

        if len(numbers) == 0:
            return 0
        elif len(numbers) == 1:
            return 1
        
        prev = numbers[0]
        for num in numbers[1:]:
            if num == prev + 1:               
                current += 1
            elif current > max:
                max = current
                current = 1
            else:
                current = 1
            
            prev = num

        if current > max:
                max = current
        
        return max



        
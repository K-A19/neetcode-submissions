class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else: 
                count[num] = 1
        
        numbers = sorted(list(count), key=lambda x: count[x], reverse=True)

        answer = []

        for i in range(k):
            answer.append(numbers[i])

        return answer


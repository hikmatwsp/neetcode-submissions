class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        answer = []
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] +=1
        values  = sorted(list(set((freq.values()))))[::-1]
        print(values)
        for i in values:
            for j in freq:
                if freq[j] == i:
                    answer.append(j)
            if len(answer) == k:
                break
        return answer
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ocurrencies = {}
        # Group & count the ocurencies with such list
        for num in nums:
            if num in ocurrencies.keys():
                ocurrencies[num] = ocurrencies[num] + 1
                continue
            ocurrencies[num] = 1
        # Sort and slice the grouped ocurrencies by "k"
        ocurrencies_sorted = sorted(ocurrencies.items(), key=lambda x: x[1], reverse=True)
        top_k = [i for i, _ in ocurrencies_sorted][:k:]
        return top_k
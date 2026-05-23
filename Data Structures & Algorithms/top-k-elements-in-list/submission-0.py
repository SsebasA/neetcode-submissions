class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsmp = {}
        res = []

        for num in nums:
            if num not in hsmp:
                hsmp[num] = 1
            else:
                hsmp[num] += 1

        while k > 0:
            max_val = max(hsmp.values())

            key = self.findK(hsmp, max_val)
            res.append(key)
            del hsmp[key]
            k -= 1

        return res

    def findK(self, hsmp, max_val) -> string:
        for k in hsmp.keys():
            if hsmp[k] == max_val:
                return k
                break

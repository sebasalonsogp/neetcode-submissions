class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0
        window = []

        for r in range(len(arr)):
            window.append(arr[r])

            if len(window) > k:
                window.pop(0)

            if len(window) == k and sum(window) / k >= threshold:
                cnt += 1

        return cnt
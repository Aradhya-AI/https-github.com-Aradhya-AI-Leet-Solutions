class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        from collections import deque

        n = len(nums)
        dq = deque()
        j = n - 1
        cost = 0
        ans = 0

        for i in range(n - 1, -1, -1):
            num = nums[i]

            while dq and nums[dq[-1]] < num:
                left = dq.pop()
                right = dq[-1] if dq else j + 1
                cost += (right - left) * (num - nums[left])

            dq.append(i)

            while cost > k:
                cost -= nums[dq[0]] - nums[j]

                if dq[0] == j:
                    dq.popleft()

                j -= 1

            ans += j - i + 1

        return ans
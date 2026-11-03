class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1

        cnt = [0] * 32

        for num in nums:
            cnt[num.bit_length() - 1] += 1

        operations = 0

        for i in range(31):
            if (target >> i) & 1:
                if cnt[i] == 0:
                    j = i + 1

                    while cnt[j] == 0:
                        j += 1

                    while j > i:
                        cnt[j] -= 1
                        cnt[j - 1] += 2
                        operations += 1
                        j -= 1

                cnt[i] -= 1

            cnt[i + 1] += cnt[i] // 2
            cnt[i] %= 2

        return operations

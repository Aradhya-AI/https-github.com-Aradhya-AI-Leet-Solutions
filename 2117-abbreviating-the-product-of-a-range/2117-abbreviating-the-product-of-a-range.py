class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        cnt2 = cnt5 = 0

        for x in range(left, right + 1):
            temp = x

            while temp % 2 == 0:
                cnt2 += 1
                temp //= 2

            while temp % 5 == 0:
                cnt5 += 1
                temp //= 5

        zeros = min(cnt2, cnt5)
        cnt2 = cnt5 = zeros

        suffix = 1
        prefix = 1.0
        large = False

        for x in range(left, right + 1):
            suffix *= x

            while cnt2 > 0 and suffix % 2 == 0:
                suffix //= 2
                cnt2 -= 1

            while cnt5 > 0 and suffix % 5 == 0:
                suffix //= 5
                cnt5 -= 1

            if suffix >= 10**10:
                large = True
                suffix %= 10**10

            prefix *= x

            while prefix >= 10**5:
                prefix /= 10

        if large:
            return str(int(prefix)) + "..." + str(suffix % 10**5).zfill(5) + "e" + str(zeros)

        return str(suffix) + "e" + str(zeros)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        '''
        plant the flowers and return how many are left

        '''

        res = n
        prev = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and prev == 0:
                if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    res -= 1

            prev = flowerbed[i]

        return res <= 0
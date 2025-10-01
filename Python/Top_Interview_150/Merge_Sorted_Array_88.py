class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        pointer = (m + n ) - 1
        pointer1 = m - 1
        pointer2 = n - 1

        for i in range(pointer, -1, -1):
            if pointer2 < 0:
                break
            if pointer1 < 0 :
                nums1[pointer] = nums2[pointer2]
                pointer -= 1
                pointer2 -= 1
            elif nums1[pointer1] >= nums2[pointer2]:
                nums1[pointer] = nums1[pointer1]
                pointer -= 1
                pointer1 -= 1
            else:
                nums1[pointer] = nums2[pointer2]
                pointer -= 1
                pointer2 -= 1




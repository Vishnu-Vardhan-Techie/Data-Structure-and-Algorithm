class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def update(self, index: int, val: int) -> None:

        diff = val - self.nums[index]
        self.nums[index] = val

        for i in range(index + 1, len(self.prefix)):
            self.prefix[i] += diff

    def sumRange(self, left: int, right: int) -> int:

        return self.prefix[right + 1] - self.prefix[left]

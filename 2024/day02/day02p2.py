bad = []


def check_valid(nums):
    nums_augmenting = nums.copy()
    nums_augmenting.sort()

    nums_decreasing = nums.copy()
    nums_decreasing.sort(reverse=True)

    if nums_augmenting == nums or nums_decreasing == nums:
        valid = True
        for idx, num in enumerate(nums):
            if idx < len(nums) - 1:
                if abs(num - nums[idx + 1]) > 3 or abs(num - nums[idx + 1]) < 1:
                    valid = False
        return valid


with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

    count = 0

    for line in lines:
        nums = list(map(int, line.split()))

        if check_valid(nums):
            count += 1
        else:
            for idx, num in enumerate(nums):
                new_nums = nums.copy()
                new_nums = new_nums[:idx] + new_nums[idx + 1:]

                if check_valid(new_nums):
                    count += 1
                    break

    print(count)

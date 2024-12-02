with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

    count = 0

    for line in lines:
        nums = list(map(int, line.split()))

        nums_augmenting = nums.copy()
        nums_augmenting.sort()

        nums_decreasing = nums.copy()
        nums_decreasing.sort(reverse=True)

        # print(nums)
        if nums_augmenting == nums or nums_decreasing == nums:
            valid = True
            for idx, num in enumerate(nums):
                if idx < len(nums) - 1:
                    if abs(num - nums[idx + 1]) > 3 or abs(num - nums[idx + 1]) < 1:
                        valid = False
            if valid:
                print(valid)
                count += 1

    print(count)

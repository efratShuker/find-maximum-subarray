def maxSumOfArr(array):
    all_elements_are_negative = max(array)
    if all_elements_are_negative < 0:
        return all_elements_are_negative
    max_of_subarray = 0
    max_of_current_subarray = 0
    for i in range(len(array)):
        max_of_current_subarray += array[i]
        if max_of_current_subarray < 0:
            max_of_current_subarray = 0
        max_of_subarray = max(max_of_current_subarray, max_of_subarray)
    return max_of_subarray


def main():
    print(maxSumOfArr([1, -9, 20, -9, 17, -5]))


if __name__ == '__main__':
    main()

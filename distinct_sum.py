def sum_distinct_elements(set1, set2):
    sum = 0
    # Check elements in set1 not in set2
    for x in set1:
        if x not in set2:
            sum += x
    # Check elements in set2 not in set1
    for y in set2:
        if y not in set1:
            sum += y
    return sum

def test_distinct_sum():
    set1 = [3, 1, 7, 9]
    set2 = [2, 4, 1, 9, 3]
    result = sum_distinct_elements(set1, set2)
    print(f"Actual sum: {result}")  # Debug output
    assert result == 13, f"Test case failed: expected 13, got {result}"
    print("Test passed: Sum of distinct elements is 13")

if __name__ == "__main__":
    test_distinct_sum()
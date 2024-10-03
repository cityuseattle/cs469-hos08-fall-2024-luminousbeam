
# Fractional Knapsack Problem

def maxValue(capacityW, weights, values):
    answer = 0
    # zip(weights, values) = [[weights[0], values[0]], [weights[1], values[1]], ...]
    # -x[1] / x[0]  = -(value / weight)  Return negative numbers to sort in descending order
    for w, v in sorted(zip(weights, values), key=lambda x: -x[1] / x[0]):
        if capacityW == 0:
            break
        if w <= capacityW:
            '''
            Please fill in your answer to replace the "?" in the code block
            '''
            answer += ?
            capacityW = ?
        else:
            answer += ?
            capacityW = ?
    return answer


# Test case #1: output = 240.0
print(maxValue(
    50,
    [10, 20, 30],
    [60, 100, 120]
))

# Test case #2: output = 178.57142857142856
print(maxValue(
    10,
    [6, 7, 3],
    [110, 120, 2]
))

# Test case #3: output = 440.0
print(maxValue(
    60,
    [40, 10, 20, 24],
    [280, 100, 120, 120]
))

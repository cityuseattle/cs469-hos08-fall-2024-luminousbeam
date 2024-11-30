# Activity Selection Problem

def activity_selection(start, end):
  n = len(start)
  if n == 0:
    return []
  start, end, actID = zip(*sorted(zip(start, end, range(n)), key=lambda x: x[1]))
  i, answer = 0, [actID[0]]

  for j in range(n):
    if start[j] >= end[i]:
      answer.append(actID[j])
      i = j

  return answer

# Test case #1: output = [0,1,2,6]
print(activity_selection([0,3,4,2,5,3,9,11,10], [3,4,6,8,9,12,13,14,15]))

# Test case #2: output = [0,1,3,4]
print(activity_selection([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))

# Test case #3: output = [1,4,0]
print(activity_selection([4, 0, 1, 1, 3], [6, 2, 3, 6, 4]))
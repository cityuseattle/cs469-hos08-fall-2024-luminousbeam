# Maximizing Number of Tasks

def maximize_tasks(A, T):
  current_time, num_of_tasks = 0, 0
  A.sort()
  for i in range(len(A)):
    current_time += A[i]
    if current_time + A[i] >= T:
      break
    num_of_tasks += 1
  return num_of_tasks

# Test case #1: output = 3 (1,2,2÷)
print(maximize_tasks([4,2,1,2,5], 8))

# Test case #2: output = 5 (1,2,3,4,5,7)
print(maximize_tasks([3,1,7,4,9,2,5], 23))
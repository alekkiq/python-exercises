# 4
def sum_of_list(list : list):
    sum = 0

    for i in list:
        sum += i
    
    return sum

def main():
    test_cases = [
        [1, 2, 3, 10, 50],   # expected => 66
        [0, 0, -1, -50, 10], # expected => -41
        [0, 0, 0, 0, 0],     # expected => 0
    ]

    for test in test_cases:
        print(sum_of_list(test))

main()
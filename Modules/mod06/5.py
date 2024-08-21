# 5
def filter_odd_numbers(list : list):
    if len(list) == 0:
        return "The given list is empty!"
    
    filtered_list = []
    
    for i in list:
        if i % 2 == 0 or i == 0:
            filtered_list.append(i)

    return filtered_list

def main():
    test_cases = [
        [1, 2, 2, 3, 5, 10, 2951, 0],   # expected => [2, 2, 10, 0]
        [-1, -20, 10, -40, -51]         # expected => [-20, 10, -40]
    ]

    for test in test_cases:
        print(filter_odd_numbers(test))

main()
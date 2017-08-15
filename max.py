def my_max(*args):
    if len(args) == 1:
        array = args[0]
    else:
        array = args
    max_value = array[0]
    for element in array:
        if max_value <= element:
            max_value = element
    return max_value

if __name__ == '__main__':
    print(my_max(1, 2, 4, 0))
    print(my_max([1, 2, 4, 0]))
    print(my_max('Python'))

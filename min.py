def my_min(*args):
    if len(args) == 1:
        array = args[0]
    else:
        array = args
    min_value = array[0]
    for element in array:
        if min_value >= element:
            min_value = element
    return min_value

if __name__ == '__main__':
    print(my_min(1, 2, 4, 0))
    print(my_min([1, 2, 4, 0]))
    print(my_min('Python'))

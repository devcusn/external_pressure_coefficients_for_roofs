def control_range(number):
    numbers = [-45, -30, -15, -5, 5, 15, 30, 45, 60, 75]
    try:
        index = numbers.index(number)
        return [number,number,True]
        
    except ValueError:
        print('hello')
        for i, num in enumerate(numbers):
            if num <= number <= numbers[i + 1]:
                return [num, numbers[i + 1],False]
        
    
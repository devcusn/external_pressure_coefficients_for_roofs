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
            
def ratio_proportion(num1, num2, num3, num4,ran):
    range1 = ran[0]
    difference = num1 - num2
    inc_or_dic = 'dec' if num1 > num2 else 'inc'
    if (inc_or_dic == 'dec'):
        dec = (num4-range1) * abs(difference) / num3
        return num1 - dec
    inc = (num4-range1) * abs(difference) / num3
    return num1 + inc
    

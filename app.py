import json

file_path = 'datas/for_double_slope_roofs/external_pressure_coefficients_0_angle.json'
file_path_2 = 'datas/for_double_slope_roofs/external_pressure_coefficients_90_angle.json'

with open(file_path, 'r') as file:
    json_data_0_angle = json.load(file)
with open(file_path_2, 'r') as file:
    json_data_90_angle = json.load(file)

json_data_0_angle_obj = json.loads(json.dumps(json_data_0_angle))
json_data_90_angle_obj = json.loads(json.dumps(json_data_90_angle))

def control_range(number):
    numbers = [-45, -30, -15, -5, 5, 15, 30, 45, 60, 75]

    for i, num in enumerate(numbers):
        if num <= number <= numbers[i + 1]:
            return [num, numbers[i + 1]]

def ratio_proportion(num1,num2,num3,num4):
    difference = num1 - num2 
    inc_or_dic = 'dec' if num1 > num2 else 'inc'
    if(inc_or_dic == 'dec'):
        dec = num4 * abs(difference) / num3
        return  num1 - dec
    inc = num4 * abs(difference) / num3
    return  num1 + inc

def find_parameter(wind_directory, wind_angle):
    datas = json_data_90_angle_obj if wind_directory == 90 else json_data_0_angle_obj
    [x,y] = control_range(wind_angle)
    x_data = datas['+' + str(x) if x > 0 else str(x)]
    y_data = datas['+' + str(y) if x > 0 else str(y)]
    
    diference = abs(y-x)

    f = ratio_proportion(x_data['f']['c_pe_10'],y_data['f']['c_pe_10'],diference,wind_angle)
    g = ratio_proportion(x_data['g']['c_pe_10'],y_data['g']['c_pe_10'],diference,wind_angle)
    h = ratio_proportion(x_data['h']['c_pe_10'],y_data['h']['c_pe_10'],diference,wind_angle)
    i = ratio_proportion(x_data['i']['c_pe_10'],y_data['i']['c_pe_10'],diference,wind_angle)
    j = ratio_proportion(x_data['j']['c_pe_10'],y_data['j']['c_pe_10'],diference,wind_angle)
    return {"f": f, "g": g, "h": h, "i": i, "j": j}


res = find_parameter(wind_directory=0, wind_angle=15)

print(res)
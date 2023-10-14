import json
from helper import control_range,ratio_proportion

file_path = 'datas/for_double_slope_roofs/external_pressure_coefficients_0_angle.json'
file_path_2 = 'datas/for_double_slope_roofs/external_pressure_coefficients_90_angle.json'

with open(file_path, 'r') as file:
    json_data_0_angle = json.load(file)
with open(file_path_2, 'r') as file:
    json_data_90_angle = json.load(file)

json_data_0_angle_obj = json.loads(json.dumps(json_data_0_angle))
json_data_90_angle_obj = json.loads(json.dumps(json_data_90_angle))

def find_parameters_90_directory(x_data, y_data, diference, wind_angle, ran):
    z = ran[2]
    f = x_data['f']['c_pe_10'] if z else ratio_proportion(
        x_data['f']['c_pe_10'], y_data['f']['c_pe_10'], diference, wind_angle,ran)
    g = x_data['g']['c_pe_10'] if z else ratio_proportion(
        x_data['g']['c_pe_10'], y_data['g']['c_pe_10'], diference, wind_angle,ran)
    h = x_data['h']['c_pe_10'] if z else ratio_proportion(
        x_data['h']['c_pe_10'], y_data['h']['c_pe_10'], diference, wind_angle,ran)
    i = x_data['i']['c_pe_10'] if z else ratio_proportion(
        x_data['i']['c_pe_10'], y_data['i']['c_pe_10'], diference, wind_angle,ran)
    return {"f": f, "g": g, "h": h, "i": i}


def find_parameters_0_directory(x_data, y_data, diference, wind_angle, ran):
    z = ran[2]
    f =x_data['f']['c_pe_10'] if z else ratio_proportion(x_data['f']['c_pe_10'],
                         y_data['f']['c_pe_10'], diference, wind_angle,ran)
    g =x_data['g']['c_pe_10'] if z else ratio_proportion(x_data['g']['c_pe_10'],
                         y_data['g']['c_pe_10'], diference, wind_angle,ran)
    h =x_data['h']['c_pe_10'] if z else ratio_proportion(x_data['h']['c_pe_10'],
                         y_data['h']['c_pe_10'], diference, wind_angle,ran)
    i =x_data['i']['c_pe_10'] if z else ratio_proportion(x_data['i']['c_pe_10'],
                         y_data['i']['c_pe_10'], diference, wind_angle,ran)
    j =x_data['j']['c_pe_10'] if z else ratio_proportion(x_data['j']['c_pe_10'],
                         y_data['j']['c_pe_10'], diference, wind_angle,ran)
    return {"f": f, "g": g, "h": h, "i": i, "j": j}


def find_parameter(wind_directory, wind_angle):
    datas = json_data_90_angle_obj if wind_directory == 90 else json_data_0_angle_obj
    [x, y, z] = control_range(wind_angle)
    x_data = datas['+' + str(x) if x > 0 else str(x)]
    y_data = datas['+' + str(y) if x > 0 else str(y)]
    diference = abs(y-x)
    if (wind_directory == 90):
        return find_parameters_90_directory(x_data, y_data, diference, wind_angle, [x,y,z])
    elif (wind_directory == 0):
        return find_parameters_0_directory(x_data, y_data, diference, wind_angle, [x,y,z])


res = find_parameter(wind_directory=90, wind_angle=-33)

print(res)

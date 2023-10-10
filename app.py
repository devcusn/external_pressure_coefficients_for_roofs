
external_pressure_coefficients = {
    "-45":{
        "f": {"c_pe_10":-0.6,"c_p_1":-0.6},
        "g": {"c_pe_10":-0.6,"c_p_1":-0.6},
        "h": {"c_pe_10":-0.6,"c_p_1":-0.6},
        "i": {"c_pe_10":-0.6,"c_p_1":-0.6},
        "j": {"c_pe_10":-0.6,"c_p_1":-0.6},
    }
}





def find_parameter():
    f = None
    g = None
    h = None
    i = None
    j=None
    return {"f": f,"g":g,"h":h,"i":i,"j":j}

find_parameter(wind_directory = 90,wind_angle=8)
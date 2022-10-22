import dcalc


def create_list(*args, **kwargs):
    response = []
    
    for idx, value in enumerate(args):
        response.append(f"Point_{idx} = {dcalc.deg_to_gms(value)}")
    
    for k, v in kwargs.items():
        response.append(f"{k} = {dcalc.deg_to_gms(v)}")
    
    return response


print(create_list(172.25899161, 321.42304971, 12.697987681352, pole=21.89617856, put_1=140.85706440))
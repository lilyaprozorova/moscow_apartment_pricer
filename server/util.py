import pickle
import json
import numpy as np
import sklearn

__categories = None
__data_columns = None
__model = None
__scaler = None

def get_estimated_price(
        house_age, dist_to_subway, subway_type, rooms, footage,
        floor, max_floor,
        distance_to_center, area, material
):
    area = __categories["areas"][area]
    print(area)
    material = __categories["materials"][material]
    print(material)
    try:
        area_index = __data_columns.index("area_" + area.lower)
    except:
        print("Area not found")
        area_index = -1
    try:
        material_index = __data_columns.index("material_" + material)
    except:
        print("Material not found")
        material_index = -1
    try:
        subtype_index = __data_columns.index("subway_type_" + subway_type)
    except:
        print("Subtype not found")
        subtype_index = -1

    x = np.zeros(len(__data_columns))
    is_last_floor = (floor == max_floor)
    is_first_floor = (floor == 1)
    x[0:9] = [house_age, dist_to_subway, rooms, footage,
               floor, max_floor, is_first_floor, is_last_floor,
               distance_to_center]
    if area_index >= 0:
        x[area_index] = 1
    if material_index >= 0:
        x[material_index] = 1
    if subtype_index >= 0:
        x[subtype_index] = 1
    

    return round(__model.predict(__scaler.transform([x]))[0] * 10000000,2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __categories

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
    with open("./artifacts/categories.json", "r") as f:
        __categories = json.load(f)


    global __model
    global __scaler
    if __model is None:
        with open('./artifacts/moscow_apartment_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    if __scaler is None:
        with open('./artifacts/moscow_apartment_scaler.pickle', 'rb') as f:
            __scaler = pickle.load(f)
    print("loading saved artifacts...done")

def get_categories_names():
    return {
        "areas" : list(__categories["areas"].keys()),
        "materials" : list(__categories['materials'].keys())
    }

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_categories_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location
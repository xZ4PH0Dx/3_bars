import json
path='./1796'
dic={}
def load_data(filepath):
    with open(filepath,'r') as f:
        json_str=json.loads(f.read())
        return json_str

def get_name_seats(json_str):
    for i in json_str['features']:
        dic[str(i['properties']['Attributes']['Name'])] = i['properties']['Attributes']['SeatsCount']
    return dic

def get_biggest_bar(data):
    dic=get_name_seats(load_data(path))
    return (str({k for k, v in dic.items() if v == max(dic.values())}))

def get_smallest_bar(data):
    dic=get_name_seats(load_data(path))
    return (str({k for k, v in dic.items() if v == min(dic.values())}))

def get_closest_bar(data, longitude, latitude):
    user_loc=[int(str(longitude).replace('.','')),int(str(latitude).replace('.',''))]
    for i in load_data(path)['features']:
        dic[str(i['properties']['Attributes']['Name'])] =\
            abs(abs(int(str(i['geometry']['coordinates'][0]).replace('.',''))-user_loc[0])-
                 abs(int(str(i['geometry']['coordinates'][1]).replace('.',''))-user_loc[1]))
    return(str({k for k,v in dic.items() if v == min(dic.values())}))

if __name__ == '__main__':
    longitude,latitude = [int(x) for x in input("Введите долготу и широту: ").split()]
    print('Самый большой бар: ',get_biggest_bar(path))
    print('Самый маленький бар: ',get_smallest_bar(path))
    print('Ближайший бар: ',get_closest_bar(path,longitude,latitude))



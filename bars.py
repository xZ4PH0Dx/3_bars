import json
path='./1796'
dic={}
def load_data(filepath):
    with open(filepath,'r') as f:
        return json.loads(f.read())

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
    choice = int(input("""Что Вы хотите найти?
          1) Самый большой бар
          2) Самый маленький бар
          3) Ближайший бар
          """))
    if choice == 1:
        print('Самый большой бар(ы): ', str(get_biggest_bar(path)).replace('{','').replace('}',''))
    if choice == 2:
        print('Самый маленький бар(ы): ', str(get_smallest_bar(path)).replace('{','').replace('}',''))
    if choice == 3:
        try:
            longitude,latitude = [float(x) for x in input("Введите долготу и широту(только цифры и" +
                                                                "разделительные точки): ").split()]
            print('Ближайший бар: ',str(get_closest_bar(path,longitude,latitude)).replace('{','').replace('}',''))
        except ValueError:
            print('Не правильно введены данные')



import pandas as pd
from geopy.geocoders import Nominatim
import folium
geo_local = Nominatim(user_agent='South Korea')

def real_address(filtered_data): #위치를 받아서 아래 geocoding에 넣기위해 표를 정제함
    
    if filtered_data is not None:
        address = filtered_data['위치']
        modified_addresses = []
        for i in address:
            a = i.split(' ')
            modified_address = " ".join(a[:4])
            modified_addresses.append(modified_address)
        return modified_addresses
    else:
        return None
def geocoding(address): #도로명주소를 위도 경도 값으로 바꿔주기
    try:
        geo = geo_local.geocode(address)
        x_y = [geo.latitude, geo.longitude]
        return x_y

    except:
        return [0,0]
    
def phone_number(filtered_data):
    if filtered_data is not None:
        phone_numbers = filtered_data['전화번호']
        modified_numberses = []
        for i in phone_numbers:
            a = i.split(' ')
            modified_numbers = " ".join(a[:4])
            modified_numberses.append(modified_numbers)
        return modified_numberses
    else:
        return None
    
def facility_name(filtered_data):
    if filtered_data is not None:
        facility_names = filtered_data['시설']
        modified_nameses = []
        for i in facility_names:
            a = i.split(' ')
            modified_names = " ".join(a[:4])
            modified_nameses.append(modified_names)
        return modified_nameses
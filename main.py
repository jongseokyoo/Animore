from typing import List
import pandas as pd
from geopy.geocoders import Nominatim
import folium
# 제작한 Class들 import
from Pet_Customer_Class import Pet, Customer 
from Savesystem_Class import SaveSystem
from AppointSystem_Class import AppointSystem
from ReviewSystem_Class import ReviewSystem
from Ceneter_Class import Center

from folium_func import real_address, geocoding, phone_number, facility_name
def main():
    customer1 = Customer()
    print(customer1)
    file_path = "C:\\Users\\monog\\OneDrive\\바탕 화면\\Python_Project\\Animore\\center.csv"
    save_list = SaveSystem(file_path)
    find_address = customer1.contact_SaveSys()
    result = save_list.filter_data_by_region(find_address)
    center_list = result.values.tolist()
    print(center_list)
    address1 = real_address(result)
    if not result.empty: #결과값이 비지 않았다면 전화번호만 따로 저장하는 부분.
        phone_numbers = phone_number(result)
        facility_names = facility_name(result)
    
    latitude = []
    longitude =[]

    for i in address1:
        latitude.append(geocoding(i)[0])
        longitude.append(geocoding(i)[1])
    hospital_locations = []
    for lat, lon in zip(latitude, longitude):
        hospital_locations.append([lat, lon])
        

    m = folium.Map(location=[37.53897093698831, 127.05461953077439], 
               zoom_start=12, 
               )
    for i in range(len(hospital_locations)):
        folium.Marker(location=hospital_locations[i], tooltip = f"{facility_names[i]} {phone_numbers[i]}").add_to(m)
    m.save('C:\\Users\\monog\\OneDrive\\바탕 화면\\Python_Project\\Animore\\momo.html') #다 안뜨는 오류...
    
    review_system = ReviewSystem(center_list)
    while True:
        
        if customer1.appoint_Center():
            appoint_center = Center()
            appoint = AppointSystem()
            appoint.request_appoint()
            appoint_center.accept_appoint(appoint.patient_info, appoint.time)
            


            center_name = input("\n리뷰를 작성하시겠습니까? 다녀온 병원 이름을 입력하세요. (종료: 'exit'): ")

            if center_name.lower() == 'exit':
                break

            rating = int(input("평점을 매겨주세요. (0-5): "))
            review = input("리뷰를 작성해주세요. : ")
            review_system.add_review(center_list, center_name, rating, review)

            view_reviews = input("이 센터의 모든 리뷰를 보시겠습니까? (y/n): ")
            if view_reviews.lower() == 'y':
                review_system.view_reviews(center_name)

        else:
            print("종료")

    

    
    

if __name__ == "__main__":
    main()
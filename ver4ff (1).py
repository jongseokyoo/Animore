from typing import List
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

class Pet:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

class Customer:
    customerID = 1
    def __init__(self):
        customer_info = input("사용자의 이름, 전화번호, 주소를 쉼표로 구분하여 입력해 주세요: ").split(',')
        self.name = customer_info[0]
        self.number = customer_info[1].strip()
        self.address = customer_info[2].strip()
        pet_info = input("반려동물의 이름, 나이, 종류를 쉼표로 구분하여 입력해 주세요: ").split(',')
        self.pet = Pet(pet_info[0], int(pet_info[1].strip()), pet_info[2].strip())
        self.customerID = Customer.customerID
       
        Customer.customerID += 1
       
     
    def contact_SaveSys(self):
        Centeraddress = input("검색할 주소를 입력하세요: ")
        return Centeraddress
   

    def appoint_Center(self):
        choice = input("에약 하시겠습니까? (Yes/No): ")
        if choice =="Yes":
            return True
        elif choice == "No":
            return False
        else:
            print("잘못 입력되었습니다. Yes/No로 입력해주세요.")

    def review_Center(self, Centername: str) -> None:
        pass

class Center:
    def __init__(self):
        center_name = input("예약을 희망하는 병원 이름을 입력해주세요.")
        self.center_name = center_name

    def accept_appoint(self, patient_info, time):
        choice = input("예약하시겠습니까? (Yes/No)")
        if choice == "Yes":
            print(patient_info, time, "에 예약이 되었습니다.")
        elif choice == "No":
            print("예약을 취소하셨습니다.")
        else:
            print("Yes/No 로 입력해주세요.")
            
class SaveSystem:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path, encoding='euc-kr')

        
    def filter_data_by_region(self, customer_address):
        try:
            filtered_df = self.df[self.df['관할구청'] == customer_address]

            if filtered_df.empty:
                print("잘못된 지역입니다. 다시 입력해주세요.")
                return []
            else:
                return  filtered_df
        except KeyError:
            print("잘못된 지역입니다. 다시 입력해주세요.")
            return []
       
   
    def return_review(self) -> str:
        pass

class AppointSystem:
    def __init__(self):
        patient_info = input("환자의 이름, 나이, 종류, 증상을 쉼표로 구분하여 입력해주세요.").split(',')
        self.name = patient_info[0]
        self.age = patient_info[1].strip()
        self.type = patient_info[2].strip()
        self.symptom = patient_info[3].strip()
        self.patient_info = [self.name, self.age, self.type, self.symptom]
   
    def request_appoint(self):
        time = input("예약을 희망하는 월, 일, 시간을 구분하여 입력해주세요.")
        self.time = time

class ReviewSystem:
    def __init__(self, center_list):
        self.centers = {center[0]: {'address': center[1], 'phone': center[2], 'reviews': []} for center in center_list}

    def select_center(self, center_name):
        if center_name in self.centers:
            return self.centers[center_name]
        else:
            print(f"{center_name} not found in the center list.")
            return None

    def add_review(self, center_list, center_name, rating, review):
        if center_name in self.centers:
            reviews = self.centers[center_name]['reviews']
            reviews.append({'rating': rating, 'review': review})

            # Calculate the updated average rating
            total_ratings = sum(review['rating'] for review in reviews)
            average_rating = total_ratings / len(reviews)

            # Update the center's average rating
            self.centers[center_name]['average_rating'] = average_rating

            # Update the center_list with the new reviews
            for center in center_list:
                if center[0] == center_name:
                    center[3] = average_rating
                    center[4] = reviews  # Update with the complete reviews list
                    break

            print(f"Review for {center_name} added successfully!")
        else:
            print(f"{center_name} not found in the center list.")

    def view_reviews(self, center_name):
        if center_name in self.centers:
            reviews = self.centers[center_name]['reviews']
            if not reviews:
                print("No reviews available.")
            else:
                for i, review in enumerate(reviews, 1):
                    print(f"Review {i}: {review['review']} (Rating: {review['rating']})")
        else:
            print(f"{center_name} not found in the center list.")


    
  


def main():
    customer1 = Customer()
    file_path = 'C:/Users/user/Downloads/파이썬/파이썬/csv파일.csv'
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
               zoom_start=14, 
               )
    for i in range(len(hospital_locations)):
        folium.Marker(location=hospital_locations[i], tooltip = f"{facility_names[i]} {phone_numbers[i]}").add_to(m)
    m.save('momo.html')
    
    review_system = ReviewSystem(center_list)
    if customer1.appoint_Center():
        appoint_center = Center()
        appoint = AppointSystem()
        appoint.request_appoint()
        appoint_center.accept_appoint(appoint.patient_info, appoint.time)
        while True:
            print("\nAvailable Centers:")
            for center in center_list:
                center_name, address, phone = center[0], center[1], center[2]
                print(f"- {center_name}, {address}, {phone}")

            center_name = input("\nEnter the name of the center you want to review (or 'exit' to quit): ")

            if center_name.lower() == 'exit':
                break

            rating = float(input("Give a rating (0-5): "))
            review = input("Write your review: ")
            review_system.add_review(center_list, center_name, rating, review)

            view_reviews = input("Do you want to view all reviews for this center? (yes/no): ")
            if view_reviews.lower() == 'yes':
                review_system.view_reviews(center_name)
                print(center_list)
    else:
        print("try it next time")

    

    
    



if __name__ == "__main__":
    main()
from typing import List

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
    def __init__(self, CeneterList: List[List[str]]):
        self.CeneterList = CeneterList

    def return_Ceneterlist(self, find_adress: str):
        find_list = []
        for inner_list in self.CeneterList:
            if find_adress in inner_list:
                find_list.append(inner_list)
        if find_list == []:
            print("찾으시는 주소가 없습니다 다시 입력해주세요.")
        else:
            return find_list
       
   
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
        self.centers = {center[0]: CenterReview() for center in center_list}

    def select_center(self, center_name):
        if center_name in self.centers:
            return self.centers[center_name]
        else:
            print(f"{center_name} not found in the center list.")
            return None

class CenterReview:
    def __init__(self):
        self.reviews = []

    def add_review(self, review, rating):
        self.reviews.append({'review': review, 'rating': rating})

    def view_reviews(self):
        if not self.reviews:
            print("No reviews available.")
        else:
            for i, review in enumerate(self.reviews, 1):
                print(f"Review {i}: {review['review']} (Rating: {review['rating']})")


#1. 무한 반복문으로 설정후 동물병원 list에 리뷰를 추가하기, 따로 CenterReview class말고, savesys에 저장되게
#2. 프로그램이 중단되지않게, 예외처리, 무한반복문 등 처리.
#3. 내용이 부실. tight하게 코드 작성 후 데이터 처리 잘 될시, 빠르게 기능추가.
def main():
   center_list = [['부산대동물병원', '금정구', '053-152-1231'],['웅비동물병원', '금정구', '053-152-1234'], ['해운대대동물병원', '해운대구', '053-112-8900'], ['동래동물병원', '동래구', '053-150-1111']] #SaveSystem value 차후 Excel list change
   save_list = SaveSystem(center_list)
   customer1 = Customer()
   find_address = customer1.contact_SaveSys()
   print(save_list.return_Ceneterlist(find_address))
   review_system = ReviewSystem(center_list)
   if customer1.appoint_Center():
       appoint_center = Center()
       appoint = AppointSystem()
       appoint.request_appoint()
       appoint_center.accept_appoint(appoint.patient_info, appoint.time)
       while True:
        print("\nAvailable Centers:")
        for center in center_list:
            print(f"- {center[0]}")

        center_name = input("\nEnter the name of the center you want to review (or 'exit' to quit): ")

        if center_name.lower() == 'exit':
            break

        selected_center = review_system.select_center(center_name)
        if selected_center:
            review = input("Write your review: ")
            rating = float(input("Give a rating (0-5): "))
            selected_center.add_review(review, rating)
            print(f"Review for {center_name} added successfully!")

        view_reviews = input("\nDo you want to view reviews for a specific center? (yes/no): ")
        if view_reviews.lower() == 'yes':
            center_name = input("Enter the name of the center you want to view reviews for: ")
            selected_center = review_system.select_center(center_name)
            if selected_center:
                selected_center.view_reviews()    



   

if __name__ == "__main__":
    main()
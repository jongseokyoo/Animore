#start Here
class Pet: # Customer 객체 생성시 사용. C++ struct와 같이 여러 인자를 가지는 변수 구현
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def __str__(self):  # Pet 객체를 문자열로 표현하는 메소드
        return f"이름: {self.name}, 나이: {self.age}, 종류: {self.type}"
class Customer:
    customerID = 1
    def __init__(self):
        try:
            customer_info = input("사용자의 이름, 전화번호, 주소를 쉼표로 구분하여 입력해 주세요: ").split(',')
        except:
            IndexError
        self.name = customer_info[0]
        self.number = customer_info[1].strip()
        self.address = customer_info[2].strip()
        N = int(input("반려동물이 총 몇 마리 인가요?")) 
        pets = []
        for i in range(N): 
            pet_info = input("반려동물의 이름, 나이, 종류를 쉼표로 구분하여 입력해 주세요: ").split(',')
            pet = Pet(pet_info[0], int(pet_info[1].strip()), pet_info[2].strip())
            pets.append(pet)
        self.pets = pets
        self.customerID = Customer.customerID
        
        Customer.customerID += 1
    def __str__(self):  # 객체를 문자열로 표현하는 메소드
        pet_info = '\n'.join(str(pet) for pet in self.pets)
        return f"고객 ID: {self.customerID}\n이름: {self.name}\n전화번호: {self.number}\n주소: {self.address}\n반려동물 정보:\n{pet_info}"  
     
    def contact_SaveSys(self): # 주소(문자열)로 검색, ... 검색 방식 여러가지?
        Centeraddress = input("검색할 주소를 입력하세요: ")
        return Centeraddress
   

    def appoint_Center(self):
        choice = input("에약 하시겠습니까? (Y/N): ")
        if choice =="Y":
            return True
        elif choice == "N":
            return False
        else:
            print("잘못 입력되었습니다. Y/N로 입력해주세요.")
#end Here

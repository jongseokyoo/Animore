class Center:
    def __init__(self):
        center_name = input("예약을 희망하는 병원 이름을 입력해주세요.")
        self.center_name = center_name

    def accept_appoint(self, patient_info, time):
        choice = input("예약하시겠습니까? (Y/N)")
        if choice == "Y":
            print(patient_info, time, "에 예약이 되었습니다.")
        elif choice == "N":
            print("예약을 취소하셨습니다.")
        else:
            print("Y/N 로 입력해주세요.")
import pandas as pd
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
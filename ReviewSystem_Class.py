class ReviewSystem:
    def __init__(self, center_list):
        self.centers = {center[0]: {'address': center[1], 'phone': center[2], 'reviews': []} for center in center_list}

    def select_center(self, center_name):
        if center_name in self.centers:
            return self.centers[center_name]
        else:
            print(f"{center_name} 병원 리스트에서 해당 병원을 찾을 수 없습니다.")
            return None

    def add_review(self, center_list, center_name, rating, review):
        if center_name in self.centers:
            reviews = self.centers[center_name]['reviews']
            reviews.append({'평점': rating, '리뷰': review})

            # Calculate the updated average rating
            total_ratings = sum(review['평점'] for review in reviews)
            average_rating = total_ratings / len(reviews)

            # Update the center's average rating
            self.centers[center_name]['average_rating'] = average_rating

            # Update the center_list with the new reviews
            for center in center_list:
               if center[0] == center_name:
                if len(center) >= 6:
                    center[4] = average_rating
                    center[5] = reviews
                else:
                    center.extend([average_rating, reviews])
                break

            print(f"{center_name}의 리뷰가 추가 되었습니다!")
        else:
            print(f"{center_name} 병원 리스트에서 해당 병원을 찾을 수 없습니다.")

    def view_reviews(self, center_name):
        if center_name in self.centers:
            reviews = self.centers[center_name]['reviews']
            if not reviews:
                print("리뷰가 없습니다.")
            else:
                for i, review in enumerate(reviews, 1):
                    print(f"리뷰 {i}: {review['리뷰']} (평점: {review['평점']})")
        else:
            print(f"{center_name} 병원 리스트에서 해당 병원을 찾을 수 없습니다.")

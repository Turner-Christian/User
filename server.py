class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        # default attributes
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print('----------------')
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member == True:
            print('ALREADY ENROLLED')
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print('NOT ENOUGH POINTS')
        self.gold_card_points -= amount 

user_christian = User('Christian', 'Turner', 'christ@gmail.com', 21)
user_christian.enroll().spend_points(50).display_info().enroll()


user_catherine = User('Cat', 'Murphy', 'catm@gmail.com', 21)
user_catherine.enroll().spend_points(80).display_info()

user_daniel = User('Daniel', 'Vintrov', 'daniel@gmail.com', 21)
user_daniel.display_info().spend_points(40)

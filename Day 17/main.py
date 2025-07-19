class User:
    def __init__(self,user_id,username,followers=0):
        self.id = user_id
        self.username = username
        self.followers = followers
        self.following = 0


    def follow(self,user):
        self.following += 1
        user.followers += 1
# print("hello world.....")


user1 = User(101,"sanju")
user2 = User(102,"dddd")
# user1.id = "oo1"
# user1.username = " Angela"
# print(user1.username)

print(user1.username,user1.id)
print(user1.followers)

user1.follow(user2)

print(user1.followers ,user1.username)
print(user1.following ,user1.username)
print(user2.followers ,user2.username)
print(user2.following, user2.username)

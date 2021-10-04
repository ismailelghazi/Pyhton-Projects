class Cars:
    def __init__(self, speed, name):
        self.sp = speed
        self.nm = name
        self.followers =0
        self.following =0
    def follow(self, user):
        user.followers += 1
        self.following +=1
car = Cars(5, "ismail")
print(car.sp)
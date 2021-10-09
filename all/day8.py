true = 0
while not true:
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5


    def givrmr(test_h,test_w):
        sM=test_h*test_w/coverage
        print(f"la moyne {sM}")
    givrmr(test_h,test_w)
    true=int(input("leave print 1 stay print 0 "))
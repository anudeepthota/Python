try:
    list = [1,2,3,4]
    print(list[6])
except IndexError as e:
    print("Index Error Excpetion...." + str(e))
finally:
    print("Execution is ended")

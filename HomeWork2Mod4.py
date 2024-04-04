auto_list = ["BMW", "MB", "LADA", "KIA", "HONDA"]
print(auto_list)
cars_count = 0
for i in range(len(auto_list)):
    print ("Я езжу на автомобиле марки ", auto_list[i])
    cars_count +=10

print("В моём автопарке ",cars_count," автомобилей")

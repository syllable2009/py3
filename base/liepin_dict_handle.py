


with open("/Users/jiaxiaopeng/liepin_zhineng", "r") as f:
    while True:
        text = f.readline()
        if not text:
            print("end")
            break
        print(text)
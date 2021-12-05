def open_or_senior(data):
    lst = []
    for (age,handicap) in data:
        if age > 54 and handicap > 7:
            lst.append("Senior")
        else:
            lst.append("Open")
    return lst

data = [(45, 12),(55,21),(19, -2),(104, 20)]
print(open_or_senior(data))
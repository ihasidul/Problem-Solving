if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])

    records.sort(key = lambda x: float(x[1]))
    lowest = records[0][1]
    second_lowest = None
    result = []
    for item in records:
        if item[1] == lowest:
            continue
        if second_lowest == None and item[1] > lowest:
            second_lowest = item[1]
        if second_lowest == item[1]:
            result.append(item[0])
            
    result.sort()
    for student in result:
        print(student)

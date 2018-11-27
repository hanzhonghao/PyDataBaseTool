import csv

def getWhiteList():
    filename = 'C:/Users/zhonghao.han/Desktop/test.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        #Line Numbers start with line 2
        next(reader)
        for row in reader:
            # 行号从2开始
            print(row)

    return reader

if __name__ == '__main__':
    getWhiteList()
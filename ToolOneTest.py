import csv
filename = 'C:/Users/zhonghao.han/Desktop/test.csv'
with open(filename) as f:
    reader = csv.reader(f)
    # 读取一行，下面的reader中已经没有该行了
    head_row = next(reader)


if __name__ == '__main__':
    open(filename)
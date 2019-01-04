import csv


def test():
    with open("test.csv", "a",newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["旭哥", 38])
        writer.writerow(["超哥哥", 29])

if __name__ == '__main__':
    test()
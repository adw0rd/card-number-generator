import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--prefix", default="4111111")
parser.add_argument("-c", "--count", type=int, default=10)


def gen(prefix, length=16):
    ccnumber = list(map(int, prefix))
    while len(ccnumber) < (length - 1):
        ccnumber.append(random.choice(range(0, 10)))
    evens, odds = [], []
    for index, element in enumerate(ccnumber):
        if index % 2 == 0:
            num = element * 2
            if num > 9:
                num -= 9
            evens.append(num)
        if index % 2 != 0:
            odds.append(element)
    total_sum = sum(evens) + sum(odds)
    last_num = 10 - (total_sum % 10)
    ccnumber.append(0 if last_num == 10 else last_num)
    return "".join(map(str, ccnumber))


def main(args):
    for i in range(args.count):
        print(gen(args.prefix))


if __name__ == "__main__":
    main(parser.parse_args())

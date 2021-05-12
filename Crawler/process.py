
SRC_PATH = 'E:/vs/TTBT_new_T.txt'
MID_PATH = 'E:/vs/TTBT_T_pro.tsv'
DST_PATH = 'E:/vs/TTBT_T.tsv'


def main():
    f = open(MID_PATH, 'a+', encoding='utf-8')
    for line in open(SRC_PATH, encoding='utf-8'):
        line1, line2 = line.split('|', 1)
        line2 = line2.split(' ')[-1]
        if len(line2) == 1:
            continue
        f.write('{}\t{}'.format(
                 line1, line2,
                encoding='utf-8'))

def main_2():
    f = open(DST_PATH, 'a+', encoding='utf-8')

    i = 0
    while i < 106478:
        f1 = open(MID_PATH, encoding='utf-8')
        f.write(f1.read())
        i += 986


if __name__ == '__main__':
    main() #数据处理
    main_2() #扩大规模
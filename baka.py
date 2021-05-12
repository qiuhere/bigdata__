import difflib
import random
dicti = {}
data_path = 'E:/vs/TTBT_T_pro.tsv'

def chat():

    f1 = open(data_path, encoding='utf-8')
    for line in f1:
        line1, line2 = line.split('\t', 1)
        if not line1 in dicti.keys():
            dicti[line1] = []
        dicti[line1].append(line2)
    while(1):
        input_sentence = input('Doragd > ')
        if input_sentence == 'q' or input_sentence == 'quit' or input_sentence == 'exit': break
        output_words = cal(input_sentence)
        print('BOT > ', output_words)


def cal(input_sentence):
    maxx = 0
    maxkey = ''
    for key in dicti.keys():
        r = difflib.SequenceMatcher(None, input_sentence, key).real_quick_ratio()
        if r > maxx:
            maxx = r
            maxkey = key
    return dicti[maxkey][random.randint(0, len(dicti[maxkey]) - 1)]


if __name__ == '__main__':
    chat()
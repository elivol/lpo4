import re
import pymorphy2
import gram

string = "Лучше приходи всегда в один и тот же час,  - попросил Лис."
string1 = "Сражение выигрывает тот, кто твердо решил его выиграть! "


# Функция разбиения строки на слова
def get_tokens(input):
    return re.sub('[ .,?:;\'\"!()\[\]\n-]+', ' ', input).strip().split(' ')


def get_seps(input):
    return re.split('\w+', input)


def morph_analysis(input):
    # Раздаление строки на слова и разделители
    words = get_tokens(input)
    seps = get_seps(input)

    # Морфологический анализ слов
    morph = pymorphy2.MorphAnalyzer()
    types_of_words = [gram.gramems.get(morph.parse(el)[0].tag.POS, 'не известно') for el in words]

    # Формирование строки - результата
    res = ''
    if seps[0]:
        res += seps[0]
        seps.pop(0)
    else:
        seps.pop(0)

    for i in range(max(len(words), len(seps))):
        if i < len(words):
            res += words[i] + '(' + types_of_words[i] + ')'
        if i < len(seps):
            res += seps[i]
    return res

print(morph_analysis(string))
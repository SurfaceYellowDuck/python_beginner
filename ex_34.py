def count_vowel_letters(word):
    return len([letter for letter in word if letter.lower() in 'ауоыэяюёие'])


def vinny_ritm(func, str_):
    phrases_list = str_.split(" ")
    cnt = 0
    for phrase in phrases_list:
        for word in phrases_list:
            res = func(word)
            cnt += res
    if cnt % 2 == 0:
        return "Парам пам-пам"
    else:
        return "Пам парам"

str_1 = "пара-ра-рам рам-пам-папам па-ра-па-да"
str_2 = "пара-ра"
print(vinny_ritm(count_vowel_letters, str_1))
print(vinny_ritm(count_vowel_letters, str_2))

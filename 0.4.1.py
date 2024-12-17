stoim_tovara = int(input())
kolvo_tovara = int(input())
promo = input()
ves_tovar = kolvo_tovara * stoim_tovara


def magaz(stoim_tovara, kolvo_tovara, promo):
    skidka = 0
    if kolvo_tovara > 1000 and kolvo_tovara < 5001 and 'SUPERDISCOUNT' in promo:
        skidka += 10
    elif kolvo_tovara > 1000 and kolvo_tovara < 5001 and 'SUPERDISCOUNT' not in promo:
        skidka += 5
    elif kolvo_tovara > 5000 and 'SUPERDISCOUNT' in promo:
        skidka += 20
    elif kolvo_tovara > 5000 and 'SUPERDISCOUNT' not in promo:
        skidka += 15
    return skidka


def magaz2(stoim_tovara, kolvo_tovara, promo):
    ves_tovar = kolvo_tovara * stoim_tovara
    if kolvo_tovara > 1000 and kolvo_tovara < 5001 and 'SUPERDISCOUNT' in promo:
        ves_tovar = ves_tovar * 0.9
    if kolvo_tovara > 1000 and kolvo_tovara < 5001 and 'SUPERDISCOUNT' not in promo:
        ves_tovar = ves_tovar * 0.95
    if kolvo_tovara > 5000 and 'SUPERDISCOUNT' in promo:
        ves_tovar = ves_tovar * 0.8
    if kolvo_tovara > 5000 and 'SUPERDISCOUNT' not in promo:
        ves_tovar = ves_tovar * 0.85
    return ves_tovar


print('Ваша скидка:', magaz(stoim_tovara, kolvo_tovara, promo))
print('Итоговая сумма:', magaz2(stoim_tovara, kolvo_tovara, promo))
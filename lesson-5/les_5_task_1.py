# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple
import helper

Company = namedtuple('Company', 'name q1 q2 q3 q4 profit')

cnt = helper.int_input('Введите количество предприятий: ')
companies = []
profit_sum = 0
for i in range(cnt):
    print('Компания #%s' % (i+1))
    name = helper.str_input('Введите название предприятие: ')
    qs = []
    for j in range(4):
        qs.append(helper.float_input('Введите прибыль для %s квартала: ' % (j+1)))
    companies.append(Company(name, *qs, sum(qs)))
    profit_sum += sum(qs)

profit_avg = profit_sum/cnt
more, less = [], []

for c in companies:
    if c.profit > profit_avg:
        more.append(c)
    elif c.profit < profit_avg:
        less.append(c)

print('=' * 10)
if cnt == 1:
    print('Введено всего одно предприятие')
    print('Название %s. Прибыль: %.2f' % (companies[0].name, companies[0].profit,))
else:
    print('Средняя прибыль: %.2f' % profit_avg)
    print('Предприятия чья прибыль меньше средней:')
    for c in less:
        print('Название %s. Прибыль: %.2f' % (c.name, c.profit))
    print('='*10)
    print('Предприятия чья прибыль больше средней:')
    for c in more:
        print('Название %s. Прибыль: %.2f' % (c.name, c.profit,))
    print('='*10)

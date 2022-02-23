def health_calculator(age, apples_ate, cigars_smoked):
    answer = (100-age) + (apples_ate * 3.5) - (cigars_smoked * 2)
    print(answer)


bucky_data = [27, 20, 0]
health_calculator(bucky_data[0], bucky_data[1], bucky_data[2])
health_calculator(*bucky_data)  # unpacking arguments

date, item, price = ['December 23, 2019', 'Colacola', 20.89]


def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)


drop_first_last([23, 78, 98, 49, 73, 63, 87])


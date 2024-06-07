from gui import out

def is_valid(question, error, len_val=0):
    if len_val == 0:
        while True:
            try:
                val = input(question)
                if len(val) == 11 and int(val):
                    return val
                else:
                    print(error)
            except ValueError:
                print(error)
    else:
        while True:
            try:
                val = input(question)
                if len(val) == len_val and int(val):
                    return val
                else:
                    print(error)
            except ValueError:
                print(error)


def checked(iter_list, temp_res):
    try:
        tmp_sum = 0
        for a, b in zip(iter_list, temp_res):
            tmp_sum += a * b
        return tmp_sum % 11
    except Exception as e:
        print('Ошибка: ', e)


def count_discharge(temp_res):
    first_iter_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    second_iter_list = [3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

    result = checked(first_iter_list, temp_res)

    if result >= 10:
        new_result = checked(second_iter_list, temp_res)
        return new_result
    else:
        return result


def main():
    snils = list(is_valid("\nВведите СНИЛС гражданина (только цифры: 00011122233): ", "\nСНИЛС введен неверно! Попробуйте еще раз" ))
    month = list(is_valid("\nВведиите месяц (2 цифры):", "\nМесяц введен неверно! Попробуйте еще раз", 2))
    year = list(is_valid("\nВведиите год  (2 цифры):", "\nГод введен неверно! Попробуйте еще раз", 2))

    tmp_list = ['232', snils, month, year, '0']

    tmp_uit_res = list()

    for string in tmp_list:
        for num_uin in string:
            tmp_uit_res.append(int(num_uin))

    discharge = count_discharge(tmp_uit_res)

    result = [str(num) for num in tmp_uit_res]

    uin_value = "".join(result) + str(discharge)

    out(uin_value)



if __name__ == '__main__':
    while True:
        main()
        print()
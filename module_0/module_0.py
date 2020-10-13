def main_game():
    # Функция загадывает случайное число и запускает алгоритм бинарного поиска.
    import numpy as np
    searched_num = np.random.randint(1, 101)

    temp_list = list(range(1, 101))
    count = 1
    
    while True:
        count += 1
        temp_list_middle = len(temp_list)//2
        guess_num = temp_list[temp_list_middle]
        if guess_num == searched_num:
            break
        else:
            if searched_num < guess_num:
                for del_element in range(temp_list_middle):
                    del temp_list[-1]
            else:
                for del_element in range(temp_list_middle):
                    del temp_list[0]
    
    return(count) # Функция возвращает количесто попыток поиска числа.


def mean_score_count(main_game, check_count=1000):
    # Функция запускает игру {check_count} раз,
    # чтобы узнать среднее число попыток поиска числа.
    import numpy as np
    score_count_list = list()
    
    for check_number in range(check_count):
        game_result = main_game()
        score_count_list.append(game_result)
    
    mean_score = int(np.mean(score_count_list))
    
    return print(f"Ваш алгоритм угадывает число в среднем за {mean_score} попыток")


mean_score_count(main_game, 500)

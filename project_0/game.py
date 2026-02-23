import numpy as np

def binary_predict(number: int = 1) -> int:
    """Угадываем число двоичным поиском
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    
    Returns:
        int: Число попыток
    """
    count = 0
    low = 1
    high = 101
    
    while True:
        count += 1
        predict_number = (low + high) // 2  # берём середину диапазона
        
        if number == predict_number:
            break
        elif number > predict_number:
            low = predict_number + 1  # ищем в верхней половине
        else:
            high = predict_number  # ищем в нижней половине
    
    return count


def score_game(binary_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        binary_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(binary_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(binary_predict)
score_game(binary_predict)
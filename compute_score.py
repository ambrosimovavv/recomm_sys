import json
import argparse
import numpy as np


def euclidean_score(data, user1, user2):
    common_movies = {}
    for item in data[user1]:
        if item in data[user2]:
            common_movies[item] = 1

    if len(common_movies) == 0:
        return 0

    squar_dif = []
    for item in data[user1]:
        if item in data[user2]:
            squar_dif.append(np.square(data[user1][item] - data[user2][item]))

    return 1 / (1 + np.sqrt(np.sum(squar_dif)))


def pearson_score(data, user1, user2):
    if user1 not in data:
        raise TypeError('Cannot find' + user1 + 'in the dataset')
    if user2 not in data:
        raise TypeError('Cannot find' + user2 + 'in the dataset')

    common_movies = {}
    for item in data[user1]:
        if item in data[user2]:
            common_movies[item] = 1

    if len(common_movies) == 0:
        return 0
    # вычисление суммы рейтинговыых оценок всех фильмов, оценнных обоими пользователями
    user1_sum = np.sum([data[user1][item] for item in common_movies])
    user2_sum = np.sum([data[user2][item] for item in common_movies])

    user1_squar_sum = np.sum([np.square(data[user1][item]) for item in common_movies])
    user2_squar_sum = np.sum([np.square(data[user2][item]) for item in common_movies])

    sum_of_prod = np.sum([data[user1][item] * data[user2][item] for item in common_movies])

    Sxy = sum_of_prod - (user1_sum * user2_sum / len(common_movies))
    Sxx = user1_squar_sum - np.square(user1_sum) / len(common_movies)
    Syy = user2_squar_sum - np.square(user2_sum) / len(common_movies)

    if Sxx * Syy == 0:
        return 0
    return Sxy / np.sqrt(Sxx * Syy)

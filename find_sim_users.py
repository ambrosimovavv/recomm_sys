import compute_score
import numpy as np


def find_similar_users(data: object, user: object,) -> object:
    if user not in data:
        raise TypeError('Cannot find' + user + 'in the dataset')

    scores = np.array([[x, compute_score.pearson_score(data, user,
                                                       x)] for x in data if x != user])

    scr_sort = np.argsort(scores[:, 1])[::-1]
    top_user = scr_sort
    lst_name = []
    for i in top_user:
        lst_name.append(scores[i][0])
    return lst_name

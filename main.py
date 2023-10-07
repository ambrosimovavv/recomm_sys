import json
#import colab_filter
import find_sim_users
import recommend

def recom_by_user(user):
    with open('ratings.json', 'r') as f:
        data = json.loads(f.read())

    sim_usrs = find_sim_users.find_similar_users(data, user)
    recom_set = recommend.get_recommedation(data, user, sim_usrs)
    return recom_set
#    print("\nФильмы на вечер для " + user + ":")
#    for i, mov in enumerate(recom_set):
#        print(str(i+1) + '.' + mov)



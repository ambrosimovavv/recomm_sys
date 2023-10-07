def get_recommedation(dataset, input_user, sim_users):
    set_input_user = set(dataset[input_user].keys())
    set_recom = set()
    for i in sim_users:
        s = set(dataset[i].keys()).difference(set_input_user)
        set_recom.update(s)
    return set_recom
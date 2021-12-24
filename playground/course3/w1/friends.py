import requests
from datetime import datetime

def calc_age(uid):
    res = []
    token = '4240476e4240476e4240476ebb423ade78442404240476e2384a22b753f658a431e8153'
    url_users = 'https://api.vk.com/method/users.get'
    params_user = { "v": "5.81",
               "access_token": token,
               "user_ids": uid,
               "fields": "bdate" }
    r_user = requests.get(url_users, params=params_user)
    user_id = r_user.json()['response'][0]['id']

    url_friends = 'https://api.vk.com/method/friends.get'
    params_friends = {"v": "5.81", "access_token": token, "user_id": user_id, "fields": "bdate"}
    r_friends = requests.get(url_friends, params=params_friends)
    data_friends = r_friends.json()['response']['items']
    friends_age = []
    for friend in data_friends:
        if 'bdate' in friend.keys():
            try:
                year = int(friend['bdate'][-4:])
                friend_age = datetime.now().year - year
                friends_age.append(friend_age)
            except ValueError:
                pass
        else:
            continue

    for age in set(friends_age):
        res.append((age, friends_age.count(age)))

    res = sorted(sorted(res, key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
    #sorted(res, key=lambda x: x[0])

    return res


if __name__ == '__main__':
    res = calc_age('id2224960')
    print(res)
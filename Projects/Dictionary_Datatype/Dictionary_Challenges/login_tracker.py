def login_tracker(users):
    tracker={}
    for user in users:
        if user not in tracker.keys():
            tracker[user]=1
        else:
            tracker[user]+=1
    return tracker


def login_tracker2(users):
    tracker={}
    for user in users:
        tracker[user]=tracker.setdefault(user,0)+1
    return tracker

users = ['john', 'bob', 'alex', 'alice', 'charlie', 'john',
         'alex', 'alice', 'john', 'alex']

track=login_tracker(users)
print(track)
track=login_tracker2(users)
print(track)

#another way

def readDict():
    a = {}
    n = int(input())
    for i in range(n):
        s = input().split()
        a[s[0]] = set(s[1:])
    return a

def friendsOfFriends(d):
    result = {}
    for person, friends in d.items():
        q = set()
        for friend in friends:
            for friend_of_friend in d.get(friend, []):
                if friend_of_friend != person and friend_of_friend not in friends:
                    q.add(friend_of_friend)
        result[person] = q
    return result
d = friendsOfFriends(readDict())

for i in sorted(d.keys()):
    print(i, sorted(d[i]))
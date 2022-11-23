"""
See ddescription at https://www.hackerrank.com/challenges/py-the-captains-room
"""

from collections import Counter

K = int(input())
rooms = list(map(int, input().split()))

counts = Counter(rooms)
captain_room, _ = counts.most_common()[-1]
print(captain_room)

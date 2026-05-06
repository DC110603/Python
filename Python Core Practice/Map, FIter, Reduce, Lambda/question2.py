"""Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use
filter() to keep only the keys whose values are greater than 50."""

d = {"apple": 100, "banana": 40, "cherry": 150}
di2=dict(filter(lambda x: x[1]>=50,d.items()))
print(di2)

"""for i in d:
    print(i)"""
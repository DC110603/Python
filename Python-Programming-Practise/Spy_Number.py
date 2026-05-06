"""n=int(input())
t=n
su=0
pro=1
while t>0:
    r=t%10
    su+=r
    pro*=r
    t//=10
if su == pro:
    print("Spy Number")"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# sample data
X = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model
model = LinearRegression()
model.fit(X_train, y_train)

# prediction
print(model.predict([[5]]))
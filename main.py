import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

df = df.drop('Cabin', axis=1)
df=df.drop('Name', axis=1)
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

df['Sex']=df['Sex'].map({'male':1, 'female':2})
df['Embarked']=df['Embarked'].map({'C':0, 'S':1, 'Q':2})
df['Total_family']=df['SibSp']+df['Parch']

X=df.drop(['PassengerId', 'Survived', 'Ticket'], axis=1)
Y=df[['Survived']]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model=RandomForestClassifier()
model.fit(X_train, Y_train)
predict=model.predict(X_test)
acerto=accuracy_score(Y_test, predict)
print(acerto)

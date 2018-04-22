from sklearn import svm
from sklearn import linear_model
from sklearn import tree
from sklearn.naive_bayes import GaussianNB 
from sklearn.gaussian_process import GaussianProcessClassifier
clf = svm.SVC()
clf1 = linear_model.LogisticRegression()
clf2 = tree.DecisionTreeClassifier()
clf3 = GaussianNB() 
clf4 = GaussianProcessClassifier() 
# clf5 = linear_model.LinearRegression()
X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,66,40],[190,90,47],[175,64,39],[177,70,40],[159,55,37],[171,75,42],[181,85,43]]
Y=['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
'female', 'male', 'male']
clf=clf.fit(X,Y)
clf1=clf1.fit(X,Y)
clf2=clf2.fit(X,Y)
clf3=clf3.fit(X,Y)
clf4=clf4.fit(X,Y)
# clf5=clf5.fit(X,Y)
prediction=clf.predict([[190,70,43]])
prediction1=clf1.predict([[190,70,43]])
prediction2=clf2.predict([[190,70,43]])
prediction3=clf3.predict([[190,70,43]])
prediction4=clf4.predict([[190,70,43]])
# prediction5=clf5.predict([[190,70,43]])
# # print(prediction)
# print(prediction1)
# print(prediction2)
# print(prediction3)
# print(prediction4)
max_acc=max(prediction,prediction1,prediction2,prediction3,prediction4);
if max_acc == prediction:
	print("SVM")
elif max_acc == prediction1:
	print("LogisticRegression")
elif max_acc == prediction2:
	print("DecisionTreeClassifier")
elif max_acc == prediction3:
	print("GaussianNB")
elif max_acc == prediction4:
	print("GaussianProcessClassifier")
# elif max_acc == prediction5:
# 	print("LinearRegression")
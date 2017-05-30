#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
clf = svm.SVC(C=10000.0,kernel='rbf') 
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 
t0=time()
clf.fit(features_train,labels_train)
print "Time taken to train = %d" % round(time()-t0,3)

pred = clf.predict(features_test)
# for i in (10,26,56):
# 	print "%dth label = %d Correct %dth label= %d" % (i,pred[i],i,labels_test[i])


# t1=time()
# print(clf.score(features_test,labels_test))
# print "Time to predict= %d seconds" % ( round(time()-t1,3) )


t2=time()
count=0
for i in range(1,1700):
	if pred[i] == 1:
		count=count+1
print "Time to count =",time()-t2
print "No. of Chris test passes =",count 
#########################################################



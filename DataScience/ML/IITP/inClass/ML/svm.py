#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.svm import SVC,NuSVC
from sklearn.metrics import accuracy_score

raw_df = pd.read_csv('../../data/basketball.csv')
df = raw_df.copy()
#%%
X = df.iloc[:,2:]
y =  df.iloc[:,1]
# train,test -> train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,train_size= 0.7)
#%%
# train (모델 선택) -> svm -SVC,NuSVC
k = 'linear'
c = 1.0
pos_clf = SVC(kernel=k,C=c).fit(X_train,y_train)

y_hat = pos_clf.predict(X_test)
acc = accuracy_score(y_hat,y_test)

def svc_param_selection(X,y,cv):
    svm_parameters = [
        {
            'kernel' : ["linear", "poly", "rbf", "sigmoid"],
            'gamma' :[0.00001,0.0001,0.001,0.01,0.1,1],
            'C' : [0.01,0.1,1,10,100,1000]
        }
    ]
    clf = GridSearchCV(SVC(),svm_parameters,cv=cv)
    clf.fit(X,y.values.ravel())
    print(clf.best_params_)
    return clf
clf = svc_param_selection(X_train,y_train,5)

# 모델 검증 verification ( 튜닝) -> accuracy, 

# 시각화
# 시각화를 하기 위해, 최적의 C와 최적의 C를 비교하기 위한 다른 C를 후보로 저장합니다.
C_canditates = []
C_canditates.append(clf.best_params_['C'] * 0.01)
C_canditates.append(clf.best_params_['C'])
C_canditates.append(clf.best_params_['C'] * 100)

# 시각화를 하기 위해, 최적의 gamma와 최적의 gamma를 비교하기 위한 다른 gamma를 후보로 저장합니다.
gamma_candidates = []
gamma_candidates.append(clf.best_params_['gamma'] * 0.01)
gamma_candidates.append(clf.best_params_['gamma'])
gamma_candidates.append(clf.best_params_['gamma'] * 100)

X = df[['3P', 'BLK']]
Y = df['Pos'].tolist()

# 포지션에 해당하는 문자열 SG와 C를 벡터화합니다.
position = []
for gt in Y:
    if gt == 'C':
        position.append(0)
    else:
        position.append(1)

# 각각의 파라미터에 해당하는 SVM 모델을 만들어 classifiers에 저장합니다.
classifiers = []
for C in C_canditates:
    for gamma in gamma_candidates:
        clf = SVC(C=C, gamma=gamma)
        clf.fit(X, Y)
        classifiers.append((C, gamma, clf))

# 18,18 사이즈의 챠트를 구성합니다.
plt.figure(figsize=(18, 18))
xx, yy = np.meshgrid(np.linspace(0, 4, 100), np.linspace(0, 4, 100))

# 각각의 모델들에 대한 결정 경계 함수를 적용하여 함께 시각화합니다.
for (k, (C, gamma, clf)) in enumerate(classifiers):
    Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    
    plt.subplot(len(C_canditates), len(gamma_candidates), k + 1)
    plt.title("gamma=10^%d, C=10^%d" % (np.log10(gamma), np.log10(C)),
              size='medium')

    # 서포트 벡터와 결정경계선을 시각화합니다.
    plt.pcolormesh(xx, yy, -Z, cmap=plt.cm.RdBu)
    plt.scatter(X['3P'], X['BLK'], c=position, cmap=plt.cm.RdBu_r, edgecolors='k')
plt.show()
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

#%%
raw_df = pd.read_csv('../../data/iris.csv')
df = raw_df.copy()

# %%
x = df.iloc[:,1:-1]
y = df.iloc[:,-1]
# %%
pca = PCA(n_components=2)
pca.fit(x)
X_r2 = pca.transform(x)
le = LabelEncoder()
le.fit(y)
le_y = le.transform(y)
# %%
df = pd.DataFrame(np.concatenate([X_r2,le_y.reshape(-1,1)],axis=1))
df.columns = ['pca_1','pca_2','target']
df.target = df.target.astype('int')
X = df.iloc[:,:-1]
y = df.iloc[:,-1]
X_train , X_test, y_train,y_test = train_test_split(X,y,test_size = 0.3)
# %%
def display_decision_surface(clf,X, y):
    x_min = X.pca_1.min() - 0.01
    x_max = X.pca_1.max() + 0.01
    y_min = X.pca_2.min() - 0.01
    y_max = X.pca_2.max() + 0.01
    
    n_classes = len(le.classes_)
    plot_colors = "ryw"
    plot_step = 0.001
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                        np.arange(y_min, y_max, plot_step))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    cs = plt.contourf(xx, yy, Z, cmap=plt.cm.RdYlBu)
    for i, color in zip(range(n_classes), plot_colors):
        idx = np.where(y == i)
        plt.scatter(X.loc[idx].pca_1, 
                    X.loc[idx].pca_2, 
                    c=color, 
                    label=le.classes_[i],
                    cmap=plt.cm.RdYlBu, edgecolor='black', s=200)

    plt.title("Decision surface of a decision tree",fontsize=16)

    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=14)
    plt.xlabel('pca_1',fontsize=16)
    plt.ylabel('pca_2',fontsize=16)
    plt.rcParams["figure.figsize"] = [7,5]
    plt.rcParams["font.size"] = 14
    plt.rcParams["xtick.labelsize"] = 10
    plt.rcParams["ytick.labelsize"] = 10
    plt.show()
# %%
dt_clf = DecisionTreeClassifier(max_depth=7,
                                  criterion='gini',
                                  min_samples_split=2,
                                  min_samples_leaf=3)
dt_clf.fit(X,y)

display_decision_surface(dt_clf,X,y)
# %%



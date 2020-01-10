import pandas as pd

df = pd.read_csv("/home/qasem/PycharmProjects/mir/data_jupyter/test_data_with_train_dictionary.csv")


df = df.drop(["documents_size", 'tag.1'], axis=1)


# In[52]:


df.head()


# In[46]:


import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
X = df.values
from sklearn.cluster import KMeans

km = KMeans(
    n_clusters=10, init='random',
    n_init=10, max_iter=300, 
    tol=1e-04,
)
y_km = km.fit_predict(X)


# In[56]:

print(y_km)


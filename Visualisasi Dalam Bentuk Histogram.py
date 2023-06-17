#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# Import library yang diperlukan
import pandas as pd
import matplotlib.pyplot as plt

# Membaca database
data = pd.read_csv("C:/PYTHON/579019292_bukalapak.csv")

# Membuat histogram dengan menggunakan data jumlah_rating dan membaginya ke dalam 10 bins
plt.hist(data['jumlah_rating'], bins=10)

# Menambahkan judul ke plot
plt.title("Histogram Jumlah Rating")

# Menetapkan label sumbu X dan Y
plt.xlabel('Jumlah Rating')
plt.ylabel('Frekuensi')

# Menampilkan plot
plt.show()


# In[ ]:





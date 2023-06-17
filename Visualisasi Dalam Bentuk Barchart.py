#!/usr/bin/env python
# coding: utf-8

# In[28]:




#!/usr/bin/env python
# coding: utf-8

# Import library yang diperlukan
import pandas as pd
import matplotlib.pyplot as plt

# Membaca database
data = pd.read_csv("C:/PYTHON/579019292_bukalapak.csv")

# Membuat bar chart dengan jumlah_sold sebagai sumbu X dan jumlah_rating sebagai sumbu Y
plt.bar(data['jumlah_sold'], data['jumlah_rating'])

# Menambahkan judul ke plot
plt.title("Jumlah Rating dan Jumlah Sold")

# Menetapkan label sumbu X dan Y
plt.xlabel('Jumlah Sold')
plt.ylabel('Jumlah Rating')

# Menampilkan plot
plt.show()


# In[ ]:





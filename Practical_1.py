import numpy as np


m = int(input())
sentences = []
for i in range(m):
        temp = input()
        for c in '''!()-[]{};:'"\,<>./?@#$%^&*_~''':
            temp = temp.replace(c, '')
        temp = temp.lower()
        temp = temp.split()
        sentences.append(temp)

query = input()
for c in '''!()-[]{};:'"\,<>./?@#$%^&*_~''':
    query = query.replace(c, '')
query = query.lower()
query = query.split()

tocken = {}
freq = {}

k = 0
for i in sentences:
        for j in set(i):
                if j not in tocken.keys():
                        tocken[j] = k
                        k = k+1
                
                freq[tocken[j]] = freq.get(tocken[j],0) + 1


freq_arr = np.zeros([m, len(tocken)])
query_vec = np.zeros([1, len(tocken)])
for i in range(m):
        for j in sentences[i]:
                freq_arr[i][tocken[j]] = freq_arr[i][tocken[j]] + 1
        freq_arr[i] = freq_arr[i]/len(sentences[i])


for j in query:
    if j in tocken.keys():
        query_vec[0][tocken[j]] = query_vec[0][tocken[j]] + 1
query_vec = query_vec/len(query)


tf_idf = np.zeros([1,len(tocken)])
for i in range(len(tocken)):
        tf_idf[0][i] = m/freq[i]
tf_idf = np.log(tf_idf)

final = np.zeros([m, len(tocken)])
for i in range(m):
        final[i] = np.multiply(tf_idf, freq_arr[i])

query_vec = np.multiply(tf_idf, query_vec)

query_vec = np.reshape(query_vec, (-1, 1))




result = np.matmul(final, query_vec)
a = result.argmax(axis = 0)
a = int(a)
a = a+1

print(a)


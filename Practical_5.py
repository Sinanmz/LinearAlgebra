import numpy as np

a, b, d = [int(i) for i in input().split()]

sentences = []
for i in range(a + b):
        temp = input()
        for c in '''!()-[]{};:'"\,<>./?@#$%^&*_~''':
            temp = temp.replace(c, '')
        temp = temp.lower()
        temp = temp.split()
        sentences.append(temp)


tocken = {}
freq = {}

k = 0
for i in sentences:
        for j in set(i):
                if j not in tocken.keys():
                        tocken[j] = k
                        k = k+1
                
                freq[tocken[j]] = freq.get(tocken[j],0) + 1


freq_arr = np.zeros((a+b, len(tocken)))
for i in range(a+b):
        for j in sentences[i]:
                freq_arr[i][tocken[j]] = freq_arr[i][tocken[j]] + 1
        freq_arr[i] = freq_arr[i]/len(sentences[i])

freq_arr = freq_arr.T

U, E, V = np.linalg.svd(freq_arr, full_matrices=False)


U_n = U[:, :d]

E_n = np.zeros((d, d))
for i in range(d):
       E_n[i, i] = E[i]

V_n = V[:d, :]

embeddings = U_n @ E_n @ V_n

for i in range(a+b):
       embeddings[:, i]/np.linalg.norm(embeddings[:, i])

in_sentences = embeddings[:, :a]

queries = embeddings[:, a:]

results = (in_sentences.T @ queries).argmax(axis=0)

[print(i) for i in results]


              
import numpy as np

def custom_round(x):
    x[np.abs(x) < 0.000001] = 0    
    return np.round(x,2)


def inverse(x):
    Gauss_jordan = np.concatenate((x, np.eye(x.shape[0])), axis=1)
    for i in range(Gauss_jordan.shape[0]):
        for k in range(i+1, Gauss_jordan.shape[0]+1):
            if np.round(Gauss_jordan[i, i], 6) != 0 :
                break
            elif k == Gauss_jordan.shape[0]:
                return -1
            else:
                Gauss_jordan[i] , Gauss_jordan[k] = Gauss_jordan[k] , Gauss_jordan[i]
        Gauss_jordan[i] /= Gauss_jordan[i, i]
        for j in range(Gauss_jordan.shape[0]):
            if j != i and np.round(Gauss_jordan[j, i], 6) != 0:
                Gauss_jordan[j] -= (Gauss_jordan[i]*Gauss_jordan[j, i])
    return Gauss_jordan[:, int(Gauss_jordan.shape[1]/2):]








    


m = int(input())
n = int(input())
p = int(input())




check = []
x_first_col = [int(i) for i in input().split()]

for j in range(n-1):
        dummy = np.array([int(i) for i in input().split()]).reshape(1, -1)
        check.append(dummy)

y_first_col = [int(i) for i in input().split()]
check.append(np.array(y_first_col).reshape(1, -1))

X = np.zeros((m, len(x_first_col)))
Y = np.zeros((m, len(y_first_col)))
queries = np.zeros((p, len(x_first_col)))

# print(check)
X[0] = x_first_col
Y[0] = y_first_col

for i in range(m-1):
    X[i+1] = [int(i) for i in input().split()]
    for j in range(n-1):
        dummy = np.array([int(i) for i in input().split()]).reshape(1, -1)
        # print(dummy)
        # print(check)
        check[j] = np.concatenate((check[j], dummy), axis=0)
    Y[i+1] = [int(i) for i in input().split()]
    check[-1] = np.concatenate((check[-1], Y[i+1].reshape(1, -1)), axis=0)



# check = check[:, 1:].reshape(m, -1)
# print(check)
for i in range(p):
    queries[i] = [int(i) for i in input().split()]


X = X.T
Y = Y.T
queries = queries.T
flag = 0
for i in range(m):
    for j in range(i+1, m):
        if (X.T[i] == X.T[j]).all():
            for k in range(len(check)):
                if not (check[k][i] == check[k][j]).all():
                    # flag = 1
                    break
    if flag == 1:
        break



XXT = X @ X.T
inv = inverse(XXT)
if X.shape[0] > X.shape[1] or flag == 1 or type(inv) == int:
    print("The results are unknown")
else:
    
    # print(XXT)
    # Gauss_jordan = np.concatenate((XXT, np.eye(X.shape[0])), axis=1)
    # Gauss_jordan = XXT
    # print(Gauss_jordan)

    # for i in range(Gauss_jordan.shape[0]):
    #     k = i
    #     for k in range(i+1, Gauss_jordan.shape[0]+1):
    #         if Gauss_jordan[i, i] != 0 :
    #             break
    #         elif k == Gauss_jordan.shape[0]:
    #             print("The results are unknown")
    #             k = -1
    #             break
    #         else:
    #             Gauss_jordan[i] , Gauss_jordan[k] = Gauss_jordan[k] , Gauss_jordan[i]
    #     if k == -1:
    #         break
    #     Gauss_jordan[i] /= Gauss_jordan[i, i]
    #     for j in range(Gauss_jordan.shape[0]):
    #         if j != i and Gauss_jordan[j, i] != 0:
    #             Gauss_jordan[j] -= (Gauss_jordan[i]*Gauss_jordan[j, i])
                # print(Gauss_jordan)


    # A = (Y @ X.T) @ 
    # print(Gauss_jordan)

    # print(np.linalg.inv(XXT))
    # print(Gauss_jordan[:, int(Gauss_jordan.shape[1]/2):] == np.linalg.inv(XXT))

    
    A = (Y @ X.T) @ (inv)
    # print(A)
    # A = custom_round(A)
  
    if np.sum(np.abs(A@X-Y))>0.01:
        print("The results are noisy")
    results = A @ queries
    results = custom_round(results)
    for i in range(results.shape[1]):
        for j in range(results.shape[0]):
            print(results[j, i], end=" ")
        print()






            




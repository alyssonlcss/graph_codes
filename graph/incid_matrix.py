import numpy as np

def charge_matrix():
    with open('first_lesson/gtest.txt', 'r') as file:
        list = file.readlines()
        for i in range(len(list)):
            line = list[i].split()
            if i == 0:
                n = int(line[0])
                m = int(line[1])
                incid_mtx = np.zeros((n, m), dtype=np.int64)
            else:
                incid_mtx[int(line[0])-1, i-1] = int(line[2])
                incid_mtx[int(line[1])-1, i-1] = int(line[2])
    out_matrix(n, m, incid_mtx)


def out_matrix(n, m, incid_mtx):
    for i in range(n):
        print(i+1, ": ", end='')
        for j in range(m):
            print("%.2d" %(incid_mtx[i,j]), end='  ')
        print()

charge_matrix()

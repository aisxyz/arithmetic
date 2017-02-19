# coding: utf8
'''
LCS的最优子结构：设X=(x1, x2, ..., xm)和Y=(y1, y2, ..., yn)为两个序列，并
设Z=(z1, z2, ..., zk)为X和Y的任意一个LCS，则：
1）如果xm=yn，那么zk=xm=yn，而且Z(k-1)是X(m-1)和Y(n-1)的一个LCS。
2）如果xm!=yn，那么zk!=xm蕴含Z是X(m-1)和Y的一个LCS。
3）如果xm!=yn，那么zk!=yn蕴含Z是X和Y(n-1)的一个LCS。

递归式：
          { 0                           i = 0 or j = 0
c[i, j] = | c[i-1, j-1] + 1             i, j > 0, xi = yj
          { max(c[i, j-1], c[i-1, j])   i, j > 0, xi != yj
where:
c[i, j] is the length of LCS in X(i) and Y(j).
'''

def LCS_length(X, Y):
    lenX = len(X)
    lenY = len(Y)
    c = [ [0] for _ in range(lenX+1) ]
    c[0] += [0] * lenY
    b = [ [0] for _ in range(lenX+1) ]
    b[0] += [0] * lenY
    
    for i in range(1, lenX+1):
        for j in range(1, lenY+1):
            if X[i-1] == Y[j-1]:
                c[i].append( c[i-1][j-1] + 1 )
                b[i].append( '\\' )
            elif c[i-1][j] >= c[i][j-1]:
                c[i].append( c[i-1][j] )
                b[i].append('|')
            else:
                c[i].append( c[i][j-1] )
                b[i].append('-')
    return c, b


def print_LCS(b, X, lenX, lenY):
    if lenX==0 or lenY==0:
        return
    if b[lenX][lenY] == '\\':
        print_LCS(b, X, lenX-1, lenY-1)
        print(X[lenX-1], end=" ")
    elif b[lenX][lenY] == '|':
        print_LCS(b, X, lenX-1, lenY)
    else:
        print_LCS(b, X, lenX, lenY-1)

        
if __name__ == "__main__":
    x = 'abcbdab'
    y = 'bdcaba'
    c, b = LCS_length(x, y)
    '''
    import pprint
    pprint.pprint(c)
    print('\n')
    pprint.pprint(b)'''
    print_LCS(b, x, len(x), len(y))
    print()
    

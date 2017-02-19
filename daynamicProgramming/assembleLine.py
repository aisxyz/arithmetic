# coding: utf8
'''
动态规划设计步骤：
1、描述最优解的结构。
2、递归定义最优解的值。
3、按自底向上的方式计算最优解的值。
4、由计算出的结果构造一个最优解。
'''

'''
Recurrence expression:
        { e1 + a1_1                                       j = 1
g_f1[j] = |
        { min( g_f1[j-1] + a1_j, g_f2[j-1] + t2_j_1 + a1_j )  j >= 2

        { e2 + a2_1                                       j = 1
g_f2[j] = |
        { min( g_f2[j-1] + a2_j, g_f1[j-1] + t1_j_1 + a2_j )  j >= 2

f* = min( g_f1[n] + x1, g_f2[n] + x2 )

where,
1. ei is time arriving first workshop on line i (i=1, 2).
2. ai_j is time assembling in workshop j on line i (1<=j<=n).
3. xi is time out last workshop on line i.
4. fi[j] is the least costed time before arriving workshop j on line i.
5. f* is the least time at last.
'''

g_f1, g_f2 = [], []
g_track_line1, g_track_line2 = [0], [0]
g_out_line = 1

def least_time_assembling(alist, tlist, elist, xlist, n):
    global g_g_f1, g_f2, g_track_line1, g_track_line2, g_out_line
    g_f1.append( elist[0] + alist[0][0] )
    g_f2.append( elist[1] + alist[1][0] )
    for j in range(1, n):
        if g_f1[j-1]+alist[0][j] <= g_f2[j-1]+tlist[1][j-1]+alist[0][j]:
            g_f1.append( g_f1[j-1] + alist[0][j] )
            g_track_line1.append(1)
        else:
            g_f1.append( g_f2[j-1] + tlist[1][j-1] + alist[0][j] )
            g_track_line1.append(2)

        if g_f2[j-1]+alist[1][j] <= g_f1[j-1]+tlist[0][j-1]+alist[1][j]:
            g_f2.append( g_f2[j-1] + alist[1][j] )
            g_track_line2.append(2)
        else:
            g_f2.append( g_f1[j-1] + tlist[0][j-1] + alist[1][j] )
            g_track_line2.append(1)

    if g_f1[n-1]+xlist[0] <= g_f2[n-1]+xlist[1]:
        least_time = g_f1[n-1] + xlist[0]
        g_out_line = 1
    else:
        least_time = g_f2[n-1] + xlist[1]
        g_out_line = 2
    return least_time


def print_resolution_inversed(n):
    print('best resolution:')
    line = g_out_line
    print('line:', line, '\tworkshop:', n)
    for j in range(n-1, 0, -1):
        line = g_track_line1[j] if line==1 else g_track_line2[j]
        print('line:', line, '\tworkshop:', j)       

def print_resolution_forward(n, line):
    if n != 1:
        line = g_track_line1[n-1] if line==1 else g_track_line2[n-1]
        print_resolution_forward(n-1, line)
        print('line:', line, '\tworkshop:', n-1)
    
    
if __name__ == '__main__':
    num_of_workshop_one_line = 6
    timelist_to_first_workshop = [2, 4]
    timelist_out_last_workwhop = [3, 2]
    timelist_on_assembling = [ [7, 9, 3, 4, 8, 4],
                               [8, 5, 6, 4, 5, 7] ]
    timelist_to_next_workshop = [ [2, 3, 1, 3, 4],
                                  [2, 1, 2, 2, 1] ]
    least_time = least_time_assembling( timelist_on_assembling,
                                        timelist_to_next_workshop,
                                        timelist_to_first_workshop,
                                        timelist_out_last_workwhop,
                                        num_of_workshop_one_line )
    print('g_f1:', g_f1)
    print('g_f2:', g_f2)
    print('g_track_line1:', g_track_line1)
    print('g_track_line2:', g_track_line2)
    print('least_time:', least_time)
    #print_resolution_inversed(num_of_workshop_one_line)
    print_resolution_forward(num_of_workshop_one_line, g_out_line)
    print('line:', g_out_line, '\tworkshop:', num_of_workshop_one_line)
   

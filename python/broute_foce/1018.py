n,m = map(int,input().split())

rows = [['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']]
success_case = [[rows[i%2] for i in range(8)],[rows[i%2-1] for i in range(8)]]

origin = []
for _ in range(n):
    origin.append(list(input()))


result = n*m

def slice_two_dimensional_array(arr,rowStart,rowEnd,colStart,colEnd):
    return [row[colStart:colEnd] for row in arr[rowStart:rowEnd]]


for i in range(0,n-8 + 1):
    for j in range(0,m-8 + 1):
        candidate = slice_two_dimensional_array(origin, i, i+8, j, j+8);
        count = 0;  
        for k in range(8):
            for l in range(8):
                if candidate[k][l] != success_case[0][k][l]:
                    count += 1
        if count < result:
            result = count
        count = 0;
        for k in range(8):
            for l in range(8):
                if candidate[k][l] != success_case[1][k][l]:
                    count += 1
        if count < result:
            result = count

        
print(result)
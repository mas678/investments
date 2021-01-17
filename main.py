import csv
 
File = open('new.csv', newline='')
reader = list(csv.reader(File))
n = len(reader) - 1
a = [0] * n
for i in range(1,n + 1):
    a[i - 1] = float(reader[i][3])
k = int(input())
b = [[float("-inf")] * n for i in range(k)]
dp = [[float("-inf")] * n for i in range(k)]
b_max = [float("-inf")] * k
a_max = float("-inf")
for i in range(n):
    
    for m in range(k):
        if m != 0:
            dp[m][i] = max(a[i] + b_max[m - 1], dp[m][i - 1])
        else:
            dp[m][i] = max(a[i] + a_max, dp[m][i - 1])
        b[m][i] = dp[m][i] - a[i]
        b_max[m] = max(b_max[m], b[m][i])
        a_max = max(a_max, -a[i])
print(dp[-1][-1])

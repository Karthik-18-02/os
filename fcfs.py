import pandas as pd

pid = ['P1', 'P2', 'P3', 'P4', 'P5']
at = [0, 3, 4, 5, 5]
bt = [2, 4, 3, 3, 1]

n = len(pid)

for i in range(n):
    for j in range(n-i-1):
        if at[j] > at[j+1]:
            at[j], at[j+1] = at[j+1], at[j]
            pid[j], pid[j+1] = pid[j+1], pid[j]
            bt[j], bt[j+1] = bt[j+1], bt[j]


ct = []
tat = []
wt = []

for i in range(n):
    if i == 0:
        ct.append(at[0] + bt[0])
    else:
        ct.append(bt[i] + max(ct[i-1], at[i]))

for i in range(n):
    tat.append(ct[i] - at[i])
    wt.append(tat[i] - bt[i])

df2 = pd.DataFrame({'PID' : pid, 'AT' : at, 'BT' : bt, 'CT' : ct, 'TAT' : tat, 'WT' : wt})
print(df2)

avg_tat = sum(tat)/n
avg_wt = sum(wt)/n

print("avg tat is:", avg_tat)
print("avg wt is:", avg_wt)
def select_items(items, T):
    n = len(items)
    dp = [[0] * (T + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        t, v = items[i - 1]
        for j in range(T + 1):
            if t > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - t] + v)

    selected_items = []
    j = T
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(items[i - 1])
            j -= items[i - 1][0]

    # 返回结果
    return dp[n][T], selected_items


T, M = map(int, input().split())
lst = []
for _ in range(M):
    t, v = map(int, input().split())
    if t <= T:
        lst.append((t, v))

max_value, selected_items = select_items(lst, T)
print("最大价值:", max_value)
print("选取的组合:", selected_items)
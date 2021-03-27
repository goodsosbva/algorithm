def perm(arr, depth, length, end):
    if depth == end:
        print(arr[:end])
        return
    for i in range(depth, length):
        arr[i], arr[depth] = arr[depth], arr[i]
        perm(arr, depth + 1, length, end)
        arr[i], arr[depth] = arr[depth], arr[i]


def permute(pool):
    res = [pool[:]]
    idx = 0
    check = [0] * len(pool)

    while idx < len(pool):
        print(check, idx)
        if check[idx] < idx:
            if idx % 2 == 0:
                print("if", pool, idx)
                pool[0], pool[idx] = pool[idx], pool[0]
                print("if", pool, idx)
            else:
                print("else", pool, idx)
                pool[check[idx]], pool[idx] = pool[idx], pool[check[idx]]
                print("else", pool, idx)

            res.append(pool[:])
            check[idx] += 1
            idx = 0

        else:
            check[idx] = 0
            idx += 1
    return res


# perm([1, 2, 3], 0, 3, 3)
print(permute(["a", "b", "c"]))
def count_pairs_int(diff, n_max):
    div_count = 0 * n_max
    for i in range(1, n_max):
        for j in range(i, n_max, i):
            div_count[j] += 1
        count = 0
        for a in range(1, n_max - diff):
            if div_count[a] == div_count[a + diff]:
                count += 1
        return count

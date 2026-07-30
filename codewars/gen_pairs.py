


def generate_pairs(n):
    generate_list = []
    for i in range(n + 1):
        for j in range(i, n + 1):
            generate_list.append([i, j])
    return generate_list

print(generate_pairs(2))
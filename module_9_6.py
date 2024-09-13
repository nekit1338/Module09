import itertools


def all_variants(text):
    for j in range(len(text) + 1):
        for combi in itertools.combinations(text, j):
            yield ''.join(combi)


a = all_variants("abc")
for i in a:
    print(i)

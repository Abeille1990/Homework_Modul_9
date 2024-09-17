def all_variants(text):
    print(len(text))
    for l in range(len(text)):
        for p in range(len(text)-l):
            print(text[p:l+p+1])

alv = all_variants("abc")

for j in alv:
    print(j)
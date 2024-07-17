def all_variants(text):

     n = len(text)

     for i in range(n):
         for j in range(n):
             for j in range(i+1, n+1):

                 yield text[i:j]


a = all_variants("abc")
for i in a:
    print(i)

lst = [1, 2, 3]
a = all_variants(lst, 2)
for i in a:
    print(i)

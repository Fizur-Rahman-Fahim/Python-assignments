def func( **kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')   #Output: fahim : 7, kafi : 4, jashim : 15, khalid : 1

result = func(fahim = 7, kafi= 4, jashim = 15, khalid = 1)

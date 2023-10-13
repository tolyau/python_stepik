# set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75,
#          76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}
#
# set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31,
#          33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}
# print(len(set_a - set_b))
# print(len(set_b - set_a))


# set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75,
#          76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}
#
# set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31,
#          33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}
# print(set_b ^ set_a)


words = ['mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
         'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error',
         'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',
         'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',
         'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention', 'tradition',
         'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal', 'government',
         'control', 'value', 'few', 'generation', 'service', 'national',
         'tradition', 'government', 'mention', 'proposal']
print(len({i for i in words if len(i)>6}))
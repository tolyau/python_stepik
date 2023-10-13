# a,b = map(int, input().split())
# if a<=b:
#     sp = [i*i for i in range(a,b+1)]
# if a>b:
#     sp= [i**3 for i in range(b,a+1 )]
#     sp.reverse()
# print(sp)
#
#
#
# st = 'Create a list of the first letters of every word in this string'
# a = st.split()
# a = [(a[i][0]) for i in range(len(a)) ]
# print(a)

# from string import ascii_uppercase
# n = int(input())
# print([ascii_uppercase[i]*(i+1) for i in range(n)])

# phrase = 'Take only the words that start with t in this sentence'
# print([i for i in phrase.split() if i.lower()[0]=='t'])

# a = phrase.split()
# a = [a[i] for i in range(len(a)) if a[i][0]=='t' or a[i][0]=='T' ]
# print(a)

# my_tuple = (
# -214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593,
# 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829,
# -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543,
# 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370,
# 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
# a = []
# for i in my_tuple:
#     if i % 2 != 0:
#         a.append(i)
#
# print(sum(a) / len(a))


sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125,
}
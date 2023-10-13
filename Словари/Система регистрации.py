n  = int(input())
name ={}
for key in range(n):
    imy = input()
    if imy in name:
        print(f"{imy}{name[imy]}")
        name[imy]+=1
    else:
        print("OK")
        name[imy]=1



    # print(name)
    # k+=1
    # else:
    #     name.pop(key)
    #     name[key+str(k)]=k
    #     k+=1
    #     print(name)

# for i in range(1,n):
#     if name[i] in name:
#         name[i] = name[i] + str(i)
#         print(name[i])
#     else:
#         print("OK")



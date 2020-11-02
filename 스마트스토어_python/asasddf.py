a = [
    {"id" : 1, "name" : "karl"},
    {"id" : 2, "name" : "Hanna"},
    {"id" : 3, "name" : "Zimmermann"},
    {"id" : 3, "name" : "Christine"}
]
id_list = []
for i in a:
    i = i.values()
    print("i :",i)
    for j in i:
        print("j :",j)
    # if i not in id_list:
    #     id_list.append(i)
print(id_list)
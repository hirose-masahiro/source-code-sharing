print("please input authors:")

str_input = input()
str_input = str_input + ","

mylist_1 = str_input.split(' ')  # 単語区切り
mylist_2 = []  # 単語のindexのリストを入れるリスト
mylist_tmp = []  # 単語のindexを入れるリスト

# 人名を区切る
for i in range(len(mylist_1)):
    mylist_tmp.append(i)
    if mylist_1[i] == "and":
        mylist_tmp.pop()
        if not mylist_2:
            mylist_1[i - 1] += ","
            mylist_2.append(mylist_tmp.copy())
            mylist_tmp.clear()
    elif mylist_1[i][-1:] == ",":
        mylist_2.append(mylist_tmp.copy())
        mylist_tmp.clear()

str_output = ""
# 人名を加工
for i in range(len(mylist_2)):
    if len(mylist_2[i]) == 2:
        str_output += mylist_1[mylist_2[i][1]] + " " + mylist_1[mylist_2[i][0]]
        if i != len(mylist_2) - 1:
            str_output += " and "
    elif len(mylist_2[i]) > 2:
        for j in range(len(mylist_2[i]) - 2):
            str_output += mylist_1[mylist_2[i][j] + 1] + ", "
        str_output += mylist_1[mylist_2[i][-1]] + \
            " " + mylist_1[mylist_2[i][0]]
        if i != len(mylist_2) - 1:
            str_output += " and "

print()
print("authors in .bib style:")
print(str_output)

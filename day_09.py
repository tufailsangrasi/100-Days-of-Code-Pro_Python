# Dictionay in Python contains a key-value pair
prog_dic = {
  "Bug":"The values where expected output not comes",
  "Function":"Which can be called again and again"
}

# retriving the dictionary
# print(prog_dic['Bug'])
# print(prog_dic.get('Bug'))

# Empty dictionary
#prog_dic = {}

# Edit the dictionary
prog_dic["Bug"] = "Error"
prog_dic["Function"] = "makes code reusable"

# print(prog_dic['Bug'])

stu_list = {
  "22SW01":"Ahmed",
  "22SW02":"Ali",
  "22SW03":"John"
}

for key in stu_list:
  print(key,":" , stu_list[key])
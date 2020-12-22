from browser.pkulaw import pkulaw
import pymongo

print(pymongo.__file__)
'''
本文件获取'新冠肺炎'标题及链接
'''

pku = pkulaw()

#获取并存储法律
laws = pku.get_laws()
print(laws)
print(len(laws))

# 获取并存储行政法规
rules = pku.get_rules()
print(rules)
print(len(rules))

# 获取并存储司法解释
justices = pku.get_justices()
print(justices)
print(len(justices))
'''
'''
# 获取并存储部门规章，部门规章第2页之后需要手动验证滑块
dept = pku.get_depts()
print(dept)
print(len(dept))
'''
'''
# 获取并存储党内法规
party = pku.get_parties()
print(party)
print(len(party))
'''
# 获取并存储团体规定
groups = pku.get_groups()
print(groups)
print(len(groups))
'''
# 获取并存储行业规定
industries = pku.get_industries()
print(industries)
print(len(industries))

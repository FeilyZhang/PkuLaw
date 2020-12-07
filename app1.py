from mongodb import mongodb
from parsing import parsing

'''
本文件根据链接获取元数据及正文
'''

# 获取并存储法律
for ele in mongodb().find_all('pkulaw', 'law'):
    print(parsing().get_html(ele).get_json(mongodb(), 'pkulaw', 'law_detail'))

# 获取并存储行政法规
for ele in mongodb().find_all('pkulaw', 'rule'):
    print(parsing().get_html(ele).get_json(mongodb(), 'pkulaw', 'rule_detail'))

# 获取并存储司法解释
for ele in mongodb().find_all('pkulaw', 'justice'):
    print(parsing().get_html(ele).get_json(mongodb(), 'pkulaw', 'justice_detail'))

# 获取并存储部门规章
for ele in mongodb().find_all('pkulaw', 'dept'):
   print(parsing().get_html(ele).get_json(mongodb(), 'pkulaw', 'dept_detail'))

# 获取并存储党内法规
for ele in mongodb().find_all('pkulaw', 'party'):
    print(parsing().get_html(ele).get_json(mongodb(), 'pkulaw', 'party_detail'))

# 获取并存储团体规定
for ele in mongodb().find_all('pkulaw', 'group'):
   print(parsing().get_html(ele).get_json(mongodb(), 'pkulaw', 'group_detail'))

# 获取并存储行业规定
for ele in mongodb().find_all('pkulaw', 'industry'):
   print(parsing().get_html(ele).get_json(mongodb(), 'pkulaw', 'industry_detail'))
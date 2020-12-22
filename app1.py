from mongodb.mongodb import mongodb
from parsing.parsing import parsing

'''
本文件根据链接获取元数据及正文
'''
'''
# 获取并存储法律
for ele in mongodb().find_all('pkulaw1', 'law'):
    print(parsing().get_html(ele).get_json(mongodb(), 'pkulaw1', 'law_details'))

# 获取并存储行政法规
for ele in mongodb().find_all('pkulaw1', 'rule'):
    print(parsing().get_html(ele).get_json(mongodb(), 'pkulaw1', 'rule_details'))

# 获取并存储司法解释
for ele in mongodb().find_all('pkulaw1', 'justice'):
    print(parsing().get_html(ele).get_json(mongodb(), 'pkulaw1', 'justice_details'))
'''

# 获取并存储部门规章
for ele in mongodb().find_all('pkulaw1', 'dept'):
   print(parsing().get_html(ele).get_json(mongodb(), 'pkulaw1', 'dept_details'))

# 获取并存储党内法规
for ele in mongodb().find_all('pkulaw1', 'party'):
    print(parsing().get_html(ele).get_json(mongodb(), 'pkulaw1', 'party_details'))
'''
# 获取并存储团体规定
for ele in mongodb().find_all('pkulaw', 'group'):
   print(parsing().get_html(ele).get_json(mongodb(), 'pkulaw1', 'group_detail'))
'''
# 获取并存储行业规定
for ele in mongodb().find_all('pkulaw1', 'industry'):
   print(parsing().get_html(ele).get_json(mongodb(), 'pkulaw1', 'industry_details'))

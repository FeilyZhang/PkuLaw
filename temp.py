from mongodb import mongodb

for ele in mongodb().find_all('pkulaw', 'justice_detail'):
    rst = ''
    for ele in ele['dept']:
        rst += ele
    print(rst)
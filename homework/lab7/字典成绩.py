
# (1)
my_dist = {"数学":101, "语文":202, "英语":203, "物理":204,"生物":206}

# (2)
my_dist['化学'] = 205

# (3)
my_dist['数学'] = 201

# (4)
del my_dist['生物']

# (5)
for key,value in my_dist.items():
    print(f'{value}:{key}',end=' || ')
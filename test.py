__author__ = 'mark_ts'
movie_data = open('movie_name.txt', 'r')
temp = movie_data.read().splitlines()
for i in temp:
    print i
#movie_name = dict( (i,j) for i,j in [map(lambda x=i[-3:]: x, i.split(',')) for i in movie_data.readlines()])

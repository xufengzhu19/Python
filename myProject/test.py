import redis

def test():
    host='r-bp1cdfadc2590b24.redis.rds.aliyuncs.com'
    port=6379
    pwd='Xu123@com'
    r=redis.StrictRedis(host=host,port=port,password=pwd)
    r.set('t','test')
    print(r.get('t'))



if __name__ == '__main__':
    test()
#! /usr/bin/env python
import redis

def incr_test():
    r = redis.StrictRedis(host="127.0.0.1", port=16379, db = 0)
    pipe = r.pipeline(transaction=False)
    pipe.hincrby("hash1", "field2", long(1.022))
    #pipe.hincrbyfloat("hash1", "field1", 1.2)
    result = pipe.execute()
    print result

if __name__ == "__main__":
    incr_test()

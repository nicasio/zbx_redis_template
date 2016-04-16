import sys, redis, json, re, struct, time, socket, argparse



client = redis.StrictRedis(host='localhost')


for i in  client.scan_iter('*'):
    print i
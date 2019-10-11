import memcache
connect = memcache.Client(["127.0.0.1:11211"])
connect.set("key", "Hello, world!")
print(connect.get("key"))
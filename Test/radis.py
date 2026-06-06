import redis

print("Attempting to connect...")

try:
    r = redis.Redis(
        host="localhost",
        port=6379,
        decode_responses=True,
        socket_connect_timeout=5,  # seconds
        socket_timeout=5
    )

    print("Sending PING...")
    print("PING:", r.ping())
    print("Redis is running!")

except Exception as e:
    print("Redis is NOT running")
    print(type(e).__name__)
    print(e)
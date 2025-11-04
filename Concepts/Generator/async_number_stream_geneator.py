"""
8) -------- Async number stream
Write an asynchronous generator async_numbers(limit, delay) that yields numbers 
from 0 up to limit-1, awaiting asyncio.sleep(delay) between each emission. Then 
write an async def main() that consumes the stream with async for and prints each received number.
"""
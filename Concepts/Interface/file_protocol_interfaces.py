"""
Exercise ----- 2 ----  File-Like Protocol
    Define a protocol named Writable that requires a write(data: bytes) -> int method and a flush() -> None method. 
    Implement two classes that satisfy the protocol:

    SimpleFileWriter that wraps a real file object opened in binary mode.
    MemoryBuffer that stores written bytes in a bytearray.
    Write a function dump(writer: Writable, payload: bytes) that writes the payload and then flushes. Test the function with both implementations.
Hints
    Import Protocol from typing.
    For the in-memory version, write can simply extend the buffer and return the length of the incoming data.
"""

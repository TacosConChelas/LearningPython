"""
Exercise -------- 5 ---------- Protocol with Runtime Check

Create a runtime-checkable protocol SupportsClose that defines a single method close() -> None. Implement two classes:

    NetworkConnection with a close method that prints “Connection closed”.
    FakeResource that does not implement close.

Write a helper is_closeable(obj: object) -> bool that returns True when obj satisfies the protocol (using isinstance). 
Test it with both classes and with a plain integer.
Hints
    Decorate the protocol with @runtime_checkable.
"""
"""
10) --------- Composable decorator pipeline
Implement a helper compose(*decorators) that returns a single decorator applying the 
supplied decorators from left to right. For example, @compose(log_calls, timer, call_counter) should 
cause a function to be logged, timed, and counted, all with one @ line. The implementation 
typically reverses the decorator list and applies each one to the function in turn.
"""
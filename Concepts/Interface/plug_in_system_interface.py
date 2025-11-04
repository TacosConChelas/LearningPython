"""
Exercise ---- 3 ----- Plug-in System with ABC

Design a tiny plug-in framework:

    An abstract base class Plugin with abstract methods initialize(app) and shutdown().
    Two concrete plug-ins: LoggerPlugin (writes a start/end message to a log file) and MetricsPlugin (stores a counter in a dictionary).

Create a minimal App class that can register plugins, call initialize on all of them, and later call shutdown. 
Demonstrate the flow by registering both plug-ins and running the app.
Hints
    Store plugins in a list inside App.
    initialize can receive the App instance so the plug-in can access shared state.
"""
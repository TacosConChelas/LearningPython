"""
Exercise ------ 4 -------  Duck-Typed GUI Widgets

Without declaring any interface, write a function render(widget) that expects the widget to have 
two methods: draw() and resize(width, height). Then create two unrelated classes:

    Button with draw printing “Button drawn” and resize storing dimensions.
    Image with draw printing “Image displayed” and resize adjusting an internal size tuple.

Pass instances of both classes to render and verify that it works. 
Afterwards, intentionally pass an object lacking one of the methods and observe the resulting AttributeError.
Hints
    This exercise illustrates pure duck typing.
"""
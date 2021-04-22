from flask import Flask
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

outer_function()
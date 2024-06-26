def print_hello_world(name: str, *, additional_text: str = ""):
    """
    Top level function to print hello world message.

    **Arguments:**

    - `name: str`: Name of the person to greet.
    - `additional_text: str`: Additional text to append to the message.

    **Returns:**

    - None
    """
    print(f"Hello, {name}! {additional_text}")
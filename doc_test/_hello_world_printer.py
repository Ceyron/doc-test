def print_hello_world(name: str, *, additional_text: str = ""):
    """
    Top level function to print hello world message.

    *Arguments*:
        - name: Name of the person to greet.
        - additional_text: Additional text to append to the message.

    *Returns*:
        - None
    """
    print(f"Hello, {name}! {additional_text}")
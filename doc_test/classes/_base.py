from typing import Any


class MyBaseClass():
    text: str

    def __init__(
        self,
        text: str,
    ):
        """
        Base class to store text.

        **Arguments:**

        - `text: str`: Text to store.
        """
        self.text = text

    def __call__(self):
        """
        Print stored text.

        **Arguments:**

        - None

        **Returns:**

        - None
        """
        print(self.text)
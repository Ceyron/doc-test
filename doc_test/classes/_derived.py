from ._base import MyBaseClass

class MyDerivedClass(MyBaseClass):
    additional_text: str

    def __init__(
        self,
        text: str,
        additional_text: str,
    ):
        """
        Derived class to store text and additional text.

        **Arguments:**

        - `text: str`: Text to store.
        - `additional_text: str`: Additional text to store.
        """
        super().__init__(text)
        self.additional_text = additional_text

    def __call__(self):
        """
        Print stored text and additional text.

        **Arguments:**

        - None

        **Returns:**

        - None
        """
        print(f"{self.text} {self.additional_text}")
        
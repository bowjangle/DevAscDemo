class MyFeature:
    """A basic feature class with a simple text transformation."""

    def __init__(self, name: str = "MyFeature"):
        self.name = name

    def transform(self, text: str) -> str:
        """Return the input text with a basic transformation applied."""
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        return text.strip().title()


def main() -> None:
    feature = MyFeature()
    sample_text = "   hello from my feature   "
    print(feature.transform(sample_text))


if __name__ == "__main__":
    main()
print("welcome brotha")
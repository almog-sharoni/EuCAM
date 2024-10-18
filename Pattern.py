
class Pattern:
    """
    Represents a binary pattern.
    """
    def __init__(self, binary_str: str):
        self.binary_str = binary_str

    def __str__(self):
        return self.binary_str

    def __eq__(self, other):
        return self.binary_str == other.binary_str

    def __hash__(self):
        return hash(self.binary_str)
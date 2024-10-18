from typing import Set
from Pattern import Pattern
class CAMMemory:
    """
    Represents the CAM storage.
    """
    def __init__(self):
        self.patterns: Set[Pattern] = set()

    def add_pattern(self, pattern: str):
        """
        Adds a binary pattern to the CAM memory.
        """
        self.patterns.add(Pattern(pattern))

    def get_patterns(self) -> Set[Pattern]:
        """
        Retrieves all patterns stored in the CAM memory.
        """
        return self.patterns
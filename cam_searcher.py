from typing import List

from cam_memory import CAMMemory
from query_masker import QueryMasker


class CAMSearcher:
    """
    Searches the CAM for patterns that match a query with a specified tolerance.
    """
    def __init__(self, cam_memory: CAMMemory, masker: QueryMasker):
        self.cam_memory = cam_memory
        self.masker = masker

    def search(self, query: str) -> List[str]:
        """
        Search the CAM memory for matches based on the masked patterns.
        """
        masked_patterns = self.masker.generate(query)
        matches = [
            str(pattern) for pattern in self.cam_memory.get_patterns()
            if pattern.binary_str in masked_patterns
        ]
        return matches
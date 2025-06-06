"""Domain entities for health records."""
from datetime import datetime

class HealthRecord:
    """represents a health record with a device ID, BPM, and timestamp.
       Attributes:
            id (int): Unique identifier for the health record.
            device_id (str): Identifier for the device that recorded the BPM.
            bpm (float): Beats per minute recorded by the device.
            created_at (datetime): Timestamp when the record was created.
    """
    def __init__(self, device_id: str, bpm: float, created_at: datetime, id: int = None):
        """initializes a HealthRecord instance.
        Args:
            device_id (str): Identifier for the device that recorded the BPM.
            bpm (float): Beats per minute recorded by the device.
            created_at (datetime): Timestamp when the record was created.
            id (int, optional): Unique identifier for the health record. Defaults to None.
        """
        self.id = id
        self.device_id = device_id
        self.bpm = bpm
        self.created_at = created_at

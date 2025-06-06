"""Application services for managing health records."""
from health.domain.entities import HealthRecord
from health.domain.services import HealthRecordService
from health.infrastructure.repositories import HealthRecordRepository
from iam.infrastructure.repositories import DeviceRepository


class HealthRecordApplicationService:
    """Service for managing health records."""
    def __init__(self):
        """Initialize the health record application service."""
        self.health_record_repository = HealthRecordRepository()
        self.health_record_service = HealthRecordService()
        self.device_repository = DeviceRepository()

    def create_health_record(self, device_id: str, bpm: float, created_at: str, api_key: str) -> HealthRecord:
        """
        create a new health record.
            Arguments:
                device_id (str): The ID of the device.
                bpm (float): The beats per minute value.
                created_at (str): The timestamp when the record was created.
                api_key (str): The API key for authentication.
            Returns:
                HealthRecord: The created health record.
            Raises:
                ValueError: If the device ID or API key is invalid.
        """        
        if not self.device_repository.find_by_id_and_api_key(device_id, api_key):
            raise ValueError("Invalid device ID or API key")
        record = self.health_record_service.create_record(device_id, bpm, created_at)
        return self.health_record_repository.save(record)
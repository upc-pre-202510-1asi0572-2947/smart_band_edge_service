"""Repository for Health Records."""
from health.domain.entities import HealthRecord
from health.infrastructure.models import HealthRecord as HealthRecordModel

class HealthRecordRepository:
    """
    Repository for Health Records.
    """
    @staticmethod
    def save(health_record) -> HealthRecord:
        """
        Save a health record to the database.
            Arguments:
                health_record (HealthRecord): The health record to save.
            Returns:
                HealthRecord: The saved health record with its ID.
        """
        record = HealthRecordModel.create(
            device_id   = health_record.device_id,
            bpm         = health_record.bpm,
            created_at  = health_record.created_at
        )
        return HealthRecord(
            health_record.device_id,
            health_record.bpm,
            health_record.created_at,
            record.id
        )
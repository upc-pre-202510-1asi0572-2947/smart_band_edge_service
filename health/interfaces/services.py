"""Interfaces for health record services."""
from flask import Blueprint, request, jsonify
from health.application.services import HealthRecordApplicationService
from iam.interfaces.services import authenticate_request

health_api = Blueprint("health_api", __name__)

health_record_service = HealthRecordApplicationService()

@health_api.route("/api/v1/health-monitoring/data-records", methods=["POST"])
def create_health_record():
    """Create a new health record.
    This endpoint allows devices to submit health records with their device ID,
    beats per minute (bpm), and an optional timestamp for when the record was created.
    The request must include a valid device ID and API key in the headers.
    Returns:
        JSON response with the created health record details or an error message.
    """
    auth_result = authenticate_request()
    if auth_result:
        return auth_result
    data = request.json
    try:
        device_id = data["device_id"]
        bpm = data["bpm"]
        created_at = data.get("created_at")
        record = health_record_service.create_health_record(
            device_id, bpm, created_at, request.headers.get("X-API-Key")
        )
        return jsonify({
            "id": record.id,
            "device_id": record.device_id,
            "bpm": record.bpm,
            "created_at": record.created_at.isoformat() + "Z"
        }), 201
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


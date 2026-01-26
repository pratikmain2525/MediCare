# core/configs/utils.py
from pathlib import Path
from fastapi import UploadFile
import uuid


def save_profile_picture(
    file: UploadFile,
    base_path: str,
    entity: str,     # "doctor" | "patient"
    entity_id: int,
    old_path: str | None = None,  # optional old file path to delete
) -> str:
    # Delete old file if exists
    if old_path:
        old_file = Path(base_path) / old_path
        if old_file.exists():
            old_file.unlink()

    # Get extension
    ext = file.filename.rsplit(".", 1)[-1].lower()
    filename = f"{entity}_{entity_id}.{ext}"

    # Prepare directory (base_path points to storeg/static)
    subfolder = f"{entity}s"
        
    upload_dir = Path(base_path) / "uploads" / subfolder
    upload_dir.mkdir(parents=True, exist_ok=True)

    # Save file
    file_path = upload_dir / filename
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    # Return relative path to store in DB
    return f"uploads/{subfolder}/{filename}"



def generate_transaction_id() -> str:
    """
    Generate demo transaction ID
    Example: TXN-9f3a2c1e
    """
    return f"TXN-{uuid.uuid4().hex[:8].upper()}"


from fastapi import APIRouter, File, HTTPException, UploadFile

from app.api.services.ingestion_pipeline import get_ingestion_pipeline
from app.dependencies import get_vs

ingest_router = APIRouter()


@ingest_router.post("/ingest")
async def ingest(file: UploadFile = File(...)):
    """Reads md file for ingestion"""

    if not file.filename.endswith(".md"):
        raise HTTPException(
            status_code=400, detail="Only markdown files can be ingested")

    content = await file.read()

    try:
        # bytes to string
        text = content.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise HTTPException(status_code=400, detail="Invalid file!") from exc

    if not text:
        raise HTTPException(status_code=400, detail="Empty file!")

    ingestion_pipeline = get_ingestion_pipeline()

    chunks = ingestion_pipeline.run(text)

    return {"status": "ok", "chunks_count": len(chunks)}

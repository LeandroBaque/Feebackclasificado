# app/routers/feedback_api.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.config.db import SessionLocal
from app.models.feedback import Feedback
from app.crud.feedback import save_feedback
from sqlalchemy import func
from ml_models.ml_pipeline import analyze_feedback

router = APIRouter()

class FeedbackInput(BaseModel):
    text: str
    source_id: int
    external_id: str | None = None


def feedback_to_dict(feedback: Feedback) -> dict:
    return {
        "id": feedback.id,
        "text_original": feedback.text_original,
        "source_id": feedback.source_id,
        "external_id": feedback.external_id,
        "channel": feedback.channel,
        "text_clean": feedback.text_clean,
        "received_at": feedback.received_at.isoformat() if feedback.received_at else None,
        "analyzed_at": feedback.analyzed_at.isoformat() if feedback.analyzed_at else None,
        "sentiment_label": feedback.sentiment_label,
        "sentiment_score": feedback.sentiment_score,
        "urgency_label": feedback.urgency_label,
        "urgency_score": feedback.urgency_score,
        "category_label": feedback.category_label,
        "category_score": feedback.category_score,
        "is_training_sample": feedback.is_training_sample,
        "extra_metadata": feedback.extra_metadata,
        "created_by": feedback.created_by,
    }

# --- SCRUM 27 ---
@router.post("/feedback/submit")
def submit_feedback(data: FeedbackInput):
    ml = analyze_feedback(data.text)
    saved = save_feedback(data, ml)
    return {"feedback_id": saved.id, "analysis": ml}


# --- SCRUM 28 ---
@router.get("/feedback/data")
def get_feedback(sentiment: str | None = None,
                 category: str | None = None,
                 urgency: str | None = None,
                 limit: int = 100):

    db = SessionLocal()
    q = db.query(Feedback)

    if sentiment:
        q = q.filter(Feedback.sentiment_label == sentiment)
    if category:
        q = q.filter(Feedback.category_label == category)
    if urgency:
        q = q.filter(Feedback.urgency_label == urgency)

    rows = q.order_by(Feedback.analyzed_at.desc()).limit(limit).all()
    return [feedback_to_dict(row) for row in rows]


# --- SCRUM 29 ---
@router.get("/feedback/summary")
def summary():
    db = SessionLocal()

    total = db.query(func.count(Feedback.id)).scalar()

    sentiment = dict(db.query(
        Feedback.sentiment_label,
        func.count(Feedback.id)
    ).group_by(Feedback.sentiment_label))

    category = dict(db.query(
        Feedback.category_label,
        func.count(Feedback.id)
    ).group_by(Feedback.category_label))

    urgency = dict(db.query(
        Feedback.urgency_label,
        func.count(Feedback.id)
    ).group_by(Feedback.urgency_label))

    return {
        "total": total,
        "sentiment": sentiment,
        "category": category,
        "urgency": urgency
    }


# --- SCRUM 30 ---
import csv, tempfile
from fastapi.responses import FileResponse

@router.get("/feedback/export")
def export_feedback():
    db = SessionLocal()
    rows = db.query(Feedback).all()

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    with open(tmp.name, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "id","text_original","sentiment_label","sentiment_score",
            "urgency_label","urgency_score","category_label","category_score","received_at"
        ])
        for r in rows:
            w.writerow([
                r.id, r.text_original, r.sentiment_label, r.sentiment_score,
                r.urgency_label, r.urgency_score, r.category_label, r.category_score, r.received_at
            ])

    return FileResponse(tmp.name, filename="feedback_export.csv")

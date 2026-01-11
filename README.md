# Database Referee

A tiny FastAPI app that recommends a database (RDS, DynamoDB, or Aurora) based on three simple answers, and explains the trade-offs.

## Screenshots

| Input Form | Results Page |
| :---: | :---: |
| ![Input Form](app/image/input.png) |
| ![Results Page](app/image/output.png) |

## Quickstart

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the API:

```
uvicorn app.main:app --reload
```

3. Open the form in your browser:

```
http://127.0.0.1:8000
```

Submit your answers and the API returns the recommendation plus the reasoning.

## Project layout

- `app/data.py` — database scores (facts only)
- `app/logic.py` — scoring logic
- `app/explanations.py` — trade-offs text
- `app/main.py` — FastAPI endpoints and simple HTML form
- `requirements.txt` — Python deps
- `.kiro/notes.txt` — placeholder for your notes

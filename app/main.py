from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from app.logic import evaluate_databases
from app.explanations import explain

# FastAPI application structure designed with Kiro
# Complete implementation from routes to HTML developed collaboratively
app = FastAPI(title="Database Referee")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>Database Referee</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #fca311; color: #14213d; padding: 2rem; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 2rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            h1 { color: #14213d; border-bottom: 2px solid #fca311; padding-bottom: 1rem; }
            h2 { color: #14213d; margin-top: 0; }
            label { display: block; margin-top: 1rem; font-weight: bold; }
            select { width: 100%; padding: 10px; margin-top: 5px; border-radius: 5px; border: 1px solid #ccc; font-size: 1rem; }
            button { display: block; width: 100%; background-color: #14213d; color: white; padding: 15px; border: none; border-radius: 5px; margin-top: 2rem; font-size: 1.2rem; cursor: pointer; font-weight: bold; }
            button:hover { background-color: #fca311; color: #14213d; }
            .hero { text-align: center; margin-bottom: 2rem; }
            .hero p { color: #666; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="hero">
                <h1>Database Referee</h1>
                <p>Answer 3 simple questions to find the perfect AWS database.</p>
            </div>
            
            <form method="post" action="/evaluate">
              <label>Is your traffic spiky / unpredictable?</label>
              <select name="traffic">
                <option value="yes">Yes, it varies wildly</option>
                <option value="no">No, it's consistent</option>
              </select>

              <label>Do you need complex SQL queries (joins, aggregations)?</label>
              <select name="complex">
                <option value="yes">Yes, complex reporting needed</option>
                <option value="no">No, mostly simple lookups</option>
              </select>

              <label>Is your team new to database operations?</label>
              <select name="beginner">
                <option value="yes">Yes, we want minimal ops</option>
                <option value="no">No, we have DBAs</option>
              </select>

              <button type="submit">Compare Options</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.post("/evaluate", response_class=HTMLResponse)
def evaluate(
    traffic: str = Form(...),
    complex: str = Form(...),
    beginner: str = Form(...)
):
    best, scores = evaluate_databases(traffic, complex, beginner)
    explanation = explain(best)

    # Generate Score Rows
    score_rows = ""
    for db, score in scores.items():
        score_rows += f"<tr><td>{db}</td><td>{score}</td></tr>"

    # Generate Why List
    why_list = "".join([f"<li>{item}</li>" for item in explanation["why"]])

    # Generate Trade-offs List
    tradeoffs_list = "".join([f"<li>{item}</li>" for item in explanation["tradeoffs"]])

    return f"""
    <html>
    <head>
        <title>Database Referee - Results</title>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #fca311; color: #14213d; padding: 2rem; }}
            .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 2rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
            h1 {{ color: #14213d; border-bottom: 2px solid #fca311; padding-bottom: 1rem; }}
            h2 {{ color: #e5e5e5; background: #14213d; padding: 0.5rem 1rem; border-radius: 5px; margin-top: 2rem; }}
            .winner-banner {{ background-color: #e5e5e5; color: #14213d; padding: 1.5rem; border-radius: 8px; text-align: center; margin-bottom: 2rem; border: 2px solid #14213d; }}
            .winner-banner h1 {{ border: none; padding: 0; margin: 0; font-size: 2.5rem; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 1rem; }}
            th, td {{ text-align: left; padding: 12px; border-bottom: 1px solid #ddd; }}
            th {{ background-color: #14213d; color: white; }}
            tr:hover {{ background-color: #f5f5f5; }}
            .btn {{ display: inline-block; background-color: #14213d; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin-top: 2rem; font-weight: bold; }}
            .btn:hover {{ background-color: #fca311; color: #14213d; }}
            ul {{ line-height: 1.6; }}
            li {{ margin-bottom: 0.5rem; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="winner-banner">
                <small>RECOMMENDED DATABASE</small>
                <h1>{best}</h1>
            </div>

            <h2>Why {best}?</h2>
            <ul>
                {why_list}
            </ul>

            <h2>Trade-offs to Consider</h2>
            <ul>
                {tradeoffs_list}
            </ul>

            <h2>Score Comparison</h2>
            <table>
                <thead>
                    <tr>
                        <th>Database</th>
                        <th>Score</th>
                    </tr>
                </thead>
                <tbody>
                    {score_rows}
                </tbody>
            </table>

            <a href="/" class="btn">Compare Again</a>
        </div>
    </body>
    </html>
    """

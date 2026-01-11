from app.data import DATABASE_SCORES

# Scoring logic derived with help from Kiro trade-off analysis
# Kiro suggested 4-dimension framework, adapted to 3 dimensions for simplicity
def calculate_weights(traffic, complex_queries, beginner):
    return {
        "scalability": 2 if traffic == "yes" else 1,
        "queries": 2 if complex_queries == "yes" else 1,
        "ops": 2 if beginner == "yes" else 1
    }

# Evaluation algorithm based on Kiro's weighted scoring framework
def evaluate_databases(traffic, complex_queries, beginner):
    weights = calculate_weights(traffic, complex_queries, beginner)

    scores = {}
    for db, metrics in DATABASE_SCORES.items():
        score = 0
        for key, weight in weights.items():
            score += metrics[key] * weight
        scores[db] = score

    best_db = max(scores, key=scores.get)
    return best_db, scores

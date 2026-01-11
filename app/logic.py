from app.data import DATABASE_SCORES

def calculate_weights(traffic, complex_queries, beginner):
    return {
        "scalability": 2 if traffic == "yes" else 1,
        "queries": 2 if complex_queries == "yes" else 1,
        "ops": 2 if beginner == "yes" else 1
    }

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

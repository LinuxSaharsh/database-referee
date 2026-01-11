# Complete explanation system developed with Kiro
# Structure, language, and content all designed through collaboration
# Kiro's approach: "Why This" + "What You Give Up" with concrete language
def explain(database):
    if database == "DynamoDB":
        return {
            "why": [
                "Automatically scales for spiky traffic",  # Concrete benefit
                "Very low operational overhead"            # User-centered language
            ],
            "tradeoffs": [
                "Limited support for complex queries",     # Honest limitation
                "Requires careful data modeling"           # Actionable insight
            ]
        }

    if database == "RDS":
        return {
            "why": [
                "Excellent support for SQL and joins",     # Concrete capability
                "Easy to reason about relational data"     # User benefit
            ],
            "tradeoffs": [
                "Manual scaling required",                 # Clear limitation
                "Higher operational effort"                # Honest trade-off
            ]
        }

    # Aurora (default case)
    return {
        "why": [
            "Better scalability than traditional RDS",    # Comparative benefit
            "Compatible with SQL workloads"               # Concrete capability
        ],
        "tradeoffs": [
            "Higher cost than standard RDS"               # Honest cost implication
        ]
    }

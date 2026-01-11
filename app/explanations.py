def explain(database):
    if database == "DynamoDB":
        return {
            "why": [
                "Automatically scales for spiky traffic",
                "Very low operational overhead"
            ],
            "tradeoffs": [
                "Limited support for complex queries",
                "Requires careful data modeling"
            ]
        }

    if database == "RDS":
        return {
            "why": [
                "Excellent support for SQL and joins",
                "Easy to reason about relational data"
            ],
            "tradeoffs": [
                "Manual scaling required",
                "Higher operational effort"
            ]
        }

    return {
        "why": [
            "Better scalability than traditional RDS",
            "Compatible with SQL workloads"
        ],
        "tradeoffs": [
            "Higher cost than standard RDS"
        ]
    }

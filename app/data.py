# Database characteristics and scoring developed with Kiro
# Complete 1-5 framework designed through collaborative analysis
DATABASE_SCORES = {
    "RDS": {
        "scalability": 3,  # Manual scaling required
        "queries": 5,      # Full SQL support
        "ops": 3          # Moderate operational overhead
    },
    "DynamoDB": {
        "scalability": 5,  # Automatic scaling
        "queries": 2,      # Limited query flexibility  
        "ops": 5          # Fully managed
    },
    "Aurora": {
        "scalability": 4,  # Good auto-scaling
        "queries": 5,      # SQL compatible
        "ops": 4          # Managed with some config
    }
}

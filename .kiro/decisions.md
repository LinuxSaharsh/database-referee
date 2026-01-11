# Architecture Decisions Made with Kiro

## Decision 1: Weighted Scoring System

**Problem**: How to objectively compare databases with different strengths?

**Kiro's Guidance**: Use a weighted scoring system where user answers determine the importance of each factor (scalability, query complexity, operational overhead).

**Implementation**: 
- `calculate_weights()` function in `app/logic.py`
- Dynamic weighting based on user priorities
- Transparent scoring that users can understand

## Decision 2: Three-Question Approach

**Problem**: Database selection involves dozens of factors - how to simplify?

**Kiro's Analysis**: Focus on the three most decisive factors:
1. Traffic predictability (affects scaling needs)
2. Query complexity (SQL vs NoSQL decision)
3. Team expertise (operational overhead tolerance)

**Implementation**: 
- Simple HTML form with three dropdowns
- Each question maps to a specific scoring dimension

## Decision 3: Explanation Strategy

**Problem**: How to help users understand why a database was recommended?

**Kiro's Approach**: 
- Separate "why this is good" from "what you're giving up"
- Use concrete, actionable language
- Avoid technical jargon

**Implementation**:
- `explain()` function returns structured explanations
- "Why" section highlights strengths
- "Trade-offs" section acknowledges limitations

## Decision 4: Database Scoring Matrix

**Problem**: How to quantify subjective database characteristics?

**Kiro's Framework**: Rate each database 1-5 on key dimensions:
- **Scalability**: How well it handles traffic spikes
- **Queries**: Support for complex SQL operations  
- **Ops**: Operational overhead and maintenance

**Implementation**: `DATABASE_SCORES` in `app/data.py`

```python
# Scores refined through Kiro analysis
DATABASE_SCORES = {
    "RDS": {"scalability": 3, "queries": 5, "ops": 3},
    "DynamoDB": {"scalability": 5, "queries": 2, "ops": 5}, 
    "Aurora": {"scalability": 4, "queries": 5, "ops": 4}
}
```
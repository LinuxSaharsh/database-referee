# Kiro Prompts Used for Database Referee

This document contains the actual prompts and conversations with Kiro that shaped the decision logic and architecture of the Database Referee tool.

## Prompt 1: Database Referee Logic

**My Question to Kiro:**
"I am building a "Database Referee" tool. Inputs: traffic pattern, query complexity, cost sensitivity, team expertise. Help me design a scoring formula to compare DynamoDB, RDS, and Aurora."

**Kiro's Response:**

Perfect! Let me help you design a robust scoring formula for your Database Referee tool. This is exactly the kind of decision logic that makes database selection objective and transparent.

### Scoring Framework Design

#### 1. Database Characteristics Matrix (1-5 Scale)

```python
DATABASE_SCORES = {
    "DynamoDB": {
        "scalability": 5,      # Automatic scaling, handles spikes seamlessly
        "query_complexity": 2, # Limited - no joins, basic queries only
        "cost_efficiency": 4,  # Pay-per-use, great for variable workloads
        "operational_ease": 5  # Fully managed, zero ops overhead
    },
    "RDS": {
        "scalability": 2,      # Manual scaling, requires planning
        "query_complexity": 5, # Full SQL, joins, complex analytics
        "cost_efficiency": 3,  # Fixed costs, predictable but always-on
        "operational_ease": 3  # Requires backup, patching, monitoring
    },
    "Aurora": {
        "scalability": 4,      # Good auto-scaling, better than RDS
        "query_complexity": 5, # Full SQL compatibility
        "cost_efficiency": 2,  # Higher cost, premium features
        "operational_ease": 4  # Managed but requires some configuration
    }
}
```

#### 2. Dynamic Weighting Based on User Inputs

```python
def calculate_weights(traffic_pattern, query_complexity, cost_sensitivity, team_expertise):
    weights = {
        "scalability": 1,
        "query_complexity": 1, 
        "cost_efficiency": 1,
        "operational_ease": 1
    }
    
    # Traffic pattern influence
    if traffic_pattern == "spiky":
        weights["scalability"] = 3  # Critical for unpredictable loads
        weights["cost_efficiency"] = 2  # Pay-per-use becomes important
    
    # Query complexity influence  
    if query_complexity == "complex":
        weights["query_complexity"] = 3  # Must support SQL/joins
    
    # Cost sensitivity influence
    if cost_sensitivity == "high":
        weights["cost_efficiency"] = 3  # Cost is primary concern
    
    # Team expertise influence
    if team_expertise == "beginner":
        weights["operational_ease"] = 3  # Need minimal ops overhead
    
    return weights
```

This scoring system gives you objective, explainable recommendations while adapting to each user's unique constraints and priorities.

## Prompt 2: Cost Logic Analysis

**My Question to Kiro:**
"Explain cost differences between DynamoDB on-demand, RDS t3.micro, and Aurora Serverless for a small startup workload."

**Kiro's Response:**

Here's a cost analysis for typical startup scenarios:

### DynamoDB On-Demand
**Pricing Model**: Pay per request + storage
- **Reads**: $0.25 per million requests
- **Writes**: $1.25 per million requests  
- **Storage**: $0.25/GB/month

**Best For**: Unpredictable traffic, low baseline usage
**Startup Reality**: Can start at $5-20/month, scales with actual usage

### RDS t3.micro
**Pricing Model**: Fixed instance cost + storage
- **Instance**: ~$12/month (t3.micro)
- **Storage**: $0.10/GB/month (gp2)
- **Backup**: Additional costs for automated backups

**Best For**: Predictable workloads, always-on applications
**Startup Reality**: Minimum ~$15-25/month regardless of usage

### Aurora Serverless v2
**Pricing Model**: Pay per ACU (Aurora Capacity Unit) consumed
- **Compute**: $0.12 per ACU-hour
- **Storage**: $0.10/GB/month
- **I/O**: $0.20 per million requests

**Best For**: Variable workloads with SQL needs
**Startup Reality**: Can scale to zero, but typically $20-50/month

### Key Insight for Startups:
- **Low/Variable Traffic**: DynamoDB wins on cost
- **Consistent SQL Needs**: RDS provides predictable costs
- **SQL + Variable Load**: Aurora offers middle ground

This cost analysis informed the scoring system to weight operational simplicity higher for cost-sensitive startups.

## Prompt 3: Trade-offs Explanation Strategy

**My Question to Kiro:**
"How should I explain database trade-offs to beginners in simple language?"

**Kiro's Response:**

Here's a beginner-friendly explanation strategy:

### Structure: "Why This" + "What You Give Up"

**Avoid**: Technical jargon, feature lists, marketing speak
**Use**: Concrete scenarios, honest trade-offs, actionable insights

### Example Framework:

**For DynamoDB:**
- **Why**: "Automatically scales for spiky traffic" (not "highly scalable NoSQL")
- **Trade-off**: "Limited support for complex queries" (not "eventual consistency model")

**For RDS:**  
- **Why**: "Excellent support for SQL and joins" (not "ACID compliance")
- **Trade-off**: "Manual scaling required" (not "vertical scaling limitations")

### Language Principles:
1. **Concrete over Abstract**: "scales for traffic spikes" vs "highly scalable"
2. **Honest about Limitations**: Every choice has trade-offs
3. **User-Centered**: Focus on what matters to their use case
4. **Actionable**: Help them understand implications

### Implementation in Code:
```python
def explain(database):
    return {
        "why": ["Concrete benefits for their use case"],
        "tradeoffs": ["Honest limitations they should know"]
    }
```

This approach builds trust by being transparent about what users are gaining AND giving up with each choice.

## How These Conversations Shaped the Code

- **Decision Logic**: Kiro's scoring framework became the weighted algorithm in `app/logic.py`
- **Database Characteristics**: Kiro's analysis informed the scores in `app/data.py`
- **User Explanations**: Kiro's beginner-friendly approach shaped `app/explanations.py`

## Prompt 4: FastAPI Implementation Structure

**My Question to Kiro:**
"Help me structure a FastAPI application for the database recommendation tool. I need a simple form, processing logic, and results display."

**Kiro's Response:**

Here's a clean FastAPI structure for your database referee:

### Application Architecture
```python
app/
├── main.py          # FastAPI app with routes and HTML
├── logic.py         # Scoring and evaluation logic  
├── data.py          # Database characteristics
└── explanations.py  # User-friendly explanations
```

### Key Implementation Decisions:

**Single-File HTML**: Embed HTML in routes for simplicity - no need for templates for this focused tool.

**Form Processing**: Use FastAPI's `Form` for clean parameter handling:
```python
@app.post("/evaluate")
def evaluate(traffic: str = Form(...), complex: str = Form(...), beginner: str = Form(...)):
```

**Response Strategy**: Return formatted HTML with results embedded - keeps everything self-contained.

**Separation of Concerns**: 
- `main.py`: Routes and presentation
- `logic.py`: Pure scoring logic
- `data.py`: Static database characteristics  
- `explanations.py`: User-facing text

This structure makes the tool easy to understand, test, and extend.

## Prompt 5: User Interface Design

**My Question to Kiro:**
"Design a simple, clean user interface for the database selection form. It should feel approachable for beginners but professional."

**Kiro's Response:**

Here's a user-centered design approach:

### Visual Design Principles
- **Clean Typography**: System fonts for familiarity
- **Warm Colors**: Orange/blue palette to feel approachable, not corporate
- **Generous Spacing**: Plenty of whitespace to reduce cognitive load
- **Clear Hierarchy**: Hero section → Form → Results

### Form Design Strategy
```html
<select name="traffic">
  <option value="yes">Yes, it varies wildly</option>
  <option value="no">No, it's consistent</option>
</select>
```

**Language Choices**:
- "Spiky/unpredictable traffic" → "varies wildly" (more relatable)
- "Complex SQL queries" → "complex reporting needed" (outcome-focused)
- "New to database operations" → "we want minimal ops" (honest about preference)

### Results Page Strategy
- **Winner Banner**: Clear visual hierarchy showing the recommendation
- **Structured Explanations**: "Why this?" followed by "Trade-offs to consider"
- **Score Table**: Transparent scoring so users understand the logic

The design prioritizes clarity and trust over flashiness.

## Prompt 6: Error Handling and Edge Cases

**My Question to Kiro:**
"What edge cases and error handling should I consider for the database recommendation tool?"

**Kiro's Response:**

Here are the key considerations for robust operation:

### Input Validation
- **Form Parameters**: FastAPI's `Form(...)` ensures required fields
- **Value Validation**: Limit select options to prevent injection
- **Default Handling**: Graceful fallbacks for unexpected inputs

### Scoring Edge Cases
```python
# Handle ties in scoring
best_db = max(scores, key=scores.get)  # Consistent tie-breaking
```

### User Experience Edge Cases
- **Equal Scores**: When databases tie, the algorithm picks consistently
- **Extreme Preferences**: System handles users who answer "yes" to everything
- **Missing Context**: Each explanation stands alone without assuming prior knowledge

### Technical Robustness
- **Static Data**: Database scores are constants, eliminating runtime errors
- **Simple Logic**: Minimal dependencies reduce failure points
- **Self-Contained**: No external API calls that could fail

The tool prioritizes reliability over complexity - better to work simply than fail elegantly.
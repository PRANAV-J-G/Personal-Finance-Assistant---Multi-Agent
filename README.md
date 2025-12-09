# Personal Finance Assistant

A multi-agent AI system for personal finance management that helps you parse, analyze, and get recommendations for your expenses using an Agent-to-Agent (A2A) architecture.

## Overview

This project uses the Strands AI framework to create a distributed system of specialized agents that work together to provide comprehensive financial guidance:

1. **Expense Parser** - Extracts structured data from natural language expense descriptions
2. **Expense Analyzer** - Analyzes structured expense data and provides detailed insights
3. **Financial Advisor** - Generates personalized recommendations and investment suggestions

## Architecture

The system follows an A2A (Agent-to-Agent) architecture where:
- Each agent runs as an independent server
- An orchestrator agent coordinates communication between agents
- Agents communicate via HTTP endpoints using the A2A protocol

```
┌─────────────────┐
│   Orchestrator  │
│   (main.py)     │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌────────┐ ┌──────────┐ ┌──────────┐
│ Parser │ │ Analyzer │ │ Advisor  │
│ :8001  │ │  :8002   │ │  :8003   │
└────────┘ └──────────┘ └──────────┘
```

## Features

- **Natural Language Processing**: Parse expense descriptions from plain text
- **Comprehensive Analysis**: Get detailed breakdowns by category, payment method, and spending patterns
- **Personalized Recommendations**: Receive tailored financial advice including:
  - Budget optimization suggestions
  - Savings opportunities
  - Investment recommendations
  - Financial health scoring
  - Actionable next steps

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Personal_Finance
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Starting the Agent Servers

Use the provided script to start all agent servers:

```bash
cd agents
./start_servers.sh
```

This will start all three agent servers:
- **Parser Server**: http://127.0.0.1:8001
- **Analyzer Server**: http://127.0.0.1:8002
- **Advisor Server**: http://127.0.0.1:8003

The script runs all servers in the background and logs output to the `logs/` directory. Press `Ctrl+C` to stop all servers.

### Running the Orchestrator

Once all servers are running, you can use the orchestrator to process your expenses:

```bash
cd agents
python main.py
```

The orchestrator will:
1. Read expense data from `spending.txt` (or `expenses.txt`)
2. Connect to all agent servers
3. Process expenses through the pipeline:
   - Parse expenses → Analyze data → Get recommendations
4. Display comprehensive results

### Input Format

Place your expense data in `spending.txt` or `expenses.txt` in the project root. The parser can handle natural language descriptions like:

```
- Rent: ₹7,500 on Dec 1 via UPI
- Swiggy order: ₹250 on Dec 5 via card
- Metro recharge: ₹600 on Dec 10 via UPI
- Groceries: ₹1,200 on Dec 15 via cash
```

## Project Structure

```
Personal_Finance/
├── agents/
│   ├── parser_server.py      # Expense parser agent server
│   ├── analyzer_server.py    # Expense analyzer agent server
│   ├── advisor_server.py     # Financial advisor agent server
│   ├── main.py               # Orchestrator agent
│   ├── start_servers.sh      # Script to start all servers
│   └── logs/                 # Server logs
│       ├── parser.log
│       ├── analyzer.log
│       └── advisor.log
├── spending.txt              # Input expense data
├── expenses.txt              # Alternative input file
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Agent Details

### Expense Parser (`parser_server.py`)
- **Port**: 8001
- **Purpose**: Converts natural language expense descriptions into structured JSON
- **Output**: JSON array with fields: date, category, description, amount, payment_method

### Expense Analyzer (`analyzer_server.py`)
- **Port**: 8002
- **Purpose**: Analyzes structured expense data
- **Output**: Comprehensive analysis including:
  - Total expenditure
  - Category breakdowns
  - Spending patterns
  - Top expenses
  - Payment method distribution

### Financial Advisor (`advisor_server.py`)
- **Port**: 8003
- **Purpose**: Provides personalized financial recommendations
- **Output**: 
  - Budget optimization tips
  - Savings opportunities
  - Investment suggestions
  - Financial health score
  - Action plan

## Logs

All server logs are written to `agents/logs/`:
- `parser.log` - Parser server logs
- `analyzer.log` - Analyzer server logs
- `advisor.log` - Advisor server logs

## Stopping Servers

If you started servers using `start_servers.sh`, press `Ctrl+C` in that terminal to stop all servers gracefully.

Alternatively, you can manually stop servers by finding their process IDs:
```bash
ps aux | grep python | grep server
kill <PID>
```

## Dependencies

Key dependencies include:
- `strands-agents` - Core agent framework
- `strands-agents-tools` - A2A client tools
- `fastapi` - Web framework for agent servers
- `uvicorn` - ASGI server

See `requirements.txt` for the complete list.

## License

See LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Notes

- Ensure all agent servers are running before using the orchestrator
- The system expects expense data in natural language format
- All amounts should be in Indian Rupees (₹) for best results
- Agent servers must be accessible on localhost ports 8001, 8002, and 8003


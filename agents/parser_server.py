#!/usr/bin/env python3
"""Parser Agent A2A Server"""

import sys
import logging
from strands import Agent
from strands.multiagent.a2a import A2AServer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

PARSER_SYSTEM_PROMPT = """
You are a specialized expense parser. Extract expense information from natural language 
descriptions and structure it into a consistent JSON format.

For each expense, extract:
- date: The date of expense (YYYY-MM-DD format, use 2024-12 if month specified)
- category: Type of expense (groceries, transport, entertainment, utilities, dining, rent, etc.)
- description: Brief description of the expense
- amount: Numerical amount (just the number)
- payment_method: cash, card, upi, etc.

CRITICAL: Return ONLY valid JSON array format. No markdown, no explanations, no backticks.
Example:
[
  {
    "date": "2024-12-01",
    "category": "rent",
    "description": "Monthly rent",
    "amount": 5000,
    "payment_method": "upi"
  }
]
"""

def create_parser_agent():
    """Create the parser agent with proper configuration"""
    try:
        logger.info("Creating parser agent...")
        
        agent = Agent(
            name="expense_parser",
            description="Parses natural language expense descriptions into structured JSON format with categories, amounts, dates, and payment methods",
            system_prompt=PARSER_SYSTEM_PROMPT,
            tools=[]
        )
        
        logger.info("Parser agent created successfully")
        return agent
        
    except Exception as e:
        logger.error(f"Failed to create parser agent: {e}", exc_info=True)
        raise

def main():
    """Start the A2A server for parser agent"""
    try:
        logger.info("=" * 60)
        logger.info("Starting Parser Agent A2A Server")
        logger.info("=" * 60)
        
        # Create the agent
        parser_agent = create_parser_agent()
        
        # Create A2A server
        logger.info("Creating A2A server on port 8001...")
        a2a_server = A2AServer(
            agent=parser_agent,
            host="127.0.0.1",
            port=8001
        )
        
        logger.info("✅ Parser Agent A2A Server ready")
        logger.info("🔧 Listening on: http://127.0.0.1:8001")
        logger.info("📄 Agent Card: http://127.0.0.1:8001/.well-known/agent.json")
        logger.info("=" * 60)
        
        # Start the server (blocking)
        a2a_server.serve()
        
    except Exception as e:
        logger.error(f"❌ Failed to start parser server: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
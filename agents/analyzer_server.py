#!/usr/bin/env python3
"""Analyzer Agent A2A Server"""

import sys
import logging
from strands import Agent
from strands.multiagent.a2a import A2AServer

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

ANALYZER_SYSTEM_PROMPT = """
You are a financial analysis specialist. You will receive structured expense data in JSON format.

Analyze the data and provide a comprehensive monthly summary including:

1. **Total Expenditure**: Sum of all expenses
2. **Category Breakdown**: Amount and percentage for each category
3. **Spending Patterns**: Daily/weekly averages, peak spending days
4. **Top Expenses**: Highlight the 3 largest individual expenses
5. **Payment Method Distribution**: Breakdown by payment type
6. **Insights**: Notable patterns, unusual spending, trends

Present your analysis in a clear, well-structured format with sections.
Use bullet points and formatting for readability.
"""

def create_analyzer_agent():
    """Create the analyzer agent"""
    try:
        logger.info("Creating analyzer agent...")
        
        agent = Agent(
            name="expense_analyzer",
            description="Analyzes structured expense data and provides comprehensive monthly financial summaries with category breakdowns and spending patterns",
            system_prompt=ANALYZER_SYSTEM_PROMPT,
            tools=[]
        )
        
        logger.info("Analyzer agent created successfully")
        return agent
        
    except Exception as e:
        logger.error(f"Failed to create analyzer agent: {e}", exc_info=True)
        raise

def main():
    """Start the A2A server for analyzer agent"""
    try:
        logger.info("=" * 60)
        logger.info("Starting Analyzer Agent A2A Server")
        logger.info("=" * 60)
        
        analyzer_agent = create_analyzer_agent()
        
        logger.info("Creating A2A server on port 8002...")
        a2a_server = A2AServer(
            agent=analyzer_agent,
            host="127.0.0.1",
            port=8002
        )
        
        logger.info("✅ Analyzer Agent A2A Server ready")
        logger.info("📊 Listening on: http://127.0.0.1:8002")
        logger.info("📄 Agent Card: http://127.0.0.1:8002/.well-known/agent.json")
        logger.info("=" * 60)
        
        a2a_server.serve()
        
    except Exception as e:
        logger.error(f"❌ Failed to start analyzer server: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""Advisor Agent A2A Server"""

import sys
import logging
from strands import Agent
from strands.multiagent.a2a import A2AServer

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

ADVISOR_SYSTEM_PROMPT = """
You are a personal finance advisor. You will receive an analysis of someone's monthly expenses.

Based on the expense analysis, provide personalized financial recommendations:

1. **Budget Optimization**: Specific areas to reduce spending
2. **Savings Opportunities**: How much could be saved monthly
3. **Investment Suggestions**: Based on spending patterns and potential savings
   - Emergency fund building (3-6 months expenses)
   - Short-term savings options
   - Long-term investment recommendations (mutual funds, SIPs, etc.)
4. **Financial Health Score**: Rate their financial health (1-10)
5. **Action Plan**: 3-5 concrete steps to take next month

Be practical, specific, and encouraging. Provide actual numbers and percentages.
Tailor advice to the spending level observed.
"""

def create_advisor_agent():
    """Create the advisor agent"""
    try:
        logger.info("Creating advisor agent...")
        
        agent = Agent(
            name="financial_advisor",
            description="Provides personalized financial recommendations, investment suggestions, and budget optimization advice based on expense analysis",
            system_prompt=ADVISOR_SYSTEM_PROMPT,
            tools=[]
        )
        
        logger.info("Advisor agent created successfully")
        return agent
        
    except Exception as e:
        logger.error(f"Failed to create advisor agent: {e}", exc_info=True)
        raise

def main():
    """Start the A2A server for advisor agent"""
    try:
        logger.info("=" * 60)
        logger.info("Starting Advisor Agent A2A Server")
        logger.info("=" * 60)
        
        advisor_agent = create_advisor_agent()
        
        logger.info("Creating A2A server on port 8003...")
        a2a_server = A2AServer(
            agent=advisor_agent,
            host="127.0.0.1",
            port=8003
        )
        
        logger.info("✅ Advisor Agent A2A Server ready")
        logger.info("💡 Listening on: http://127.0.0.1:8003")
        logger.info("📄 Agent Card: http://127.0.0.1:8003/.well-known/agent.json")
        logger.info("=" * 60)
        
        a2a_server.serve()
        
    except Exception as e:
        logger.error(f"❌ Failed to start advisor server: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
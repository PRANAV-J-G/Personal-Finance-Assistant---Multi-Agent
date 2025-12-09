from strands import Agent
from strands_tools.a2a_client import A2AClientToolProvider
import logging

logging.basicConfig(level=logging.INFO)

ORCHESTRATOR_SYSTEM_PROMPT = """
You are a Personal Finance Assistant orchestrator. You coordinate with three specialized 
A2A agents to provide comprehensive financial guidance:

1. expense_parser - Parses natural language expense descriptions
2. expense_analyzer - Analyzes structured expense data
3. financial_advisor - Provides investment and savings recommendations

Always process requests in this sequence:
1. Parse expenses using expense_parser
2. Analyze the parsed data using expense_analyzer
3. Generate recommendations using financial_advisor

Present results in a user-friendly format with clear sections.
"""

def create_orchestrator():
    """Create orchestrator that connects to A2A agent servers"""
    
    # Define the URLs of your A2A agent servers
    agent_urls = [
        "http://127.0.0.1:8001",  
        "http://127.0.0.1:8002",  
        "http://127.0.0.1:8003", 
    ]
    
    # automatically discovers agent cards and creates tools
    a2a_tool_provider = A2AClientToolProvider(
        known_agent_urls=agent_urls
    )
    
    # Create orchestrator with A2A tools
    orchestrator = Agent(
        name="finance_orchestrator",
        system_prompt=ORCHESTRATOR_SYSTEM_PROMPT,
        tools=a2a_tool_provider.tools
    )
    
    return orchestrator

def main():
    
    with open("/Users/pranav/Files/Learning/strandsaws/Personal_Finance/spending.txt", "r") as file:
        expense_text = file.read()
        
    print("Personal Finance Assistant (A2A Architecture)")
    print("=" * 60)
    print("\nConnecting to A2A agents...")
    
    try:
        orchestrator = create_orchestrator()
        
        print("Connected to all A2A agents")
        print("\nProcessing your expenses...\n")
        
        prompt = f"""
        Process these monthly expenses:
        
        {expense_text}
        
        Please:
        1. Parse and structure the expenses
        2. Provide a comprehensive analysis
        3. Give personalized recommendations
        """
        
        response = orchestrator(prompt)
        
        print("\n" + "=" * 60)
        print("RESULTS")
        print("=" * 60)
        print(response)
        print("\n" + "=" * 60)
        
    except Exception as e:
        print(f" Error: {e}")


if __name__ == "__main__":
    main()
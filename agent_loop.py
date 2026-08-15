import re
from agent import Agent
from tools import TOOLS
from prompts import SYSTEM_PROMPT, SYSTEM_PROMPT_RAG
from groq import Groq
import os
from dotenv import load_dotenv


action_pattern = re.compile(r"Action:\s*(\w+):\s*(.+)")
answer_pattern = re.compile(r"Answer:\s*(.+)", re.DOTALL)

def Agentloop( query, client, max_steps = 10):
    my_agent = Agent(client, system = SYSTEM_PROMPT_RAG)
    next_query = query

    for i in range(max_steps):
        response = my_agent.call(query)
        print(response)

        answer_match = answer_pattern.search(response)
        if answer_match:
            return answer_match.group(1).strip
        action_match = action_pattern.search(response)
        if action_match:
            tool_name = action_match.group(1)
            tool_input = action_match.group(2).strip()
            if tool_name not in TOOLS:
                observation = f"Error: unknown tool '{tool_name}'"
            else:
                observation = TOOLS[tool_name](tool_input)

            print(f"Observation: {observation}")
            next_query = f"Observation: {observation}"
            continue

        return "Error: could not parse a valid Action or Answer."

    return "Max steps reached without a final answer."



if __name__ == "__main__":
    load_dotenv()
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    answer = Agentloop("According to the uploaded document, what is the security situation on Pakistan's eastern border?", client)
    print("FINAL ANSWER")
    print(answer)



from rag.llm import LocalLLM

llm = LocalLLM()

prompt = """
You are a SQL expert.

Tables:
- calls(agent_name, talk_time_sec, call_date, csat_score)
- agents(agent_name, team)

Question:
For each team, calculate the average talk time per call and total number of calls.
Return team, avg_talk_time, total_calls.

SQL:
"""

print("Generating complex SQL...\n")

output = llm.generate(prompt)

print(output)

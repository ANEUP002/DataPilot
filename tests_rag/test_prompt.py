from rag.prompt import build_sql_prompt

docs = [
    "Table calls has agent_name, talk_time_sec",
    "Table agents has team"
]

q = "average talk time per agent"

print(build_sql_prompt(q, docs))

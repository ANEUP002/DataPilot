from rag.retriever import Retriever

schema_docs = [
    "Table calls stores call center conversations. Columns: agent_name, talk_time_sec, hold_time, call_date, csat_score.",
    "Table agent_performance stores aggregated metrics per agent including avg_talk_time, total_calls, csat_avg.",
    "Table schedules stores agent working hours and shifts. Columns: agent_name, date, shift_start, shift_end, hours_worked.",
    "Table attendance logs daily check-in and check-out times for agents and hours worked.",
    "Table agents stores employee details including team and supervisor.",
    "Table payroll stores salary and bonus payments.",
    "Table sales stores orders and revenue by region and date.",
    "Table customers stores client contact info.",
    "Table tickets stores customer support tickets and resolution status.",
    "Table marketing stores campaign budgets and impressions."
]

retriever = Retriever(schema_docs)

queries = [
    "average talk time per agent",
    "agent working hours schedule",
    "total sales revenue",
    "customer support tickets"
]

for q in queries:
    print(f"\nQuery: {q}")
    for r in retriever.retrieve(q):
        print("  →", r)

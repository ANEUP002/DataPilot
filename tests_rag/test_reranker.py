from rag.reranker import Reranker

docs = [
    "Table calls has columns agent_name, talk_time_sec, call_date, csat_score",
    "Table call_logs has duration_sec, wait_time, resolution_status",
    "Table agent_performance has avg_talk_time, total_calls, csat_avg",
    "Table agents has team, supervisor, hire_date",
    "Table schedules has shift_start, shift_end",
    "Table payroll has salary, bonus, pay_date",
    "Table benefits has insurance_plan, vacation_days",
    "Table sales has revenue, region, order_id",
    "Table products has price, inventory_count",
    "Table customers has name, email, phone",
    "Table tickets has issue_type, status",
    "Table inventory has item_id, quantity",
    "Table shipments has delivery_date, status",
    "Table marketing has campaign_id, impressions",
    "Table website_analytics has page_views, bounce_rate",
    "Table finance has expenses, quarter",
    "Table audits has findings, department",
    "Table training has course_name, completion_date",
    "Table support_notes has notes, timestamps",
    "Table system_logs has log_level, message"
]

print("Loading reranker...")
reranker = Reranker()

query = "average talk time per agent"

print("\nReranking...")
results = reranker.rerank(query, docs, top_k=3)

print("\nTop results:")
for r in results:
    print("-", r)

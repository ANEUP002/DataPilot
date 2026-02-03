def build_sql_prompt(question: str, schema_docs: list[str]) -> str:
    """
    Build a strong prompt for SQL generation.

    Inputs:
        question: user natural language question
        schema_docs: retrieved relevant schema text

    Returns:
        prompt string for the LLM
    """

    schema_text = "\n".join(schema_docs)

    prompt = f"""
You are an expert SQL analyst.

Your job is to write a correct SQL query using ONLY the provided schema.

Follow these rules strictly:
- Return ONLY SQL
- Return EXACTLY one SQL statement
- DO NOT explain anything
- DO NOT add text before or after
- Only use columns listed in the schema
- NEVER invent columns (like id)
- NEVER assume fields
- If unsure, use: SELECT * FROM table LIMIT 5
- For preview queries, NEVER use ORDER BY
- Always prefer LIMIT for first rows

====================
DATABASE SCHEMA:
====================
{schema_text}

====================
QUESTION:
====================
{question}

====================
SQL:
====================
"""

    return prompt.strip()

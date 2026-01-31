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
- Use ONLY tables and columns from the schema
- Do NOT invent columns or tables
- Return ONLY SQL
- Do NOT explain anything
- Do NOT add comments
- Output only the final SQL query

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

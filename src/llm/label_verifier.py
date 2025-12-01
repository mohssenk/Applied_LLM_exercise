import pandas as pd
from typing import Optional
from llm.client import LLMClient
from llm.llm_output_model import LLMOutput
from llm.prompt import PROMPT

class LabelVerifier:
    def __init__(
        self, 
        llm_client: Optional[LLMClient] = None
    ):
        self.client: LLMClient = llm_client if llm_client else LLMClient()

    def run_dataframe(
        self, 
        df: pd.DataFrame
    ) -> pd.DataFrame:
        results: list[dict] = []
        for _, row in df.iterrows():
            out: LLMOutput = self._run_llm_row(row)
            results.append({
                "query": row["query"],
                "query_id": row["query_id"],
                "product_id": row["product_id"],
                "is_match_correct": out.is_match_correct,
                "corrected_query": out.corrected_query
            })
        return pd.DataFrame(results)
    
    def _run_llm_row(
        self, 
        row: pd.Series
    ) -> LLMOutput:
        prompt: str = PROMPT.format(
            query=row["query"],
            query_id=row["query_id"],
            product_id=row["product_id"],
            title=row["product_title"],
            brand=row["product_brand"],
            description=row["product_description"],
            bullets=row["product_bullet_point"],
        )
        output: LLMOutput = self.client.generate_structured_response(
            prompt=prompt,
            output_model=LLMOutput
        )
        return output


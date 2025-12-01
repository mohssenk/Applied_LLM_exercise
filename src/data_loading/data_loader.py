import os
from typing import List, Optional, Iterable
from settings.config import DATA_PATH
import pandas as pd


class DataLoader:
    def __init__(
        self, dataset_a_name: str, 
        dataset_b_name: str
    ):
        self.dataset_a_name = dataset_a_name
        self.dataset_b_name = dataset_b_name
        self.data_path = DATA_PATH

    def create_filtered_dataset(
        self,
        merge_on: List[str] | str, 
        include_col: Optional[str] = None,
        include_values: Optional[Iterable[str]] = None,
        equal_col: Optional[str] = None,
        equal_value: Optional[str] = None,
    ) -> pd.DataFrame:
        df_a = self._load_dataset(self.dataset_a_name)
        df_b = self._load_dataset(self.dataset_b_name)
        df_merged = self._merge_datasets(merge_on, df_a, df_b)
        include = {include_col: include_values} if include_col and include_values else {}
        equal = {equal_col: equal_value} if equal_col and equal_value else {}
        df_filtered = self._filter_dataset(df=df_merged, include=include, equal=equal)
        return df_filtered

    def _load_dataset(
        self,
        dataset_name: str
    ) -> pd.DataFrame:
        path = os.path.join(self.data_path, dataset_name)
        return pd.read_parquet(path)

    @staticmethod
    def _merge_datasets(
        merge_on: List[str] | str,
        df_a: pd.DataFrame,
        df_b: pd.DataFrame,
    ) -> pd.DataFrame:
        return df_a.merge(df_b, on=merge_on, how="inner")

    @staticmethod
    def _filter_dataset(
        df: pd.DataFrame,
        include: Optional[dict[str, Iterable[str]]] = None,
        equal: Optional[dict[str, str]] = None,
    ) -> pd.DataFrame:
        if include:
            for col, values in include.items():
                df = df[df[col].isin(values)]
        if equal:
            for col, value in equal.items():
                df = df[df[col] == value]
        return df

    
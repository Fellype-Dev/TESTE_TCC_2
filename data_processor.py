"""
data_processor.py

Módulo auxiliar para processamento, agregação e formatação de dados numéricos e relatórios.
Utilizado para testes de revisão de código e arquitetura.
"""

import json
import logging
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self, default_threshold: float = 0.0):
        self.default_threshold = default_threshold
        self.processed_records: List[Dict[str, Any]] = []

    def process_records(self, records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Filtra e normaliza os registros fornecidos com base no limiar configurado.
        """
        results = []
        for record in records:
            value = record.get("value", 0.0)
            if value >= self.default_threshold:
                record_copy = dict(record)
                record_copy["normalized_value"] = round(value, 2)
                results.append(record_copy)
        
        self.processed_records.extend(results)
        return results

    def calculate_summary(self) -> Dict[str, Any]:
        """
        Gera um resumo estatístico simples dos registros processados.
        """
        if not self.processed_records:
            return {"count": 0, "total": 0.0, "average": 0.0}

        total = sum(item.get("normalized_value", 0.0) for item in self.processed_records)
        count = len(self.processed_records)
        average = total / count if count > 0 else 0.0

        return {
            "count": count,
            "total": round(total, 2),
            "average": round(average, 2)
        }

    def export_summary_json(self) -> str:
        """
        Exporta o resumo estatístico em formato JSON.
        """
        summary = self.calculate_summary()
        return json.dumps(summary, indent=2)


def format_report_title(report_name: str) -> str:
    """
    Gera um título limpo e atemporal para relatórios.
    """
    return f"Relatório de Execução - {report_name.strip().capitalize()}"

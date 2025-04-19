import pandas as pd
from pathlib import Path
import openpyxl  # For Excel formatting
from typing import List, Dict

def save_to_excel(data: List[Dict], file_path: str, sheet_name: str = "Companies") -> None:
    """
    Save data to Excel with auto-formatting for French business data
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    df = pd.DataFrame(data)
    
    # French-style formatting
    with pd.ExcelWriter(path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        # Auto-adjust columns
        worksheet = writer.sheets[sheet_name]
        for column in worksheet.columns:
            max_length = max(len(str(cell.value)) for cell in column)
            worksheet.column_dimensions[column[0].column_letter].width = max_length + 2
        
        # Freeze header row
        worksheet.freeze_panes = "A2"

def group_by_ape_code(data: List[Dict]) -> Dict[str, List[Dict]]:
    """Group companies by their APE code"""
    grouped = {}
    for company in data:
        ape = company.get("code_ape", "N/A")
        grouped.setdefault(ape, []).append(company)
    return grouped
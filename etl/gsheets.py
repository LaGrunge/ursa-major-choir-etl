from __future__ import annotations

import json
from typing import Any, List

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def build_sheets_service(service_account_info: dict) -> Any:
    creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
    return build("sheets", "v4", credentials=creds)


def append_rows(
    service: Any,
    spreadsheet_id: str,
    range_a1: str,
    rows: List[List[Any]],
) -> None:
    body = {"values": rows}
    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range_a1,
        valueInputOption="USER_ENTERED",
        insertDataOption="INSERT_ROWS",
        body=body,
    ).execute()

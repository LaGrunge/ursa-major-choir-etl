from __future__ import annotations

import json
import os
from datetime import datetime, timezone

from dotenv import load_dotenv

from etl.gsheets import append_rows, build_sheets_service


def main() -> None:
    load_dotenv()

    target_spreadsheet_id = os.environ["TARGET_SPREADSHEET_ID"]
    sa_json = os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]

    service_account_info = json.loads(sa_json)
    service = build_sheets_service(service_account_info)

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    append_rows(
        service=service,
        spreadsheet_id=target_spreadsheet_id,
        range_a1="etl_run_log!A:D",
        rows=[[now, "SUCCESS", "weekly_etl", "started"]],
    )

    print("Logged ETL run")


if __name__ == "__main__":
    main()

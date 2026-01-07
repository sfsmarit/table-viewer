from fastapi import FastAPI
from fastapi.responses import Response
import io

import data

api = FastAPI(title="Tape-Out List CSV Download API")


@api.get(data.API_PATH)
def download_csv():
    # Build your data
    df = data.create_data()

    # Create CSV text with UTF-8 BOM for Excel compatibility
    buf = io.StringIO()
    buf.write("\ufeff")  # UTF-8 BOM
    df.to_csv(buf, index=False)  # comma-separated, quoted as needed
    csv_text = buf.getvalue()

    # Return as downloadable attachment
    return Response(
        content=csv_text,
        media_type="text/csv; charset=utf-8",
        headers={
            "Content-Disposition": 'attachment; filename="saw_tapeout.csv"',
            "Cache-Control": "no-store",
        },
    )

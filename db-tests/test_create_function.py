from pathlib import Path
import base64

from singlestoredb.connection import Cursor

def test_create_functions(singlestoredb_tempdb: Cursor):
    cursor = singlestoredb_tempdb

    wasm = Path.cwd() / "target" / "wasm32-wasi" / "debug" / "add_one.wasm"
    wit = Path.cwd() / "add_one.wit"

    assert wasm.exists(), "Make sure to build the Wasm library before running tests"

    wasm_data = base64.b64encode(wasm.read_bytes()).decode()
    wit_data = base64.b64encode(wit.read_bytes()).decode()

    cursor.execute(f"CREATE FUNCTION add_one AS WASM FROM BASE64 \"{wasm_data}\" WITH WIT FROM BASE64 \"{wit_data}\"")


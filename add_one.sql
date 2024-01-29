-- Create both functions that make up the extension
CREATE FUNCTION add_one AS WASM FROM LOCAL INFILE "add_one.wasm" WITH WIT FROM LOCAL INFILE "add_one.wit";

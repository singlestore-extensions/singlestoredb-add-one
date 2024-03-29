# Add One

The Add One SingleStore DB extension, written in Rust.

## Building

In order to build the Wasm

1. Install Rust and Cargo
2. Install the Rust `wasm32-wasi` target
3. Run `cargo build --target wasm32-wasi`

To build the extension from the Wasm locally, run the following.

```bash
cp ./target/wasm32-wasi/release/add_one.wasm ./add_one.wasm
tar cvf add_one.tar add_one.sql add_one.wasm add_one.wit 
```

## Testing

There are automated script tests in the `db-tests` directory.
They are run against the `singlestoredb-dev-image`.

In order to run the tests

1. Install Python 3
2. Install `singlestoredb[pytest]` (and optionally `pytest-xdist`) using pip
3. Set the `SINGLESTORE_LICENSE` environment variable
4. Run the `pytest` command

If you installed `pytest-xdist`, you can also distribute the tests to multiple workers
by running `pytest -n auto` or giving a specific number instead of `auto`

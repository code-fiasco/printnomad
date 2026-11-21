# The Python core runs in the browser via Pyodide

The extension converts with the same Python core as the CLI and the OrcaSlicer plugin, loaded through Pyodide in a Web Worker, instead of a TypeScript port. One implementation means one test suite and conversions byte-identical to the CLI; the cost is a ~13 MB one-time download, ~1 s start-up, and a core restricted to the standard library.

## Considered Options

- **TypeScript port of the core**: faster start and smaller download, but two implementations of every conversion rule to keep in step.

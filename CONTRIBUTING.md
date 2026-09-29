# Contributing

## Notebook dependencies

Notebooks are run with `pixi run --script`, for example:

```sh
pixi run --script pixi-sandbox/notebook.py --experimental
```

For this to work, declare the dependencies in a `conda-script` block at the top of each notebook script:

```python
# /// conda-script
# channels = ["https://prefix.dev/conda-forge"]
# entrypoint = "marimo edit ${SCRIPT}"
#
# [dependencies]
# python = ">=3.12"
#
# [tool.pixi.pypi-dependencies]
# marimo = "*"
# pandas = "==3.0.6"
# pyarrow = "==25.0.1"
# /// end-conda-script
```

See `pixi-sandbox/notebook.py` for a full example.

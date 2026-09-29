# /// conda-script
# channels = ["https://prefix.dev/conda-forge"]
# entrypoint = "marimo edit ${SCRIPT}"
#
# [dependencies]
# python = ">=3.12"
#
# [tool.pixi.pypi-dependencies]
# marimo = "*"
# duckdb = "==1.5.6"
# gdrive-fsspec = "==0.4.1"
# pandas = "==3.0.6"
# pyarrow = "==25.0.1"
# /// end-conda-script

import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd

    from gdrive_fsspec import GoogleDriveFileSystem

    return GoogleDriveFileSystem, pd


@app.cell
def _(GoogleDriveFileSystem):
    # for initial exec, token='browser'
    fs = GoogleDriveFileSystem(token='cache')
    return (fs,)


@app.cell
def _(fs, pd):
    key = "gdrive://shared/20260929_airkorea_finalized_observation/year=2005/data_0.parquet"
    df = pd.read_parquet(path=key, filesystem=fs)
    return (df,)


@app.cell
def _(df):
    df
    return


if __name__ == "__main__":
    app.run()

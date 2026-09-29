# marimo-usecase

A collection of [marimo](https://marimo.io) use cases.

## Use cases

| Directory | Description |
| --- | --- |
| [`google-drive/`](./google-drive) | Working with Google Drive |
| [`pixi-sandbox/`](./pixi-sandbox) | Running marimo notebooks in a pixi environment |

## Getting started

The only requirement is [pixi](https://pixi.sh).  
(Notebooks run in marimo's sandbox mode)

```bash
pixi exec -s marimo -s uv marimo edit --sandbox <notebook>.py
```

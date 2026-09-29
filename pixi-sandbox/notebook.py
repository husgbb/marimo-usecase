# /// conda-script
# channels = ["https://prefix.dev/conda-forge"]
# entrypoint = "marimo edit ${SCRIPT}"
#
# [dependencies]
# python = ">=3.12"
# gdal = "==3.13.3"
#
# [tool.pixi.pypi-dependencies]
# marimo = "*"
# gdal = "==3.13.3"
# /// end-conda-script

import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    from osgeo import gdal

    gdal.UseExceptions()

    url = "https://github.com/wmgeolab/geoBoundaries/raw/9469f09/releaseData/gbOpen/KOR/ADM1/geoBoundaries-KOR-ADM1.geojson"

    dataset = gdal.OpenEx(f"/vsicurl/{url}", gdal.OF_VECTOR)
    layer = dataset.GetLayer(0)

    feature_rows = [
        {
            "shapeName": feature.GetField("shapeName"),
            "shapeISO": feature.GetField("shapeISO"),
            "geometry_type": feature.GetGeometryRef().GetGeometryName(),
        }
        for feature in layer
    ]
    layer.ResetReading()

    print(f"Layer: {layer.GetName()}")
    print(f"Feature count: {layer.GetFeatureCount()}")
    print(f"Extent: {layer.GetExtent()}")
    print(f"CRS: {layer.GetSpatialRef().GetName()}")
    return (feature_rows,)


@app.cell
def _(feature_rows, mo):
    mo.ui.table(feature_rows)
    return


if __name__ == "__main__":
    app.run()

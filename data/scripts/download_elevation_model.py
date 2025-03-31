#!/usr/bin/env python3

"""Download an elevation model data set from HRI’s WCS service."""


import pathlib
import rasterio
import rasterio.mask
import shapely
import urllib.parse


BOUNDING_BOX = (
    25494767,  # minx
    6671328,  # miny
    25497720,  # maxx
    6673701,  # maxy
)

DESTINATION_CRS = "EPSG:4326"
SOURCE_CRS = "EPSG:3879"


def main():
    """Download an elevation model data set from HRI’s WCS service."""
    # Where to save the downloaded data sets? One directory up from this script
    OUTPUT_DIRECTORY = pathlib.Path().absolute().parent

    # Download data set for the specified bounding box
    # in the upstream native reference system ETRS GK-25 (EPSG:3879),
    # then reproject it to WGS-84 (EPSG:4326)
    with rasterio.open(
        "WCS:https://kartta.hel.fi/ws/geoserver/avoindata/wcs?"
        + urllib.parse.urlencode(
            {
                "service": "WCS",
                "version": "1.0.0",
                "request": "GetCoverage",
                "coverage": "Korkeusmalli_2021_50cm",
                "clip": shapely.geometry.box(*BOUNDING_BOX).wkt,
                "crs": SOURCE_CRS,
            }
        )
    ) as source:
        destination_transform, destination_width, destination_height = (
            rasterio.warp.calculate_default_transform(
                SOURCE_CRS,
                DESTINATION_CRS,
                source.width,
                source.height,
                *source.bounds,
            )
        )
        destination_meta = source.meta
        destination_meta.update(
            {
                "driver": "GTiff",
                "crs": DESTINATION_CRS,
                "height": destination_height,
                "width": destination_width,
                "transform": destination_transform,
            }
        )
        with rasterio.open(
            OUTPUT_DIRECTORY / "elevation_model_2021.tif",
            "w",
            compress="LZW",
            predictor="3",
            num_threads="NUM_CPUS",
            **destination_meta,
        ) as destination:
            for band in source.indexes:
                rasterio.warp.reproject(
                    source=rasterio.band(source, band),
                    src_crs=SOURCE_CRS,
                    src_transform=source.transform,
                    destination=rasterio.band(destination, band),
                    dst_crs=DESTINATION_CRS,
                    dst_transform=destination.transform,
                )


if __name__ == "__main__":
    main()

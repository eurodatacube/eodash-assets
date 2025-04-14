#!/usr/bin/python
"""
go through all RACE and eodashboard indicators, get their collection
find a matching definition programatically
convert schema from v4 config in legends.json to v5 schema https://github.com/eodash/eodash_catalog/wiki/Colorlegend
"""

from typing import Any, Dict
import json
from pathlib import Path
import yaml
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import numpy as np
from matplotlib.colors import (
    LinearSegmentedColormap,
)
import cmocean

import os

COUNTER = 0
generator_script_dir = Path(__file__).parent
LEGENDS_JSON_PATH = Path(generator_script_dir / "legends.json").resolve()
folder_eodash_catalog_v4_configs = (
    Path(__file__).parent.parent / "eodash-v4-catalog-for-migration-tests"
)
collections_dir = Path(folder_eodash_catalog_v4_configs / "collections").resolve()
indicators_dir = Path(folder_eodash_catalog_v4_configs / "indicators").resolve()
catalogs_dir = Path(folder_eodash_catalog_v4_configs / "catalogs").resolve()

# prepare a special legend cfastie (NDVI), as its not in matplotlib
cfastie = np.load(os.path.join(os.path.dirname(__file__), "cfastie.npy"))
cfastie_prepared = [
    [
        i / 255,
        [rgbadef / 255 for rgbadef in step],
    ]
    for i, step in enumerate(cfastie)
]
cm.register_cmap(
    name="cfastie", cmap=LinearSegmentedColormap.from_list("cfastie", cfastie_prepared)
)
for colormap_name in dir(cmocean.cm):
    if isinstance(getattr(cmocean.cm, colormap_name), LinearSegmentedColormap):
        cmap = LinearSegmentedColormap.from_list(
            colormap_name, getattr(cmocean.cm, colormap_name)(range(256))
        )
        try:
            cm.register_cmap(name=colormap_name, cmap=cmap)
        except ValueError:
            pass


def load_json(file_path: str) -> Dict[str, Any]:
    """Load a JSON file and return its content as a dictionary."""
    with open(file_path, "r", encoding="utf-8") as f:
        data: Dict[str, Any] = json.load(f)
    return data


def convert_v5_syntax(old_label_config_dict: Dict[str, Any]) -> Dict[str, Any]:
    output = {
        "title": "Sample text",
        "range": "",  # individual colors as html hexcode
        "domain": "",  # default [0, 1], that translates to range
        "scaleType": "continuous",  # default, also discrete/threshold
    }
    output["title"] = old_label_config_dict["label"]

    cm_def_old = old_label_config_dict.get("cm")
    hex_colors = cm_def_old
    if old_label_config_dict.get("discrete"):
        output["scaleType"] = "discrete"

    if isinstance(cm_def_old, str):
        # single colorscale name, convert to hex
        cmap = cm.get_cmap(cm_def_old, 14)  # 14 discrete colors
        hex_colors = [mcolors.to_hex(cmap(i)) for i in range(cmap.N)]
    elif isinstance(cm_def_old, list):
        if isinstance(cm_def_old[0], str):
            # hexcodes already
            pass
        elif isinstance(cm_def_old[0], list):
            # list of two elements, a number and a list of rgb/rgba colors
            rgb = [color_definition[1][:3] for color_definition in cm_def_old]
            normalized_rgb = [
                [rgb_n[0] / 255, rgb_n[1] / 255, rgb_n[2] / 255] for rgb_n in rgb
            ]
            hex_colors = [mcolors.to_hex(rgb_val) for rgb_val in normalized_rgb]
    output["domain"] = old_label_config_dict["range"]
    output["range"] = hex_colors

    if old_label_config_dict.get("ticks") and old_label_config_dict.get("tickLabels"):
        if isinstance(old_label_config_dict["tickLabels"][-1], str):
            # categorical scale
            # only take as many hexcode entries, as there is labels - linear space
            indices = np.linspace(
                0,
                len(output["range"]) - 1,
                len(old_label_config_dict["tickLabels"]),
                dtype=int,
            )
            selected_hex_colors = [output["range"][i] for i in indices]
            output["range"] = selected_hex_colors
            output["domain"] = old_label_config_dict["tickLabels"]
            output["scaleType"] = "categorical"
        else:
            # numerical scale
            output["domain"] = [
                old_label_config_dict["tickLabels"][0],
                old_label_config_dict["tickLabels"][-1],
            ]
    if output["scaleType"] == "continuous":
        output["tickFormat"] = ".0f"

    return output


# load legends definitions in legends.json
data = load_json(LEGENDS_JSON_PATH)
# mapping of collection file yaml to legend key for cases where renaming was not fully done
CUSTOM_MAPPING_MANUAL_MATCH = {
    "GHS_BUILT-S-R2023A": "GHS-BUILT-S-R2023A",
    "CROPOMAT1_crop_forecast_at": "crop_forecast_CropOM",
    "CROPOMAT2_crop_forecast_at_water": "crop_forecast_CropOM",
    "CROPOMHU1_crop_forecast_hu": "crop_forecast_CropOM",
    "CROPOMHU2_crop_forecast_hu_water": "crop_forecast_CropOM",
    "CROPOMHUMR1_crop_forecast_hu_mezohegyes": "crop_forecast_CropOM",
    "CROPOMHUMR2_crop_forecast_hu_mezohegyes_water": "crop_forecast_CropOM",
    "CROPOMHUSC1_crop_forecast_hu_bekes": "crop_forecast_CropOM",
    "CROPOMHUSC2_crop_forecast_hu_bekes_water": "crop_forecast_CropOM",
    "CROPOMRO1_crop_forecast_ro": "crop_forecast_CropOM",
    "CROPOMRO2_crop_forecast_ro_water": "crop_forecast_CropOM",
    "CDS4_wind_10m_v": "CDS3_wind_10m_u",
    "E12d_truck_detections_primary_roads": "E12c_truck_detections_motorways",
    "E13q_vessel_density_tanker": "E13o_vessel_density_all",
    "E13r_vessel_density_others": "E13o_vessel_density_all",
    "E13p_vessel_density_cargo": "E13o_vessel_density_all",
    "N1_city_no2": "N1b_NO2",
    "IDEAS1_hopi": "IDEAS1_hopi_b1",
    "grdi-v1-raster": "grdi-v1-built",
    "grdi-shdi-raster": "grdi-v1-built",
    "grdi-vnl-slope-raster": "grdi-v1-built",
    "grdi-vnl-raster": "grdi-v1-built",
    "grdi-filled-missing-values-count": "grdi-v1-built",
    "grdi-imr-raster": "grdi-v1-built",
    "grdi-cdr-raster": "grdi-v1-built",
    "SIE_sea_ice_thickness_envisat": "SITI_IS2SITMOGR4-cog",
    "SIC_sea_ice_thickness_cryosat": "SITI_IS2SITMOGR4-cog",
    # "WSF_world_settlement_footprint": "", # needs special cathegorical manual one
    "N12_sea_ice_concentration_antarctic": "N12_sea_ice_concentration",
    "N12_1_sea_ice_concentration_arctic": "N12_sea_ice_concentration",
    # "N6_geoglam": "", # needs special cathegorical manual one
    "CDS8_windv_ERA5-SingleLevel_100m_GLOBAL": "CDS7_windu_ERA5-SingleLevel_100m_GLOBAL",
    "N3a2_chl_concentration_tri_esa": "N3a2_chl_concentration_tri",
    "N3a2_chl_concentration_tri_jaxa": "N3a2_chl_concentration_tri",
    "N3a2_chl_concentration_tri_nasa": "N3a2_chl_concentration_tri",
    "N3a2_total_suspended_matter_tri_esa": "N3a2_total_suspended_matter_tri",
    "N3a2_total_suspended_matter_tri_jaxa": "N3a2_total_suspended_matter_tri",
    "N3a2_total_suspended_matter_tri_nasa": "N3a2_total_suspended_matter_tri",
    "RECCAP2_2_AGC_LVOD_amazonia_smooth_max_crop": "RECCAP2_1_AGC_LVOD_amazonia_methods_mean_crop",
    "RECCAP2_3_AGC_LVOD_amazonia_smooth_mean_crop": "RECCAP2_1_AGC_LVOD_amazonia_methods_mean_crop",
    "RECCAP2_4_AGC_LVOD_amazonia_trend_mean_crop": "RECCAP2_1_AGC_LVOD_amazonia_methods_mean_crop",
    "RECCAP2_7_degraded_biomass": "RECCAP2_6_deforested_biomass",
    "RECCAP2_8_edge_biomass_change": "RECCAP2_6_deforested_biomass",
    "RECCAP2_10_intact_biomass_change_smooth_max": "RECCAP2_9_intact_biomass_change_methods_mean",
    "RECCAP2_11_intact_biomass_change_smooth_mean": "RECCAP2_9_intact_biomass_change_methods_mean",
    "RECCAP2_12_intact_biomass_change_trend_mean": "RECCAP2_9_intact_biomass_change_methods_mean",
    # "FNF_Palsar": "", # needs special cathegorical manual one
    "4D_Greenland_Duration": "ADD_Melt_Duration",
    "4D_Greenland_Melt_Onset": "ADD_Melt_Onset",
    "4D_Greenland_Melt_Season_End": "ADD_Melt_Season_End",
    "4D_Greenland_Meltmap": "ADD_Meltmap",
}


def find_matching_legend_definition(
    contained_collection_str: str,
) -> tuple[str, dict]:
    """Find a matching collection YAML based on the key and
    shout if we do not have a match"""
    if contained_collection_str in CUSTOM_MAPPING_MANUAL_MATCH:
        # print("found on manual mapping", contained_collection_str)
        # if not found, print it out, needs a manual mapping
        for catalog_name, catalog_legend_values in data.items():
            for legend_name, collection_legend_def in catalog_legend_values.items():
                if legend_name == CUSTOM_MAPPING_MANUAL_MATCH[contained_collection_str]:
                    return (
                        CUSTOM_MAPPING_MANUAL_MATCH[contained_collection_str],
                        collection_legend_def,
                    )
    # search through all keys to find matching legend definition in json
    for catalog_name, catalog_legend_values in data.items():
        for legend_name, collection_legend_def in catalog_legend_values.items():
            if legend_name == contained_collection_str:
                # print("found on direct name match", contained_collection_str)
                return contained_collection_str, collection_legend_def
    return (None, None)


def add_colorlegend_to_yaml(contained_collection_str: str):
    global COUNTER
    with open(collections_dir / f"{contained_collection_str}.yaml", "r+") as hh:
        # read the collection_yaml and do the collection search
        collection_yaml_content = yaml.safe_load(hh)
        # only print match for those where Legend key exists to migrate
        if (
            "Legend" in collection_yaml_content
            and "Colorlegend" not in collection_yaml_content
        ):
            (match, legend_def) = find_matching_legend_definition(
                contained_collection_str, collection_yaml_content
            )
            if match:
                # get label
                if not (legend_def.get("logarithmic")):
                    # convert to new syntax
                    converted_output: dict = convert_v5_syntax(legend_def)
                    # modify original dictionary (YAML comments are lost)
                    yaml_section_to_add = {"Colorlegend": converted_output}
                    # change files in place
                    yaml.dump(yaml_section_to_add, hh, default_flow_style=False)
            else:
                print("match not found", contained_collection_str)
        else:
            print("Legend key not present in", contained_collection_str)


if __name__ == "__main__":
    collection_yaml_files = list(collections_dir.glob("*.yaml"))
    indicator_yaml_files = list(indicators_dir.glob("*.yaml"))

    for catalog_filename in [
        catalogs_dir / "race.yaml",
        catalogs_dir / "trilateral.yaml",
    ]:
        # read its indicators
        with open(catalog_filename, "r") as fh:
            catalog_yaml_content = yaml.safe_load(fh)
            indicators_in_this_catalog: list = catalog_yaml_content["collections"]
            for indicator_or_collection in indicators_in_this_catalog:
                # check if indicator or collection
                if indicator_or_collection in [
                    yaml_file.stem for yaml_file in indicator_yaml_files
                ]:
                    # read the indicator_yaml_file, get all its collections and for each, do the collection search
                    with open(
                        indicators_dir / f"{indicator_or_collection}.yaml", "r"
                    ) as gh:
                        # read yaml
                        indicator_yaml_content = yaml.safe_load(gh)
                        # get list of collections
                        list_of_contained_collections = indicator_yaml_content[
                            "Collections"
                        ]
                        for contained_collection_str in list_of_contained_collections:
                            # read the collection_yaml and do the collection search
                            add_colorlegend_to_yaml(contained_collection_str)

                else:
                    # it is a collection
                    # read the collection_yaml and do the collection search
                    add_colorlegend_to_yaml(indicator_or_collection)

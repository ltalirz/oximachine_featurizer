# -*- coding: utf-8 -*-
"""Testing the conversion of feature files
into feature matrix and label file into label vector"""
import os

import pandas as pd
from pymatgen import Structure

from oximachine_featurizer.featurize import FeatureCollector, GetFeatures, featurize

THIS_DIR = os.path.dirname(__file__)


def test_featurization():
    """Test the basic featurizer"""
    structure = Structure.from_file(
        os.path.join(
            THIS_DIR, "..", "..", "examples", "structures", "BaO2_mp-1105_computed.cif"
        )
    )
    featurizer = GetFeatures(structure, "")
    feat = featurizer.return_features()
    assert len(feat) == 2
    assert len(feat[0]["feature"]) == len(feat[1]["feature"]) == 129


def test_featurize():
    """Test the featurization wrapper function."""
    structure = Structure.from_file(
        os.path.join(
            THIS_DIR, "..", "..", "examples", "structures", "BaO2_mp-1105_computed.cif"
        )
    )
    x, indices, names = featurize(structure)  # pylint: disable=invalid-name
    assert len(x) == len(indices) == len(names)


def test_make_labels_table(provide_label_dict):
    """Test conversion of raw labels in list of dictionaries"""
    label_dict, expected_table = provide_label_dict

    labels_table = FeatureCollector.make_labels_table(label_dict)

    assert labels_table == expected_table


def test_create_clean_dataframe(provide_dummy_feature_list, provide_label_dict):
    """Test merging of features and labels"""
    _, expected_table = provide_label_dict
    feature_list = provide_dummy_feature_list

    df = FeatureCollector._create_clean_dataframe(  # pylint:disable=invalid-name,protected-access
        feature_list, expected_table
    )
    assert isinstance(df, pd.DataFrame)  # make sure we have a dataframe
    assert len(df) == len(expected_table)  # there are no N/As

    # an interesting case is UKUDIP01 with two metals
    assert len(df[df["name"] == "UKUDIP01"]) == 2
    assert (
        df[(df["name"] == "UKUDIP01") & (df["metal"] == "Cu")]["oxidationstate"].values
        == 2
    )
    assert (
        df[(df["name"] == "UKUDIP01") & (df["metal"] == "Gd")]["oxidationstate"].values
        == 3
    )


def test_get_x_y_names(provide_dataframe):
    """Test splitting in features, labels and names"""
    df = provide_dataframe  # pylint:disable=invalid-name

    (
        X,  # pylint:disable=invalid-name
        y,  # pylint:disable=invalid-name
        names,
    ) = FeatureCollector._get_x_y_names(  # pylint:disable=protected-access
        df
    )

    assert len(X) == len(y) == len(names)
    # an interesting case is UKUDIP01 with two metals
    ukudip01 = [n == "UKUDIP01" for n in names]
    assert sum(ukudip01) == 2
    oxidation_states = [ox for i, ox in enumerate(y) if ukudip01[i]]
    assert oxidation_states == [2, 3]


def test__partial_match_in_name():
    """Test if the partial match detector works as intended"""
    assert FeatureCollector._partial_match_in_name(  # pylint:disable=protected-access
        "MAHSUK01", ["MAHSUK", "JIZJIN"]
    )

    assert (
        not FeatureCollector._partial_match_in_name(  # pylint:disable=protected-access
            "MAHSUK01", ["ORIVUI", "JIZJIN"]
        )
    )

# Changelog

### [0.2.8](https://www.github.com/kjappelbaum/oximachine_featurizer/compare/v0.2.7...v0.2.8) (2020-12-11)


### Bug Fixes

* console script entry point names ([eabafe3](https://www.github.com/kjappelbaum/oximachine_featurizer/commit/eabafe38e1d3f6d0f3383f067e73aa3eb4426493))

### [0.2.7](https://www.github.com/kjappelbaum/oximachine_featurizer/compare/v0.2.6...v0.2.7) (2020-12-11)


### Miscellaneous

* changelog sections for release-please ([e6cbb1c](https://www.github.com/kjappelbaum/oximachine_featurizer/commit/e6cbb1ca1328780248cf54859cd5b358b1e745e6))

### [0.2.6](https://www.github.com/kjappelbaum/oximachine_featurizer/compare/v0.2.5...v0.2.6) (2020-12-11)


### Documentation

* updated docs about the parsing tools ([ebf850a](https://www.github.com/kjappelbaum/oximachine_featurizer/commit/ebf850ab82bf69d0fa98cd7824d803000aa66a46))

### [0.2.5](https://www.github.com/kjappelbaum/oximachine_featurizer/compare/v0.2.4...v0.2.5) (2020-12-11)


### Documentation

* fixing docstrings, mocking imports ([da512c1](https://www.github.com/kjappelbaum/oximachine_featurizer/commit/da512c14d15a1f0b27c4c91063d31b65173a4b1d))

### [0.2.4](https://www.github.com/kjappelbaum/oximachine_featurizer/compare/v0.2.3...v0.2.4) (2020-12-11)


### Documentation

* updated docs about the parsing tools ([08367f8](https://www.github.com/kjappelbaum/oximachine_featurizer/commit/08367f85c0a7ae91f20f306bda23af6c3af95a7a))

### [0.2.3](https://www.github.com/kjappelbaum/oximachine_featurizer/compare/v0.2.2...v0.2.3) (2020-12-11)


### Documentation

* adding API docs ([a638164](https://www.github.com/kjappelbaum/oximachine_featurizer/commit/a6381640c921d0009796560e2f979984d3fbb2b2))

## v0.2.2 (2020-08-26)

### New

-   Feat: increasing cutoff. \[Kevin\]

### Changes

-   Chore: preparing next release. \[Kevin\]
-   Chore: reverse option should work as is_flag. \[Kevin\]
-   Chore: adding reverse option for featurize many. \[Kevin\]
-   Chore: changing default. \[Kevin\]
-   Chore: updated exclude list. \[Kevin\]
-   Chore: changing default. \[Kevin\]
-   Chore: changing search cutoffs. \[Kevin\]
-   Chore: changing search cutoffs. \[Kevin\]
-   Chore: updated run_featurization_many. \[Kevin\]
-   Chore: added changelog. \[Kevin\]
-   Chore: fix in readme. \[Kevin\]

## v0.2.1 (2020-07-31)

### New

-   Feat: rename package BREAKING CHANGE This change is needed to make
    it easier to navigate between the different oximachine packages.
    \[Kevin\]
-   Featurization_many. \[Kevin\]
-   Featurization_many. \[Kevin\]
-   Featurization_many. \[Kevin\]
-   Feat: moving exclude list to separate module. \[Kevin\]
-   Feat: extending the list of excluded structures. \[Kevin\]
-   Feat: adding option to parse negative oxidation states. \[Kevin\]

### Changes

-   Chore: update readme. \[Kevin\]
-   Chore: completely dropping any previous python 2 support imports.
    \[Kevin\]
-   Chore: completely dropping any previous python 2 support imports.
    \[Kevin\]
-   Chore: updating readme and hopefully fixing failing test. \[Kevin\]
-   Chore: updated tests. \[Kevin\]
-   Chore: performance improvements in featurization. \[Kevin\]
-   Chore: lower logging level. \[Kevin\]
-   Chore: catch warning, make outdir. \[Kevin\]
-   Chore: using versioneer. \[Kevin\]
-   Chore: updated readme. \[Kevin\]
-   Chore: cleaned up repo. \[Kevin\]
-   Chore: cleaned up repo. \[Kevin\]
-   Chore: updating precommit, simplyfing dependencies. \[Kevin\]
-   Chore: updating precommit, simplyfing dependencies. \[Kevin\]
-   Chore: updating precommit, simplyfing dependencies. \[Kevin\]
-   Chore: updating precommit, simplyfing dependencies. \[Kevin\]
-   Chore: introduced timeout for featurization. \[Kevin\]
-   Chore: introduced timeout for featurization. \[Kevin\]
-   Chore: introduced timeout for featurization. \[Kevin\]
-   Chore: introduced timeout for featurization. \[Kevin\]
-   Chore: fixing dependencies. \[Kevin\]
-   Chore: working with oxidation state 0. \[kjappelbaum\]

### Fix

-   Vesion fixed. \[Kevin\]
-   Missing import. \[Kevin\]
-   Hopefully tests no longer fail. \[Kevin\]
-   Hopefully tests no longer fail. \[Kevin\]
-   Hopefully tests no longer fail. \[Kevin\]
-   Parsing returns no np.nan in case there is a metal with no oxidation
    state. \[Kevin\]
-   Exclude module. \[Kevin\]
-   Fixing typo in readme. \[Kevin\]
-   Fixing typo in comment. \[Kevin\]
-   Fixing typo in comment. \[Kevin\]

### Other

-   Really dirty, hardcoded timeout as passing the instance timeout
    variable to the decorator is quite nasty. \[Kevin\]
-   Really dirty, hardcoded timeout as passing the instance timeout
    variable to the decorator is quite nasty. \[Kevin\]
-   Really dirty, hardcoded timeout as passing the instance timeout
    variable to the decorator is quite nasty. \[Kevin\]
-   Really dirty, hardcoded timeout as passing the instance timeout
    variable to the decorator is quite nasty. \[Kevin\]
-   Adding note about metal centers to Readme. \[Kevin\]
-   Adding example explanation in readme. \[Kevin\]
-   Adding example notebook. \[Kevin\]
-   Updating readme. \[Kevin\]
-   Updating readme. \[Kevin\]
-   Updating readme. \[Kevin\]
-   Updating readme. \[Kevin\]
-   Changing license to GPL. \[Kevin\]
-   Should be python 3.5 compatible now. \[Kevin\]
-   Partially removing f strings for python3.5. \[Kevin\]
-   Python 3.5. \[Kevin\]
-   Python 3.5. \[Kevin\]
-   Return also featurenames. \[Kevin\]
-   Adding return_features function. \[Kevin\]
-   Clean up repo. \[Kevin\]
-   Adding zenodo badge. \[Kevin\]

## v0.2.0-alpha (2019-12-09)

-   Installation workaround. \[Kevin\]
-   Installation workaround. \[Kevin\]
-   Cleaning repo. \[Kevin\]
-   Cleaning repo. \[Kevin\]
-   Cleaning repo. \[Kevin\]
-   Cleaning repo. \[Kevin\]
-   Cleaning repo. \[Kevin\]
-   Cleaning repo. \[Kevin\]
-   Cleaning repo. \[Kevin\]
-   Create pythonpackage.yml. \[Kevin Jablonka\]
-   Cleaning up repo. \[Kevin\]

## v0.2.0a1 (2019-11-05)

### Fix

-   Fixed bug in feature names. \[kjappelbaum\]
-   Fixed bug in feature names. \[kjappelbaum\]
-   Fixed bug in feature names. \[kjappelbaum\]
-   Fix slicing. \[kjappelbaum\]
-   Fix outpath feature names. \[kjappelbaum\]

### Other

-   Starting cleaning. \[kjappelbaum\]
-   Added merging scripts, fixing errors in MP mining script. \[Kevin\]
-   Cleaning after linting, part 1. \[Kevin\]
-   New featurization version. \[Kevin Jablonka\]
-   Adding old_format mode. \[kjappelbaum\]
-   Backwards incompatbile changes in featruization and feature
    collection as old featurization only considered one metal site per
    structure. \[kjappelbaum\]
-   Ward prd -\> ward prb. \[kjappelbaum\]
-   Adding random column option. \[kjappelbaum\]
-   Adding random column option. \[kjappelbaum\]
-   Adding random column option. \[kjappelbaum\]
-   Exclude oxidation state 7. \[kjappelbaum\]
-   Row/column features. \[kjappelbaum\]
-   Row/column features. \[kjappelbaum\]
-   Excluding oxidation state 7 case. \[kjappelbaum\]
-   Float and not int \... \[kjappelbaum\]
-   Datatype percentage must be str. \[kjappelbaum\]
-   Drop duplicates via str. \[kjappelbaum\]
-   Print df for debugging. \[kjappelbaum\]
-   Print df for debugging. \[kjappelbaum\]
-   Print df for debugging. \[kjappelbaum\]
-   Print df for debugging. \[kjappelbaum\]
-   Holdout option in runscript. \[kjappelbaum\]
-   Updated featurecollector with ability for holdout set.
    \[kjappelbaum\]
-   Do not add cases where featurization failed. \[kjappelbaum\]
-   Add feature class selection as CLI argument. \[kjappelbaum\]
-   Exclude more. \[kjappelbaum\]
-   Added feature collection runscript. \[kjappelbaum\]
-   Ready for featurization. \[kjappelbaum\]
-   Added some logging statements. \[kjappelbaum\]
-   Added enviornment file. \[kjappelbaum\]
-   Adding cluster runscript. \[kjappelbaum\]
-   Added docs. \[Kevin Jablonka\]
-   Cleaning code. \[Kevin Jablonka\]
-   Adding tests. \[Kevin Jablonka\]
-   \[WIP\] featurization. \[kjappelbaum\]
-   Adding more parser tests. \[Kevin Jablonka\]
-   Mining code. \[kjappelbaum\]
-   \[WIP\] Distribution analysis: Run mining on MOF subset, now run
    reference on all structures. \[kjappelbaum\]
-   \[WIP\] Distribution analysis: Run mining on MOF subset, now run
    reference on all structures. \[kjappelbaum\]
-   Preparing parse run. \[kjappelbaum\]
-   Passed tests. \[kjappelbaum\]
-   Initial commit. \[kjappelbaum\]
-   Initial commit. \[Kevin\]

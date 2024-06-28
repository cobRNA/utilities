#!/usr/bin/env python3

"""
 Use to remove fakeExons after tmerging anchored TM.
 Loads fakeExons info from fakeExons file into set by
 chr,start,end,strand features. Subsequently, reads 
 tmergeOutput line by line and comapres mentioned features
 with those present in fake exons set.
 If they match, line is consider as fake exon and discarded.
 Operates on sets, so all duplicated lines are removed!
 Does not require sorted input to work correctly.
"""

import sys
import argparse


def remove_fakes(tmerged, fakes) -> set:
    """
    Read chr|start|end|strand exon info from tmerge set.
    If exon does not exist in fakes set, add it
    to new without_fakes set.
    After completion, return resulitng set.

    Args:
    tmerged (set): exons from anchored merging procedure. Contains fake exons.
    fakes (set): fake exons extracted after anchoring.

    Returns:
    set: exons from tmerged that were not common with fakes.
    """
    without_fakes = set()

    for transcript in tmerged:
        features_list = transcript.split()
        exon = features_list[0] + features_list[3] + features_list[4] + features_list[6]
        if exon not in fakes:
            without_fakes.add(transcript)

    # Report progress
    sys.stderr.write(f"Exons from tmergeOutput file: {len(tmerged)} \n")
    sys.stderr.write(f"FakeExons to remove: {len(fakes)} \n")
    sys.stderr.write(f"Resulting number of exons: {len(without_fakes)} \n")
    return without_fakes


def main() -> None:
    """
    Handles arguments, loads data into tmerged and fakes data sets.
    Returns exons set not containing fake exons to STDOUT.
    """
    # Handle comandline arguments
    parser = argparse.ArgumentParser(
        description="Removes fakeExons from tmergedOutput file.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-a",
        "--tmergedOutput",
        help="path to tmergedOutput file containing all exons",
        default=None,
    )

    parser.add_argument(
        "-f",
        "--fakeExons",
        help="path to fakeExons file containing only fake exons",
        default=None,
    )

    parser.add_argument(
        "-t",
        "--trueExons",
        help="path to trueExons file containing only true exons",
        default=None,
    )

    args = parser.parse_args()
    config = vars(args)

    # Open tmergedOutput file and load into memory
    # Set comprehension is used to:
    # - removed empty lines: "if x" part
    # - create fakes hash using only necessary features from input
    with open(config["tmergedOutput"], "r", encoding="utf-8") as file:
        tmerged = {x for x in file.read().split(sep="\n") if x}
    # Open fakeExons file and load into memory
    with open(config["fakeExons"], "r", encoding="utf-8") as file:
        fakes = {
            x.split()[0] + x.split()[3] + x.split()[4] + x.split()[6]
            for x in file.read().split(sep="\n")
            if x
        }
    # Open trueExons file and load into memory
    with open(config["trueExons"], "r", encoding="utf-8") as file:
        trues = {
            x.split()[0] + x.split()[3] + x.split()[4] + x.split()[6]
            for x in file.read().split(sep="\n")
            if x
        }

    # Create true_fakes set - in rare situations fake exons can align with short true exons
    true_fakes = fakes - trues

    # Remove fakeExons
    clean_set_of_exons = remove_fakes(tmerged=tmerged, fakes=true_fakes)

    # Return exons without fakes
    sys.stdout.write("\n".join(clean_set_of_exons))
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()

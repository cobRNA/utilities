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
    # Remove fake exons
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
    # Handle comandline arguments
    parser = argparse.ArgumentParser(
        description="Removes fakeExons from tmergedOutput file.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-t",
        "--tmergedOutput",
        help="path to tmergedOutput file",
        default=None,
    )

    parser.add_argument(
        "-f",
        "--fakeExons",
        help="path to fakeExons file",
        default=None,
    )

    args = parser.parse_args()
    config = vars(args)

    # Open tmergedOutput file and load into memory
    with open(config["tmergedOutput"], "r", encoding="utf-8") as file:
        tmerged = set([x for x in file.read().split(sep="\n") if x])
    # Open fakeExons file and load into memory
    with open(config["fakeExons"], "r", encoding="utf-8") as file:
        fakes = set(
            [
                x.split()[0] + x.split()[3] + x.split()[4] + x.split()[6]
                for x in file.read().split(sep="\n")
                if x
            ]
        )

    # Remove fakeExons
    clean_set_of_exons = remove_fakes(tmerged, fakes)

    # Return exons without fakes
    sys.stdout.write("\n".join(clean_set_of_exons))
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()

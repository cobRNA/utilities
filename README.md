# Utilities
Short shell, python and R scripts to get the work done.

# Content
## Bash scripts
### - `create_venv.sh`:
**Description:**
Automates creation of Python3.x virtual environment with preinstalled basic modules.

**Usage:**
Set prefered Python version (`Python3.11` by default)

Run in terminal: `./create_venv.sh [OPTIONAL_DIR_NAME]`

If `DIR_NAME` not supplied or already exists, prompt will appear

## Python scripts
### - `removeFakes.py`:
**Description:**
Created to remove fakeExons after anchored merging procedure.
Input:
tmerged+fakeExons.gtf - raw file created by tmerging anchored transcripts
fakeExonsToRemove.gff - file contating fake exons extracted just after anchoring by:
`cat anchored_transcripts.gff | grep 'fakeExon' > fakeExonsToRemove.gff`

**Usage:**
Run in terminal:
`./removeFakes.py -t tmerged+fakeExons.gtf -f fakeExonsToRemove.gff | sort -k1,1 -k4,4n -k5,5n | gzip > ExonsWithoutFakes.gz`


### - `targetsToTsv.py`:
**Description:**
Read targets from STDIN and converts it to tsv.
Crafted for the Hv3_CLS3_targetDesign.gtf.gz analysis in R.

**Usage:**
Run in terminal:
`zcat Hv3_CLS3_targetDesign.gtf.gz | ./targetsToTsv.py - > targets.tsv`


## R scripts
### - `name.r`:
**Description:**


**Usage:**
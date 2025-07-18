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

### - `shuffle_gtf.v1.sh`

**Description:**
Reads content of gtf file from STDIN and shuffles its content.
Before use adjust GENOME_FILE and SEED(optional) variables.

**Usage:**
Run in terminal: `cat input.gtf | ./shuffle_gtf.v1.sh - > output.gtf`

**Author:**
Rory Johnson

## Python scripts

### - `remove_fakes.py`:

**Description:**
Created to remove fakeExons after anchored merging procedure.
FakeExons are identified by hash created from concatenation of chr,start,end,strand.
Rarely, fakeExons can align with short trueExon of different transcript.
To avoid removing them this,

**Input:**
tmerged+fakeExons.gtf - raw file created by tmerging anchored transcripts
fakeExonsToRemove.gff - file contating fake exons extracted just after anchoring by:
`cat anchored_transcripts.gff | grep -wF 'fakeExon' > fakeExonsToRemove.gff`
trueExons.gff - file containing non-fake exons extracted just after anchoring by:
`cat anchored_transcripts.gff | grep -wFv 'fakeExon' > trueExons.gff`

**Usage:**
Run in terminal:
`./removeFakes.py -a tmerged+fakeExons.gtf -f fakeExonsToRemove.gff -t trueExons.gff | sort -k1,1 -k4,4n -k5,5n | gzip > ExonsWithoutFakes.gz`

### - `targets_to_tsv.py`:

**Description:**
Read targets from STDIN and converts it to tsv.
Crafted for the Hv3_CLS3_targetDesign.gtf.gz analysis in R.

**Usage:**
Run in terminal:
`zcat Hv3_CLS3_targetDesign.gtf.gz | ./targetsToTsv.py - > targets.tsv`

## Perl scripts

### - `simplifyGencodeGeneTypes.v27_M16.pl`:

### - `simplifyGencodeGeneTypes.v43_M32.pl`:

**Description:**
Source: https://github.com/julienlag/utils/blob/c57b06f99af92e60a89f3b1ad7a8a7ec02fdc475/simplifyGencodeGeneTypes.pl
Modified to work with Gencode.v27 / M16 and .v43 / M32 gene types respectively.

**Input:**
Raw Gencode annotation.

**Usage:**
Run in terminal:
`zcat gencode.v27.annotation.gtf.gz | ./simplifyGencodeTypes.v27_M16 - | gzip > gencode.v27.annotation.simplified.gtf.gz`

## R scripts

### - `name.r`:

**Description:**

**Usage:**

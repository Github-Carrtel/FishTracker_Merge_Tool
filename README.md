# FishTracker Merge Tool

> Python script for extracting, processing, and merging the data exported by the FishTracker software (version 0.1).

---

## 1. Metadata

| Field | Value |
|-------|-------|
| **Name** | FishTracker Merge Tool |
| **Version** | 1.0.0 |
| **Date** | April 2025 |
| **Authors / Developers** | Quentin Godeaux |
| **Contact** | quentin.godeaux@inrae.fr |
| **Laboratory / Responsible organisation** | INRAE — UMR CARRTEL (Centre Alpin de Recherche sur les Réseaux Trophiques et les Écosystèmes Limniques), Thonon-les-Bains, France |
| **License** | GNU General Public License v3.0 (GPL-3.0) |
| **Website** |  |
| **Source code** |  |
| **Scientific field** | Freshwater ecology, limnology, hydroacoustics, fish monitoring, scientific data processing |
| **Key features** | Extraction of dates and times from file names, merging of multiple FishTracker exports, data formatting |
| **Technologies** | Python 3.x, pandas |
| **Keywords** | FishTracker, acoustic camera, fish tracking, data processing, merge, Python, pandas |

---

## 2. Context & History

### History
- Preliminary material: 
- Previous versions: First identified version
- Integrated components and dependencies:
  - `pandas`: BSD license (compatible with GPL-3.0)
- Roadmap: 
- Equivalent software: 

### Related project(s)
-Reference publication:  Godeaux, Quentin, Hervé Rogissart, Clément Rautureau, François Martignac, Franck Cattanéo, et Jean Guillard. « Comparative evaluation of two automated fish counting software tools using acoustic camera data ». Ecological Informatics 97 (août 2026): 103904. https://doi.org/10.1016/j.ecoinf.2026.103904.

---

## 3. Objectives

### Scientific objectives
Facilitate the analysis of fish-monitoring data by consolidating multiple FishTracker track exports into a single, analysable dataset. The tool automates the extraction of acquisition dates and times from file names and standardises the output, so that downstream behavioural, abundance, or phenology analyses can be performed on a unified database rather than on scattered individual exports.

### Usage and dissemination objectives
- Expected lifetime: 
- Intended use: Scientific production, post-processing data analysis.
- Target audience: Researchers, engineers, and technicians.
- Dissemination objectives: Promote open science; provide a research‑data deposit ensuring transparency.
- Desired collaboration community: Yes.
- Preservation: 

---

## 4. Technical Features

- Technologies used: Python 3.x
- Dependencies: `pandas`, standard library (`os`)
- Reuse of existing building blocks: 
- Technical constraints: Strict compatibility with the naming and data format of FishTracker v0.1 (files ending in `_tracks.txt`).
- Standards and norms: Output files in CSV format, semicolon-delimited (`;`).

---

## 5. Installation & Usage

### Prerequisites
- Python 3.x environment
- `pandas` library

### Installation
Clone or download the repository, then install the dependencies (ideally in a virtual environment):
```bash
pip install pandas
```

### Quick start
1. Place the text files to be processed (ending in `_tracks.txt`) in a folder.
2. Edit the `FishTracker-Merge-Tool.py` file and set the `source_folder` variable to the folder path:
   ```python
   source_folder = r"/path/to/your/folder"
   ```
3. Run the script:
   ```bash
   python FishTracker-Merge-Tool.py
   ```
4. The merged file `CSOT_merged.txt` will be generated in the same folder.

---

## 6. Team & Development Organisation

### Governance
- Responsible organisation: INRAE/USMB — UMR CARRTEL

### Team
- Members: Quentin Godeaux, Hervé Rogissart, Clément Rautureau, François Martignac, Franck Cattanéo, Jean Guillard.

### Development organisation
- Methods and tools: Python 3.x developed in VS Code.
- Quality procedures: The script includes robust batch processing that skips incompatible files.
- Version, bug, and validation management: Git / GitHub (local).
- Documentation: Manual update of the README.

---

## 7. Distribution & Citation

### Reference repository
- Main repository URL: https://github.com/Github-Carrtel/FishTracker_Merge_Tool/
- Persistent identifier (DOI): https://doi.org/10.1016/j.ecoinf.2026.103904

### Citation
Godeaux, Quentin, Hervé Rogissart, Clément Rautureau, François Martignac, Franck Cattanéo, et Jean Guillard.(2026).« Comparative evaluation of two automated fish counting software tools using acoustic camera data ». Ecological Informatics 97: 103904. https://doi.org/10.1016/j.ecoinf.2026.103904.

---

## 8. Software Management Plan (SMP)

- SMP manager: 
- Update frequency: When major data‑set updates occur. 
- Link with the DMP (Data Management Plan): 

---

## 9. Legal & IP

- **Authors / Rights holders**: Quentin Godeaux, Hervé Rogissart, Clément Rautureau, François Martignac, Franck Cattanéo, Jean Guillard.  
- Code license: **GNU General Public License v3.0 (GPL-3.0)** 
- **Planned opening date**: Immediately upon publication.   [1]

---

*This README is structured according to the Research Software Management Plan Template, PRESOFT Project V3.2 (CNRS/IN2P3, 2018).*

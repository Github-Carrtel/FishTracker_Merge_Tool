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
| **Technologies** | Python 3.x (standard library only), PyInstaller |
| **Keywords** | FishTracker, acoustic camera, fish tracking, data processing, merge, Python, pandas |

---

## 2. Context & History

### History
- Preliminary material: 
- Previous versions: First identified version
- Integrated components and dependencies:
  - Python standard library only (`os`, `sys`, `csv`) — no third-party dependency
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
- Dependencies: none — Python standard library only (`os`, `sys`, `csv`); distributed as a standalone Windows executable built with PyInstaller
- Reuse of existing building blocks: 
- Technical constraints: Strict compatibility with the naming and data format of FishTracker v0.1 (files ending in `_tracks.txt`).
- Standards and norms: Output files in CSV format, semicolon-delimited (`;`).

---

## 5. Installation & Usage

There are two ways to use the tool. Both automatically use the folder where the program is located, so no path ever needs to be edited.

### Option A — Standalone executable (recommended, no installation)
A ready-to-use Windows executable (`FishTracker-Merge-Tool.exe`) is provided. It bundles everything needed: **no Python and no libraries have to be installed**.

1. Place `FishTracker-Merge-Tool.exe` in the same folder as the text files to be processed (the folder containing the `_tracks.txt` files).
2. Double-click the executable.
3. The merged file `CSOT_merged.txt` is generated in the same folder.

### Option B — Run the Python script
Requires only **Python 3.x** (no external library — the script uses the standard library only).

1. Place `FishTracker-Merge-Tool.py` in the same folder as the `_tracks.txt` files.
2. Run the script:
   ```bash
   python FishTracker-Merge-Tool.py
   ```
3. The merged file `CSOT_merged.txt` is generated in the same folder.

### Rebuilding the executable (optional, for developers)
The executable can be regenerated from the script with [PyInstaller](https://pyinstaller.org/):
```bash
pip install pyinstaller
pyinstaller --onefile --console --name "FishTracker-Merge-Tool" FishTracker-Merge-Tool.py
```
The resulting `FishTracker-Merge-Tool.exe` is created in the `dist/` folder.

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

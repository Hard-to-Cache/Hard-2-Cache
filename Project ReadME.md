# HardToCache: Automated Artifact Scoring Framework

## Project Overview
HardToCache is a reproducible science framework that automates the evaluation and scoring of scientific artifacts (research papers, datasets, and technical documents). This project addresses key challenges in research reproducibility by creating a standardized scoring system, automating data collection, and generating visual reports for transparent evaluation.

### Key Features
- 🖥️ **Integrated Web Dashboard**: Project website with embedded scorecard visualizations
- 📊 **Automated Scoring System**: Quantitative evaluation of research artifacts using predefined metrics
- 🤖 **Web Scraping Pipeline**: Automated data collection from scientific sources
- 🖨️ **Printable Poster Template**: Conference-ready visual summary of findings
- 🔄 **Reproducible Workflow**: Version-controlled automation via GitHub

## Reproducible Science Framework
Our solution enhances research reproducibility through:

1. **Standardized Evaluation Metrics**
   - Consistent scoring criteria across all artifacts
   - Transparent weighting system for quality assessment
   
2. **Automated Data Processing**
   - Web scraping pipeline for data collection
   - Automated scoring calculations
   - Version-controlled data transformations

3. **Visual Transparency**
   - Embedded scorecard visualizations in web and print formats
   - Publicly accessible evaluation methodology
   - Team bios and contribution tracking

4. **Open Workflow**
   - GitHub-based version control
   - Containerized execution environment
   - Complete documentation of methodology

## Technology Stack
- **Python**: Core programming language for web scraping and data processing
- **Google Colab**: Cloud-based environment for automation scripts
- **GitHub Pages**: Hosting for the project website
- **Terminal/Virtualenv**: Local development environment
- **Canva**: Poster design and visual layout
- **Google Docs/Sheets**: Collaborative content creation and scorecard metrics
- **PyMuPDF (PyPDF2)**: PDF processing and text extraction
- **SGX3 Project Server**: Secure environment for processing sensitive research data
- **HTML/CSS**: Website frontend implementation

## Project Timeline
| Date       | Milestone |
|------------|-----------|
| June 23    | Received scoring criteria, initial setup |
| June 24    | Website layout draft, team bios collection |
| June 25    | Poster design, score embedding |
| June 26    | Finalized website and poster |
| **June 27** | **Presentation & Q&A support** |

## Installation & Usage
# Clone repository
git clone https://github.com/your-username/HardToCache.git

# Install dependencies
pip install -r requirements.txt

# Run web scraper
python scraper.py

# Generate scorecard
python scorecard_processor.py

# Launch local server (SGX3 compatible)
python -m http.server --dir ./output

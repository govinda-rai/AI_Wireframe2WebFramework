# Placeholder for README.md
# AI Test Framework

## Overview
This framework automates the comparison of wireframes with actual websites using AI-powered layout analysis and functionality testing.

## Features
- **Layout Analysis**: Detect mismatches between wireframes and live UI using YOLO.
- **Functional Testing**: Validate UI components using Selenium.
- **Automated Reporting**: Generates detailed reports for mismatches and failed test cases.

## Installation
### Prerequisites
Ensure you have Python installed (>=3.8).

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
Run the framework with:
```bash
python main.py
```

## Project Structure
```
ai_test_framework/
│
├── wireframe_comparator/
│   ├── layout_analysis.py
│   ├── functionality_check.py
│   ├── report_generator.py
│
├── yolo_model/
│   ├── yolov5s.pt
│   ├── labels.yaml
│
├── tests/
│   ├── test_image_processing.py
│   ├── test_layout_analysis.py
│
├── requirements.txt
├── README.md
├── main.py
```

## Output
After execution, the framework generates a `report.json` containing:
- Detected layout mismatches
- Functional test results

## Contributing
Feel free to submit issues and pull requests.

## License
This project is licensed under the MIT License.

# Placeholder for project_doc.md
# AI Test Framework - Project Documentation

## Introduction
This document provides an in-depth explanation of the AI Test Framework, detailing its components, working mechanisms, and usage.

## Objective
The AI Test Framework automates the verification of UI layouts and functionality by comparing wireframes with developed websites using AI.

## Key Components
1. **Layout Analysis**
   - Uses YOLO for object detection to identify UI elements in wireframes and screenshots.
   - Compares bounding boxes to detect mismatches.

2. **Functional Testing**
   - Uses Selenium to validate UI functionality.
   - Automates user interactions like button clicks and form submissions.

3. **Reporting**
   - Generates a `report.json` with detected layout mismatches and functional test results.

## Installation & Setup
1. Ensure Python (>=3.8) is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

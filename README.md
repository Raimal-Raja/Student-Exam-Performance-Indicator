# Student-Exam-Performance-Indicator

Flask student-performance prediction project with data-processing, model-training, and inference pipeline components.

## Setup and repository reference

### Project structure

- [app.py](app.py)
- [application.py](application.py)
- [artifacts](artifacts)
- [catboost_info](catboost_info)
- [notebook](notebook)
- [requirements.txt](requirements.txt)
- [setup.py](setup.py)
- [src](src)
- [templates](templates)

### Getting started

```bash
git clone https://github.com/Raimal-Raja/Student-Exam-Performance-Indicator.git
cd Student-Exam-Performance-Indicator
```

Create and activate a virtual environment, then install the project dependencies:

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r "requirements.txt"
```

Application entry point:

```bash
python application.py
```

### Configuration and limitations

Training needs the input dataset and the dependencies in requirements.txt. Inference loads artifacts/model.pkl and artifacts/preprocessor.pkl relative to the project. Regression tests use synthetic models; full training and saved production artifacts were not exercised.

### Maintenance fixes

- Preserve intended error messages when no exception traceback is active.
- Resolve prediction artifacts from the project directory instead of the process working directory.
- Support saving a model to a filename in the current directory.

### Validation

Recorded checks from the previous maintenance review (2026-10-08): 14 existing Python files passed syntax checks; changed files and new regression tests were checked separately. 4 regression tests passed. Syntax checks do not establish full runtime correctness. External APIs, live scraping, GUI interaction, notebook training and production deployment were not comprehensively exercised.

```bash
python -m unittest discover -s tests -v
```

### Contributions

Describe the issue, reproduction steps, environment, and expected behavior when proposing a change. Keep generated environments, credentials, and unnecessary build artifacts out of new commits.

### License

No top-level license file was found during this review.

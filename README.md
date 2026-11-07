
# AI Code Reviewer

An AI-powered code review application built using Python, Streamlit, and multiple Large Language Model (LLM) providers.

AI Code Reviewer uses a task-based routing system to perform specialized code analysis, including bug detection, security auditing, and deep architectural review.

---

## Overview

AI Code Reviewer allows developers to upload source code files or paste code directly into the application for automated analysis.

The application uses three different LLM providers through LangChain integrations:

- **Groq:** Used for quick bug detection.
- **Mistral:** Used for security auditing.
- **Google Gemini:** Used for deep architectural code review.

The application provides a Streamlit interface to execute reviews, display results, generate Markdown reports, and create PNG summary charts.

## Features

- Upload source code files or paste code directly.
- Optional programming language selection.
- Automated bug detection.
- Security auditing.
- Deep architectural code review.
- Task-based LLM routing.
- Integration with Groq, Mistral, and Google Gemini.
- Markdown review report generation.
- Review summary metrics.
- PNG summary chart generation.
- Configurable chart generation (1–5 charts).

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| LLM Integration | LangChain |
| Bug Detection | Groq |
| Security Audit | Mistral |
| Deep Code Review | Google Gemini |
| Environment Management | python-dotenv |
| Data Visualization | Matplotlib |
| Report Generation | Markdown |

## Project Structure

```text
aicode-reviewer/
│
├── agents/
│   ├── reviewer.py
│   └── router.py
│
├── animations/
│   └── loader.py
│
├── output/
│   ├── reports/
│   └── charts/
│
├── Test_code_file/
│   └── mainn.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Architecture

The application consists of three main components:

### 1. User Interface – `app.py`

- Provides the Streamlit interface.
- Handles source code uploads and direct code input.
- Detects programming languages based on file extensions.
- Allows users to specify a language hint.
- Executes the full code review.
- Displays review metrics and detailed results.
- Generates downloadable Markdown reports and PNG charts.

### 2. Review Engine – `agents/reviewer.py`

The review engine coordinates three specialized review tasks through `run_full_review()`:

- Bug Detection
- Security Audit
- Deep Code Review

It collects the responses from all three LLM providers and returns them as a dictionary.

### 3. LLM Router – `agents/router.py`

The router manages LLM client initialization and task-based model selection.

It defines five task types:

- `QUICK_BUG`
- `SECURITY_AUDIT`
- `DEEP_REVIEW`
- `MENTOR_CHAT`
- `ANTI_PATTERN`

The routing table maps each task to its corresponding LLM provider.

## How It Works

### Step 1: Code Input

Users can submit source code through either of the following methods:

- Upload a source code file.
- Paste code directly into the Streamlit text area.

An optional programming language hint can also be provided.

### Step 2: Language Detection

The application identifies the programming language using the uploaded file's extension.

Supported file extensions:

| Extension | Language |
|---|---|
| `.py` | Python |
| `.js` | JavaScript |
| `.ts` | TypeScript |
| `.java` | Java |
| `.c` | C |
| `.cpp` | C++ |
| `.cs` | C# |
| `.go` | Go |
| `.rb` | Ruby |
| `.php` | PHP |
| `.html` | HTML |
| `.css` | CSS |

Users can also manually provide a language hint.

### Step 3: Run Full Review

After submitting the code, users click the **Run Full Review** button.

The application calls `run_full_review()` from `agents/reviewer.py`.

### Step 4: Specialized Code Analysis

The review engine executes three independent review passes.

**Bug Detection – Groq**

- Performs a quick scan of the submitted code.
- Identifies potential bugs.
- Uses the `QUICK_BUG` task type.

**Security Audit – Mistral**

- Analyzes the submitted code for potential security issues.
- Uses the `SECURITY_AUDIT` task type.

**Deep Code Review – Google Gemini**

- Performs a comprehensive architectural review.
- Uses the `DEEP_REVIEW` task type.

### Step 5: Result Generation

The responses from the three review passes are collected in a dictionary containing:

- `bugs`
- `security`
- `deep_review`

The results are displayed in separate sections in the Streamlit interface.

### Step 6: Report and Chart Generation

After the review is completed, the application:

- Generates a Markdown report.
- Calculates keyword-based review summary metrics.
- Generates PNG summary charts.
- Displays the generated charts in the application.

---

## Installation and Setup

### Prerequisites

- Python 3.10 or higher.
- pip package manager.
- API credentials for Groq, Mistral, and Google Gemini.

### 1. Clone the Repository

```bash
git clone https://github.com/iisamridhii/aicode-reviewer.git
```

Navigate to the project directory:

```bash
cd aicode-reviewer
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
venv\Scripts\activate.bat
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

Install the packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Configure API Keys

Create a `.env` file in the root directory of the project.

Add the following API credentials:

```env
GROQ_API_KEY=your_groq_api_key
MISTRALAI_API_KEY=your_mistral_api_key
GOOGLE_API_KEY=your_google_api_key
```

The application uses `load_dotenv()` from `python-dotenv` to load environment variables.

**Note:** Keep your API credentials private. Do not upload your `.env` file to GitHub.

### 6. Run the Application

Execute the following command:

```bash
streamlit run app.py
```

After successful execution, Streamlit displays a local URL in the terminal.

Open the URL in your browser:

```text
http://localhost:8501
```

---

## Usage

1. Launch the application.
2. Open the sidebar containing the application settings.
3. Upload a source code file or paste code directly into the text area.
4. Optionally enter the programming language.
5. Select the number of charts to generate using the slider.
6. Click **Run Full Review**.
7. Wait for the three review passes to complete.
8. View the generated review summary and detailed results.
9. Download the Markdown review report.

---

## Programmatic Usage

The review engine can also be accessed independently of the Streamlit interface.

Import the `run_full_review()` function:

```python
from agents.reviewer import run_full_review

code = """
def add(a, b):
    return a + b
"""

results = run_full_review(
    code=code,
    language="Python"
)

print(results.keys())
```

Expected output:

```python
dict_keys(['bugs', 'security', 'deep_review'])
```

The function returns a dictionary containing the responses from all three review passes.

---

## Output

The application generates two types of output files.

### 1. Markdown Reports

The application generates a Markdown report containing the results of the three review passes.

Output directory:

```text
output/reports/
```

Report filenames are generated using the source filename.

### 2. PNG Summary Charts

The application generates PNG charts representing the review summary metrics.

Output directory:

```text
output/charts/
```

Chart filenames follow this naming convention:

```text
review_summary_1.png
review_summary_2.png
review_summary_3.png
```

The number of charts generated depends on the value selected using the sidebar slider.

---

## Important Files

| File | Description |
|---|---|
| `app.py` | Streamlit interface and application orchestration |
| `agents/reviewer.py` | Executes the three specialized review tasks |
| `agents/router.py` | Initializes LLM clients and handles task-based routing |
| `animations/loader.py` | Contains the console loader function |
| `requirements.txt` | Lists project dependencies |
| `.gitignore` | Specifies files and directories excluded from Git |

---

## Troubleshooting

### 1. Streamlit Command Not Found

If the terminal does not recognize the Streamlit command:

- Ensure the virtual environment is activated.
- Verify that the dependencies have been installed.

Run:

```bash
pip install -r requirements.txt
```

Then:

```bash
streamlit run app.py
```

### 2. LLM Client Initialization Errors

If an LLM client fails to initialize:

- Verify that the API key is valid.
- Check the environment variable names.
- Ensure the `.env` file is located in the project root.
- Verify that the required provider packages are installed.

### 3. Review Execution Errors

If an error occurs during code review:

- Check the terminal for the displayed error traceback.
- Verify the provider API credentials.
- Check the availability of the configured LLM provider.

### 4. Empty Code Input

If no source code is provided, the application displays a warning asking the user to upload a file or paste code before running the review.

---

## Repository

GitHub Repository:

https://github.com/iisamridhii/aicode-reviewer



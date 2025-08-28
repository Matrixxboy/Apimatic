# Apimatic CLI 🚀  

[![Matrixxboy](https://img.shields.io/badge/github-Matrixxboy-purple.svg)](https://github.com/Matrixxboy)
[![npm version](https://badge.fury.io/js/Apimatic-cli.svg)](https://www.npmjs.com/package/Apimatic-cli)
[![npm downloads](https://img.shields.io/npm/dt/Apimatic-cli.svg)](https://www.npmjs.com/package/Apimatic-cli)
[![License](https://img.shields.io/npm/l/Apimatic-cli.svg)](https://github.com/Matrixxboy/Apimatic-cli/blob/main/LICENSE)

A **Node.js CLI wrapper** for the [Apimatic Python package](https://pypi.org/project/Apimatic/).  
It allows you to run Apimatic commands directly from Node / npm while leveraging the underlying Python engine.  

---

Here’s a **cleaned-up and more beginner-friendly version** of your installation guide:

---

## 📦 Installation Guide

### 1️⃣ Install the CLI (NPM)

```bash
# Install globally via npm
npm install -g apimatic-cli
```

### 2️⃣ Install the Python Package (PyPI)

```bash
# Install globally via pip
pip install Apimatic
```

⚠️ **Note:**

* This CLI is just an NPM wrapper around the Python package.
* You **must install both** for it to work correctly.

---

## ✅ Verify Installation

```bash
# Check if apimatic-cli is installed globally
npm list -g --depth=0

# Check if Apimatic is installed globally in Python (avoid virtualenvs)
pip list
```

You should see both **`apimatic-cli`** (npm) and **`Apimatic`** (pip) listed.

---

## 🔄 Upgrade to Latest Version

```bash
# Update the npm wrapper
npm update -g apimatic-cli

# Upgrade the Python package
pip install --upgrade Apimatic
```

---

Would you like me to also make a **diagram/flowchart image** showing how `apimatic-cli (npm)` just calls `Apimatic (Python)` so users instantly understand the relationship?

---

## ⚡ Usage

Apimatic now uses commands to separate actions.

**1. Generate Documentation:**
```bash
apimatic generate [OPTIONS]
```

**2. Configure API Keys:**
```bash
apimatic config [OPTIONS]
```

This internally calls the Python module: `python3 -m Apimatic.cli [command] [options]`

---

## 🔑 Configuration

To use AI enhancements from providers like OpenAI, Google Gemini, or Groq, you must set an API key.

```bash
# Set your OpenAI API key
apimatic config --set-openai-key YOUR_API_KEY

# Set your Google Gemini API key
apimatic config --set-gemini-key YOUR_API_KEY

# Set your Groq API key
apimatic config --set-groq-key YOUR_API_KEY
```
The key will be stored securely in your home directory for the Python package to use.

---

## ⚙️ Generation Options

| Option | Description |
| --- | --- |
| `-h, --help` | Show help message and exit |
| `--src SRC` | Root directory of the project to scan (Default: current directory) |
| `--framework [FRAMEWORK ...]` | Force a specific framework (`flask`, `fastapi`, etc.). If omitted, auto-detected |
| `--format {markdown}` | Output format (Default: `markdown`) |
| `--output OUTPUT` | Path for the generated output file (Default: `API_Docs.md`) |
| `--use-ollama` | Enhance with a local Ollama model |
| `--ollama-model MODEL` | Ollama model to use (e.g., `phi3:mini`) |
| `--use-openai` | Enhance with an OpenAI model |
| `--openai-model MODEL` | OpenAI model to use (e.g., `gpt-4o-mini`) |
| `--use-google-gemini` | Enhance with a Google Gemini model |
| `--google-gemini-model MODEL` | Gemini model to use (e.g., `gemini-1.5-flash`) |
| `--use-groq` | Enhance with a Groq model |
| `--groq-model MODEL` | Groq model to use (e.g., `llama3-8b-8192`) |

---

## 📝 Examples

**Basic Generation:**
```bash
# Generate Markdown docs from the current project
apimatic generate --src . --output API_Docs.md
```

**AI-Enhanced Documentation:**

First, set your key:
```bash
apimatic config --set-openai-key sk-xxxxxxxx
```
Then, generate with enhancement:
```bash
# Use OpenAI's gpt-4o-mini model
apimatic generate --src . --use-openai --openai-model gpt-4o-mini

# Use a local Ollama model
apimatic generate --src . --use-ollama --ollama-model phi3:mini
```

---

## 🤖 Recommended AI Models

| Provider | Recommended Model | Notes |
| --- | --- | --- |
| **Ollama (Local)** | `phi3:mini`, `llama3:8b` | Fast, free, and runs on your machine. Great for privacy. |
| **OpenAI** | `gpt-4o-mini` | Excellent balance of cost, speed, and intelligence. |
| **Google Gemini** | `gemini-1.5-flash` | Fast and cost-effective model from Google. |
| **Groq** | `llama3-8b-8192` | Incredibly fast inference speeds. |

---

## ⚙ Requirements

* **Node.js** (v16+ recommended)
* **Python 3.9+** installed and available as `python` or `python3`
* **Apimatic Python package** installed:

  ```bash
  pip install Apimatic
  ```

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo, make your changes, and submit a PR.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).



---

✨ This version is tailored for **npm users**, with:
- npm badges instead of PyPI  
- `npm install -g Apimatic-cli` instructions  
- Keeps the **same CLI usage table** so both pip & npm users get consistent docs  

---

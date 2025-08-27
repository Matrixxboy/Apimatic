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

Once installed, you can run:

```bash
Apimatic [options]
```

This internally calls:

```bash
python3 -m Apimatic.cli [options]
```

---

## 🔑 Options

| Option                        | Description                                                                      |
| ----------------------------- | -------------------------------------------------------------------------------- |
| `-h, --help`                  | Show help message and exit                                                       |
| `--src SRC`                   | Root directory of the project to scan (Default: current directory)               |
| `--framework [FRAMEWORK ...]` | Force a specific framework (`flask`, `fastapi`, etc.). If omitted, auto-detected |
| `--format {markdown,openapi}` | Output format (`markdown` or `openapi`) – Default: `markdown`                    |
| `--output OUTPUT`             | Path for the generated output file (Default: `API_Docs.md` or `openapi.yaml`)    |
| `--use-ollama`                | Enhance generated docs with descriptions from a local Ollama model               |
| `--model MODEL`               | Ollama model for enhancement (e.g., `llama3:instruct`). Requires `--use-ollama`  |

---

## 📝 Examples

Generate Markdown docs:

```bash
Apimatic --src . --format markdown --output API_Docs.md
```

Generate OpenAPI spec:

```bash
Apimatic --src . --format openapi --output openapi.yaml
```

Force framework detection (Flask):

```bash
Apimatic --src ./my_flask_app --framework flask
```

Enhance docs with AI (Ollama):

```bash
Apimatic --src . --use-ollama --model llama3.2:1b
```

---

## 🤖 Recommended Ollama Models (1–2 GB)

When using `--use-ollama`, you can choose a local model for API explanations:

| Model         | Size    | Why Use It                                                                  |
| ------------- | ------- | --------------------------------------------------------------------------- |
| `llama3.2:1b` | \~1.3GB | Fast, nimble, and great for generating clear API explanations (recommended) |
| `gemma2:2b`   | \~1.6GB | Slightly larger, richer outputs, good balance of quality and size           |
| `dolphin-phi` | \~1.6GB | Alternative small model with solid reasoning ability                        |
| `orca-mini`   | \~1.9GB | Bigger (3B params) but still under 2GB; more context-aware                  |
| `moondream2`  | \~0.8GB | Ultra-light, very fast, but less detailed                                   |

👉 **Recommended Default**: `llama3.2:1b`

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

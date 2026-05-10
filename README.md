<div align="center">

# ⚙️ RepoForge

**Forge your project structure in seconds.**

*A desktop app that automates repository creation with professional templates — no terminal required.*

---

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.x-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange?style=for-the-badge)

</div>

---

## 📌 Overview

Every developer knows the pain: you have a great idea, but before writing a single line of meaningful code, you spend 10 minutes creating folders, adding boilerplate files, and setting up the same structure you've done a hundred times before.

**RepoForge eliminates that friction.**

It's a modern desktop application built with Python and CustomTkinter that generates complete, professional project structures for the most common tech stacks — with a single click, no terminal required.

---

## ❓ Why RepoForge?

| Without RepoForge | With RepoForge |
|---|---|
| Manually create each folder | Click once, done |
| Forget files like `.gitignore` or `.env` | Every file included by default |
| Repeat the same setup every project | Consistent structure every time |
| Risk typos in folder names | Predefined, battle-tested templates |
| Open terminal, remember commands | Clean GUI — just point and click |

> RepoForge doesn't replace Git or your IDE. It gives you the perfect starting point so you can focus on what actually matters: **building.**

---

## ✨ Features

- 🖥️ **Modern dark UI** built with CustomTkinter
- 📁 **Automatic folder and file generation** using Python's `pathlib`
- 🧩 **4 ready-to-use templates** for popular tech stacks
- 🔍 **Duplicate project detection** — prevents overwriting existing folders
- ⚡ **Instant boilerplate** — from zero to structured project in under 5 seconds
- 🧼 **No terminal needed** — fully GUI-driven experience

---

## 🧩 Available Templates

### 🐍 Python CLI
```
project/
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── __init__.py
├── .gitignore
├── requirements.txt
└── README.md
```

### ⚡ FastAPI
```
project/
├── app/
│   ├── __init__.py
│   ├── routes/
│   ├── models/
│   ├── services/
│   ├── database/
│   └── main.py
├── tests/
│   └── __init__.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### ⚛️ React
```
project/
├── src/
│   ├── components/
│   ├── pages/
│   ├── hooks/
│   ├── assets/
│   ├── App.jsx
│   └── main.jsx
├── public/
│   └── index.html
├── .gitignore
├── package.json
└── README.md
```

### 🤖 Discord Bot
```
project/
├── commands/
├── events/
├── utils/
├── .env
├── .gitignore
├── main.py
└── requirements.txt
```

---

## 🖼️ Preview

```
┌─────────────────────────────────┐
│           ⚙️  RepoForge          │
│                                 │
│       [ New Project [+] ]       │
│                                 │
│  Project name                   │
│  ┌───────────────────────────┐  │
│  │ insert the name           │  │
│  └───────────────────────────┘  │
│                                 │
│  Project description            │
│  ┌───────────────────────────┐  │
│  │ insert the description    │  │
│  └───────────────────────────┘  │
│                                 │
│  Select your technology         │
│  ┌──────────────────────────┐   │
│  │       Python CLI         │   │
│  ├──────────────────────────┤   │
│  │         FastAPI          │   │
│  ├──────────────────────────┤   │
│  │          React           │   │
│  ├──────────────────────────┤   │
│  │       Discord Bot        │   │
│  └──────────────────────────┘   │
│                                 │
│  [ ✅ Create FastAPI repo ]     │
│                                 │
│  Project my-api created! ✓      │
└─────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| [Python 3.10+](https://python.org) | Core language |
| [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) | Modern GUI framework |
| [pathlib](https://docs.python.org/3/library/pathlib.html) | Filesystem operations |

---

## ⚙️ How It Works

RepoForge keeps it simple under the hood:

1. **Template definitions** — each tech stack is mapped to a list of files and folders inside a Python dictionary
2. **Path resolution** — `pathlib.Path` builds the full path for each item relative to the project name the user provides
3. **Smart creation** — items ending with `/` are created as directories; everything else is created as an empty file with `.touch()`
4. **Duplicate check** — before creating anything, RepoForge verifies whether a folder with that name already exists in the current directory
5. **User feedback** — a label updates in real time to confirm success or warn about errors

No magic. Just clean, readable Python.

---

## 📦 Installation

**Prerequisites:** Python 3.10 or higher

```bash
# 1. Clone the repository
git clone git clone <repository-url>

# 2. Install dependencies
pip install customtkinter

# 3. Run the app
python main.py
```

> No virtual environment is required, but it's always a good practice to use one.

---

## 🚀 Usage

1. Open the app with `python main.py`
2. Click **New Project [+]**
3. Enter your **project name** (this will be the folder name)
4. Enter an optional **description**
5. Select your **technology template**
6. Click the **Create repo** button
7. Your project structure is ready inside the current directory ✅

---

## 🔍 Example

Given project name `my-fastapi-app` with the **FastAPI** template selected, RepoForge will generate:

```
my-fastapi-app/
├── app/
│   ├── __init__.py
│   ├── routes/
│   ├── models/
│   ├── services/
│   ├── database/
│   └── main.py
├── tests/
│   └── __init__.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

Ready to `cd` into and start coding immediately.

---

## 📁 RepoForge Project Structure

```
repoforge/
├── main.py          # Entry point — UI and logic
├── requirements.txt # Project dependencies
└── README.md        # This file
```

> The project is intentionally kept simple and single-file for now. Refactoring into modules (`core/`, `ui/`) is planned for future versions.

---

## 🗺️ Roadmap

### Version 1.0 — Current
- [x] Dark mode UI with CustomTkinter
- [x] 4 project templates
- [x] Automatic folder/file generation
- [x] Duplicate project detection
- [x] User feedback labels

### Version 1.1 — Planned
- [ ] GitHub API integration — create remote repo automatically
- [ ] Custom output directory selector
- [ ] Token-based authentication with secure local storage

### Version 1.2 — Future
- [ ] Auto Git initialization and first commit (via subprocess)
- [ ] Custom template creator
- [ ] Settings screen with persistent configuration
- [ ] README auto-generation based on project name and description

### Version 2.0 — Long-term vision
- [ ] Git operations without Git installed (pure Python)
- [ ] One-click: local structure + GitHub repo + first push
- [ ] Executable distribution via PyInstaller

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for new templates, features, or bug fixes:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please keep PRs focused and well-described.

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it.

See the [LICENSE](LICENSE) file for details.

---

## 🙏 Credits

Built with focus, curiosity, and a genuine desire to solve a real developer problem.

Special thanks to:
- [Tom Schimansky](https://github.com/TomSchimansky) for the excellent CustomTkinter library
- The Python community for `pathlib` and the broader standard library

---

<div align="center">

Made with ☕ and Python

⭐ If RepoForge saved you time, consider starring the repo!

</div>


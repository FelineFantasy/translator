# Console Translator 🌐

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![deep_translator](https://img.shields.io/badge/deep_translator-1.x-orange.svg)](https://pypi.org/project/deep-translator/)

A simple console translator written in Python. Translate text between Russian and English languages right in your terminal!

## 📋 Table of Contents
- [Description](#description)
- [How to Use](#how-to-use)
- [Installation](#installation)
- [Example Usage](#example-usage)
- [Project Files](#project-files)
- [Requirements](#requirements)
- [Future Plans](#future-plans)
- [Author](#author)

## 📝 Description

**Console Translator** is a simple program for translating text directly from the command line. It uses the `deep_translator` library, which connects to Google Translate for high-quality translations.

### Features:
- 🔄 **Two directions** — Russian → English and English → Russian
- 🚀 **Instant translation** — Fast response from Google Translate
- 📦 **Minimalism** — Simple interface without unnecessary features
- 🛡️ **Reliability** — Error handling during translation
- 🔌 **No API keys required** — Works out of the box

## 🎮 How to Use

1. Run the program
2. Select translation direction (1 or 2)
3. Enter text to translate
4. Get the translation

## ⚙️ Installation

### Option 1: Download ZIP
1. Click the green **"Code"** button on this page
2. Select **"Download ZIP"**
3. Extract the archive
4. Install dependencies: `pip install -r requirements.txt`
5. Run the program: `python translator.py`

### Option 2: Clone repository
```bash
git clone https://github.com/FelineFantasy/translator.git
cd translator
pip install -r requirements.txt
python translator.py
```

## 💻 Example Usage

```
Select translation direction:
1. Russian → English
2. English → Russian
> 1

Enter text: Привет, мир!
Translation: Hello, world!
```

## 📁 Project Files

```
translator/
├── translator.py       # Main program file
├── requirements.txt    # Dependencies
├── .gitignore          # Files and folders ignored by Git
└── README.md           # Documentation
```

## 📋 Requirements

- Python 3.x
- deep_translator

## 🔮 Future Plans

- [ ] Add support for more languages
- [ ] Translation history
- [ ] Save translations to file

## 👤 Author
- **FelineFantasy**
- **License**: MIT

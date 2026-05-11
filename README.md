# Text Swap

A lightweight Python tool to find and replace a word or phrase across all files of a given suffix in a directory — fast, local, and dependency-free.

No CLI. No config files. No cloud.
Just point it at a folder and go.

## ✨ Features

📁 Targets all files of a given suffix in a directory
🔍 Find and replace any word or phrase
🔡 Optional case-insensitive matching
🖥️ Minimal dark-themed GUI built with CustomTkinter
🔐 100% offline — nothing leaves your machine
🐍 Pure Python standard library (no dependencies for the core)

## 📦 Installation

1. Download the latest release from Releases

2. Extract the ZIP

3. Run Text_Swap.exe

No installer required.
No Python required.

## 📦 Requirements (for Developers)

Python 3.10+

For the GUI only:

```bash
pip install -r requirements.txt
```

## 🧭 How It Works

1. Choose the directory containing your files
2. Set the file suffix (e.g. `.txt`, `.sql`)
3. Enter the word or phrase to find, and what to replace it with
4. Hit **Run**

The tool processes every matching file in the directory and reports how many replacements were made per file.

## ⚙️ Function Reference

```python
swap(directory, suffix, find, replace, case_insensitive=False)
```

| Parameter | Type | Description |
|---|---|---|
| `directory` | `str` | Path to the target folder |
| `suffix` | `str` | File extension to target, e.g. `.txt` or `.sql` |
| `find` | `str` | Word or phrase to search for |
| `replace` | `str` | Word or phrase to replace with |
| `case_insensitive` | `bool` | Case-insensitive matching. Defaults to `False` |

## 📝 Notes

- Only files directly inside `directory` are processed — subdirectories are ignored
- Files are read and written as UTF-8; unreadable files are skipped
- Special regex characters in the `find` string are treated as plain literals

## 📄 License

MIT License

## ❤️ Why Batch Replace?

Because small tools should:

- Do one thing well
- Stay out of your way
- Respect your files

## 💬 Feedback

Issues and suggestions are welcome via GitHub Issues.
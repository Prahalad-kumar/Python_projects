# 🎭 Mad Libs Generator

A small, colorful, and user-friendly Mad Libs CLI built with Python. Fill in placeholders in a template story and get a silly, shareable result! 🌟

This README explains how to run the app, install optional enhancements, and customize the story template.

## ✨ Features

- Reads a story template at `story.txt` with placeholders like `<adjective>` or `<animal>`.
- Friendly, colored prompts for each placeholder (uses `colorama` if available). 🎨
- Saves completed stories to timestamped text files (optional). 💾
- Clear-screen, play-again loop, and safe handling of interrupts. ⏪

## 🧩 Story format

Placeholders are specified using angle brackets. Example in `story.txt`:

```
Once upon a time, there was a <adjective> <animal> who loved to <verb>.
```

The app will find each unique placeholder (order preserved) and ask you to provide a value for it.

## 🚀 Quick start

1. Make sure you're in this folder (where `App.py` and `story.txt` live).
2. (Optional) Install `colorama` for nicer cross-platform colors:

```bash
pip install colorama
```

3. Run the app:

```bash
python App.py
```

Follow the prompts to enter words for each placeholder. When the story is shown, you'll be asked whether to save it and whether you'd like to play again.

## 🛠️ Tips

- Empty input: if you just press Enter for a prompt, the placeholder will remain (wrapped in `<...>`). This helps you skip if you want to keep the original placeholder.
- To add your own story: edit `story.txt` and include placeholders using `<like_this>`.
- Saved files are created alongside `story.txt` and named like `madlibs_YYYYMMDD_HHMMSS.txt`.

## 💡 Troubleshooting

- If colors don't render nicely, it's likely your environment doesn't have `colorama`. Installing it with `pip install colorama` usually fixes the issue.
- If you get `FileNotFoundError`, ensure `story.txt` is present in the same folder as `App.py`.

## ❤️ Contributing

Feel free to open issues or fork the repo. Small ideas:

- Add a GUI with Tkinter or a web front-end.
- Let users choose between multiple story templates.

## 📄 License

This project is free to use and adapt. Have fun and make silly stories! 😄

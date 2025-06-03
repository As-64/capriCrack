# 🔐 pyCrack – Simple Python Hash Cracker

**pyCrack** is a lightweight, GUI-based hash cracking tool written in Python. Designed for cybersecurity learners, CTF participants, and ethical hackers, this tool can crack common hash types using wordlists via a simple and intuitive interface.

---

## 🎯 Features

- ✅ Supports **MD5**, **SHA-1**, and **SHA-256**
- ✅ Automatic hash type detection (based on hash length)
- ✅ GUI-based file selection using EasyGUI
- ✅ Wordlist-driven brute-force cracking
- ✅ Easy-to-extend — add more wordlists to enhance performance

---

## 🛠️ Requirements

- Python 3.x
- [EasyGUI](https://pypi.org/project/easygui/)

Install EasyGUI via pip:
```bash
pip install easygui

🚀 How to Use
1. Clone this repository:

git clone https://github.com/your-username/pyCrack.git
cd pyCrack

2. Make sure you have a wordlists/ directory with at least one .txt wordlist inside. You can add more files to this folder.

3. Run the program:

python pyCrack.py

4. Use the GUI to:

Choose a target hash file or input it manually

Select a wordlist from the wordlists folder

Choose a hash type or let the tool identify it

📁 Wordlists
Default wordlists go in the /wordlists/ directory.
Feel free to add your own — common ones include:

rockyou.txt

top1000.txt

custom.txt

Each line should contain a single candidate password.

🧠 Planned Features
Hash type identifier module

Multi-threaded cracking for speed

Support for SHA-512, bcrypt, and salted hashes

Web version (Flask GUI)

Built-in wordlist downloads

📜 License
This project is licensed under the MIT License.

❤️ Contribute
Want to contribute? Spot an issue? Suggest a feature?
Open a pull request or drop an issue — all contributions welcome!

⚡ Created as part of our initiative — empowering young cybersecurity builders.


# Admin Panel Finder | Team CDF

![Banner](https://img.shields.io/badge/Team-CDF-green) ![Python](https://img.shields.io/badge/Python-3.x-blue) ![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🔎 Overview

**Admin Panel Finder** is a simple and effective Python tool designed to help security researchers, pentesters, and web admins find hidden or unprotected admin login pages on websites. It works by scanning a target URL with a customizable wordlist of common admin panel paths.

The tool supports multithreading for faster scanning and detects potential SQL injection error messages to highlight vulnerable pages.

---

## ⚙️ Features

- Multithreaded scanning for fast performance
- Detects common admin panel paths from a customizable wordlist
- Checks HTTP status codes and page content for "login" keyword
- Flags SQL injection error messages in responses
- Simple command-line interface with interactive input
- Lightweight and easy to use

---

## 📋 Requirements

- Python 3.x
- `requests` library

Install dependencies with:

```bash
cd CDF-ADMIN-FINDER
pip install request
python3 v7-1.py

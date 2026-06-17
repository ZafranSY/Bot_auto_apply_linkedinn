# LinkedIn Auto Job Applier

A web scraping bot that automates LinkedIn job applications. Searches relevant jobs, fills application forms, customizes your resume based on job descriptions, and applies automatically. Capable of 100+ applications per hour.

Built and maintained by **Zafran Bin Muhamad Sakowi**.

---

## Quick Start

1. **Install Python 3.10+** and required packages:
   ```
   pip install undetected-chromedriver pyautogui setuptools openai flask-cors flask
   ```
2. **Install Google Chrome** (latest version).
3. **Clone this repo** or download as ZIP.
4. **Configure your details** in `config/personals.py` and `config/questions.py`.
5. **Run the bot:**
   ```
   python runAiBot.py
   ```
6. **(Optional)** View application history:
   ```
   python app.py
   ```
   Then open `http://localhost:5000`.

---

## Configuration

| File | What to Configure |
|------|------------------|
| `config/personals.py` | Your name, phone, address, location |
| `config/questions.py` | Resume path, salary, notice period, LinkedIn, portfolio answers |
| `config/search.py` | Search terms, location filters, job preferences |
| `config/secrets.py` | LinkedIn login, AI provider credentials |
| `config/settings.py` | Click timing, stealth mode, background mode |

---

## Features

- Automated Easy Apply job applications
- AI-powered question answering (OpenAI, DeepSeek, Gemini)
- Resume customization per job description
- Smart skip logic for irrelevant jobs
- Multi-chrome profile support
- Background/stealth mode
- Application history dashboard

---

## About Me

**Zafran Bin Muhamad Sakowi**  
Final-year Computer Science (Software Engineering) student at Universiti Teknologi Malaysia (GPA 3.79/4.00)

- **Portfolio:** [zafran-sakowi.my](https://zafran-sakowi.my)
- **LinkedIn:** [linkedin.com/in/zafran-sakowi](https://www.linkedin.com/in/zafran-sakowi/)
- **Email:** zafransakowi@gmail.com

---

## Disclaimer

This program is for educational purposes only. Use at your own risk. Adhere to LinkedIn's terms of service regarding web scraping.

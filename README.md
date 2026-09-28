# password-strength-checker-SOP-python

A small Flask web app that rates the strength of a password and suggests how to improve it.

Enter a password in the form, submit it, and the page shows a strength rating plus a list of the criteria the password does not yet meet.

## How strength is judged

`check_password_strength()` in `app.py` checks five criteria:

| Criterion | Rule |
|-----------|------|
| Length | at least 8 characters |
| Uppercase | at least one letter `A-Z` |
| Lowercase | at least one letter `a-z` |
| Number | at least one digit `0-9` |
| Special character | at least one of `!@#$%^&*()` |

The rating depends on how many criteria are met:

| Criteria met | Rating |
|--------------|--------|
| 5 | Very Strong |
| 4 | Strong |
| 3 | Medium |
| 2 | Weak |
| 0-1 | Very Weak |

For every criterion that is not met, the app adds a suggestion (for example, "Password should include at least one number.").

Only the characters `!@#$%^&*()` count as special characters; other symbols such as `-`, `_` or `?` do not.

## Requirements

- Python 3
- Flask

## Setup

```bash
git clone https://github.com/pranjulya/password-strength-checker-SOP-python.git
cd password-strength-checker-SOP-python
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install flask
```

## Run

```bash
python app.py
```

Then open http://127.0.0.1:5002 in your browser.

The app starts Flask's built-in development server with `debug=True`, so it is meant for local use only.

## Project structure

```
.
├── app.py               # Flask app: strength-checking logic and the "/" route (GET shows the form, POST shows the result)
└── templates/
    └── index.html       # Password form and result/suggestions display
```

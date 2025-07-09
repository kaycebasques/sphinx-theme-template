from pathlib import Path

def setup(app):
    app.add_html_theme('sphinx-theme-template', Path(__file__).resolve().parent)

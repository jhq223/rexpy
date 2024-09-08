from taipy import Gui
from app import pages
from config import DUBUG

Gui(pages=pages, css_file='main.css').run(debug=DUBUG, use_reloader=DUBUG)

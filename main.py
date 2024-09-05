from taipy import Gui
from app import pages

Gui(pages=pages).run(debug=True, use_reloader=True)

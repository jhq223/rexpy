from taipy import Gui
from app import pages

print("hsjak")
Gui(pages=pages).run(debug=True, use_reloader=True)

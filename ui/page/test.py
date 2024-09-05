from taipy.gui import Markdown, notify

value = 0

# Definition of the page
test_md = Markdown("""
# Getting started with Taipy GUI

count: <|{value}|>

<|+|button|on_action=on_button1_action|>
<|-|button|on_action=on_button2_action|>
""")


def on_button1_action(state):
    notify(state, "info", f"The text is: {state.value}")
    state.value += 1


def on_button2_action(state):
    notify(state, "info", f"The text is: {state.value}")
    state.value -= 1

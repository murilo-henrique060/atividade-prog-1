from flet import Ref
from flet import View, Column, Container, Text, TextField, ElevatedButton
from flet import TextAlign, padding, ButtonStyle, TextStyle
from flet import ControlEvent

def login(page):
  email_ref = Ref[TextField]()
  password_ref = Ref[TextField]()

  def login_handler(e: ControlEvent):
    email = email_ref.current.value
    password = password_ref.current.value

  return View(
    "login",
    [
      Container(
        Text("Welcome to my app!", **styles["title-text"]),
        **styles["title-container"]
      ),

      Container(
        Column([
          Container(
            Text("Email", **styles["input-label"]),
            **styles["input-label-container"]
          ),
          TextField(ref=email_ref, autofocus=True, **styles["input-field"])
        ]),
        **styles["input-container"]
      ),

      Container(
        Column([
          Container(
            Text("Password", **styles["input-label"]),
            **styles["input-label-container"]
          ),
          TextField(ref=password_ref, password=True, **styles["input-field"])
        ]),
        **styles["input-container"]
      ),

      ElevatedButton("Login", **styles["submit-button"], on_click=login_handler)
    ],
    **styles["view"]
  )

styles = {
  "view": {
    "horizontal_alignment": "center",
    "vertical_alignment": "center"
  },

  "title-text": {
    "size": 30,
    "text_align": TextAlign.CENTER
  },
  "title-container": {
    "padding": 25
  },


  "input-label": {
    "size": 16,
  },
  "input-label-container": {
    "padding": padding.only(left=5)
  },
  "input-field": {
    "border": "1px solid #ccc",
    "border_radius": 5
  },
  "input-container": {
    "width": 700,
    "padding": padding.only(bottom=10)
  },


  "submit-button": {
    "width": 300,
    "style": ButtonStyle(
      padding=padding.symmetric(vertical=15),
      text_style=TextStyle(
        size=18
      ),
    )
  }
}
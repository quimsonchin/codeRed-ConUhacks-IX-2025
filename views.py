<<<<<<< Updated upstream
print("hello")
=======
from flask import Blueprint

views = Blueprint("views")

@views.route('/')
def home():
    return "home page"
>>>>>>> Stashed changes

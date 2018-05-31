from flask import render_template, Blueprint, request, flash

main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/')
def landing():
    return render_template('main/landing.html')

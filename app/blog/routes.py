from flask import Blueprint

blog_bp = Blueprint('blog', __name__, template_folder='templates')

@blog_bp.route('/entrada/<int:id>')
def entrada(id):
    return f"Mostrando el título de la entrada con ID: {id}"
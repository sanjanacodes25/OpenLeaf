from flask import render_template, request, Blueprint
from main.models import Post

mmain = Blueprint('mmain', __name__)


@mmain.route("/")
@mmain.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@mmain.route("/about")
def about():
    return render_template('about.html')

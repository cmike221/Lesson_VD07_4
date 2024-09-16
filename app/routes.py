from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import EditProfileForm
# from . import create_app

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('edit_profile.html')


@main.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        # Здесь можно добавить код для сохранения изменений профиля
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('edit_profile'))
    return render_template('edit_profile.html', form=form)

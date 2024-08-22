from flask import Blueprint, redirect, render_template, request
from app.forms.forms import ImageForm
from app.models import db, Image
from flask_login import current_user, login_required
from app.api.aws_utils import (
    upload_file_to_s3, get_unique_filename)

image_routes = Blueprint("images", __name__)


@image_routes.route("/new", methods=["GET", "POST"])
# @login_required
def upload_image():
    form = ImageForm()

    if form.validate_on_submit():

        image = form.data["image"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)
        print(upload)

        if "url" not in upload:
        # if the dictionary doesn't have a url key
        # it means that there was an error when you tried to upload
        # so you send back that error message (and you printed it above)
            return {'error': 'error'}

        url = upload["url"]
        new_image = Image(image= url)
        db.session.add(new_image)
        db.session.commit()
        return {"image": new_image.to_dict()}, 201

    if form.errors:
        print(form.errors)
        return {}

    return {'message': 'hello'}

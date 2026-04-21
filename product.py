# product.py

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from database import db
from models import Product

product = Blueprint("product", __name__)


# ==================================================
# VIEW ALL PRODUCTS
# ==================================================
@product.route("/products")
def products():

    all_products = Product.query.order_by(Product.id.desc()).all()

    return render_template(
        "products.html",
        products=all_products
    )


# ==================================================
# ADD PRODUCT
# ==================================================
@product.route("/add-product", methods=["GET", "POST"])
def add_product():

    if "user_id" not in session:
        flash("Please login first.")
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        name = request.form.get("name")
        category = request.form.get("category")
        price_str = request.form.get("price")
        description = request.form.get("description")

        if not name or not price_str:
            flash("Name and price are required.")
            return redirect(url_for("product.add_product"))

        try:
            price = float(price_str)
        except ValueError:
            flash("Invalid price format.")
            return redirect(url_for("product.add_product"))

        new_product = Product(
            user_id=session["user_id"],
            name=name,
            category=category,
            price=price,
            description=description
        )

        db.session.add(new_product)
        db.session.commit()

        flash("Product added successfully.")
        return redirect(url_for("product.my_products"))

    return render_template("add-product.html")


# ==================================================
# MY PRODUCTS
# ==================================================
@product.route("/my-products")
def my_products():

    if "user_id" not in session:
        flash("Please login first.")
        return redirect(url_for("auth.login"))

    user_products = Product.query.filter_by(
        user_id=session["user_id"]
    ).order_by(Product.id.desc()).all()

    return render_template(
        "my-products.html",
        products=user_products
    )


# ==================================================
# EDIT PRODUCT
# ==================================================
@product.route("/edit-product/<int:id>", methods=["GET", "POST"])
def edit_product(id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    product_data = Product.query.get_or_404(id)

    if product_data.user_id != session["user_id"]:
        flash("Unauthorized access.")
        return redirect(url_for("product.my_products"))

    if request.method == "POST":

        name = request.form.get("name")
        category = request.form.get("category")
        price_str = request.form.get("price")
        description = request.form.get("description")

        if not name or not price_str:
            flash("Name and price are required.")
            return redirect(url_for("product.edit_product", id=id))

        try:
            price = float(price_str)
        except ValueError:
            flash("Invalid price format.")
            return redirect(url_for("product.edit_product", id=id))

        product_data.name = name
        product_data.category = category
        product_data.price = price
        product_data.description = description

        db.session.commit()

        flash("Product updated successfully.")
        return redirect(url_for("product.my_products"))

    return render_template(
        "edit-product.html",
        product=product_data
    )


# ==================================================
# DELETE PRODUCT
# ==================================================
@product.route("/delete-product/<int:id>")
def delete_product(id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    product_data = Product.query.get_or_404(id)

    if product_data.user_id != session["user_id"]:
        flash("Unauthorized access.")
        return redirect(url_for("product.my_products"))

    db.session.delete(product_data)
    db.session.commit()

    flash("Product deleted successfully.")
    return redirect(url_for("product.my_products"))


# ==================================================
# PRODUCT DETAILS
# ==================================================
@product.route("/product/<int:id>")
def product_details(id):

    product_data = Product.query.get_or_404(id)

    return render_template(
        "product-details.html",
        product=product_data
    )
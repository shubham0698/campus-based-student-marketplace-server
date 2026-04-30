# product.py

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from database import db
from models import Product, User, Wishlist, Order
from recommendations import get_recommendations, get_nearest_products, get_trending_products

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

    return render_template("add_product.html")


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
        "my_products.html",
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
    
    # Increment view count for recommendations
    product_data.view_count += 1
    db.session.commit()

    return render_template(
        "product-details.html",
        product=product_data
    )


# ==================================================
# SEARCH PRODUCTS
# ==================================================
@product.route("/search")
def search():
    """
    Search products by keyword in name and description.
    """
    query = request.args.get("q", "").strip()
    
    if not query:
        flash("Please enter a search term.")
        return redirect(url_for("product.products"))
    
    # Search in product name and description
    search_results = Product.query.filter(
        (Product.name.ilike(f"%{query}%") | 
         Product.description.ilike(f"%{query}%")) &
        (Product.status == "available")
    ).order_by(Product.created_at.desc()).all()
    
    return render_template(
        "search-results.html",
        products=search_results,
        query=query,
        result_count=len(search_results)
    )


# ==================================================
# FILTER BY CATEGORY
# ==================================================
@product.route("/category/<category>")
def filter_by_category(category):
    """
    Filter products by category.
    """
    # Sanitize category
    category = category.strip().lower()
    
    products_by_category = Product.query.filter(
        Product.category.ilike(f"%{category}%"),
        Product.status == "available"
    ).order_by(Product.created_at.desc()).all()
    
    return render_template(
        "category-products.html",
        products=products_by_category,
        category=category.title(),
        result_count=len(products_by_category)
    )


# ==================================================
# GET ALL CATEGORIES
# ==================================================
@product.route("/categories")
def categories():
    """
    Get all available categories.
    """
    categories = db.session.query(Product.category).filter(
        Product.status == "available",
        Product.category != None
    ).distinct().all()
    
    category_list = [cat[0] for cat in categories if cat[0]]
    
    return render_template(
        "categories.html",
        categories=category_list
    )


# ==================================================
# LOCATION-BASED SEARCH
# ==================================================
@product.route("/nearest")
def nearest_products():
    """
    Get products nearest to the user's location.
    Requires user to be logged in with location set.
    """
    if "user_id" not in session:
        flash("Please login to use location-based search.")
        return redirect(url_for("auth.login"))
    
    max_distance = request.args.get("distance", 50, type=int)
    limit = request.args.get("limit", 12, type=int)
    
    nearest = get_nearest_products(session["user_id"], max_distance, limit)
    
    user = User.query.get(session["user_id"])
    
    return render_template(
        "nearest-products.html",
        products=nearest,
        user_location=user.location_name if user else "Campus",
        max_distance=max_distance,
        result_count=len(nearest)
    )


# ==================================================
# PERSONALIZED RECOMMENDATIONS
# ==================================================
@product.route("/recommendations")
def recommendations():
    """
    Get personalized product recommendations using collaborative filtering.
    Requires user to be logged in.
    """
    if "user_id" not in session:
        flash("Please login to see recommendations.")
        return redirect(url_for("auth.login"))
    
    num_recommendations = request.args.get("limit", 10, type=int)
    
    recommended_products = get_recommendations(session["user_id"], num_recommendations)
    
    return render_template(
        "recommendations.html",
        products=recommended_products,
        result_count=len(recommended_products)
    )


# ==================================================
# TRENDING PRODUCTS
# ==================================================
@product.route("/trending")
def trending():
    """
    Get trending products based on popularity score.
    """
    limit = request.args.get("limit", 12, type=int)
    
    trending_products = get_trending_products(limit)
    
    return render_template(
        "trending-products.html",
        products=trending_products,
        result_count=len(trending_products)
    )
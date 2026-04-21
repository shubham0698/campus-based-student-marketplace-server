# dashboard.py

from flask import Blueprint, render_template, session, redirect, url_for, flash
from sqlalchemy import func

from models import User, Product, Order, Wishlist, Message

dashboard = Blueprint("dashboard", __name__)


# ==================================================
# MAIN DASHBOARD
# ==================================================
@dashboard.route("/dashboard")
def dashboard_home():

    if "user_id" not in session:
        flash("Please login first.")
        return redirect(url_for("auth.login"))

    user_id = session["user_id"]

    total_products = Product.query.filter_by(user_id=user_id).count()

    available_products = Product.query.filter_by(
        user_id=user_id,
        status="available"
    ).count()

    sold_products = Product.query.filter_by(
        user_id=user_id,
        status="sold"
    ).count()

    wishlist_count = Wishlist.query.filter_by(
        user_id=user_id
    ).count()

    orders_count = Order.query.filter_by(
        buyer_id=user_id
    ).count()

    messages_count = Message.query.filter(
        Message.receiver_id == user_id
    ).count()

    recent_products = Product.query.filter_by(
        user_id=user_id
    ).order_by(Product.id.desc()).limit(5).all()

    return render_template(
        "dashboard.html",
        total_products=total_products,
        available_products=available_products,
        sold_products=sold_products,
        wishlist_count=wishlist_count,
        orders_count=orders_count,
        messages_count=messages_count,
        recent_products=recent_products
    )


# ==================================================
# PROFILE PAGE
# ==================================================
@dashboard.route("/profile")
def profile():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    user = User.query.get(session["user_id"])

    return render_template(
        "profile.html",
        user=user
    )


# ==================================================
# WISHLIST PAGE
# ==================================================
@dashboard.route("/wishlist")
def wishlist():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    wishlist_items = Wishlist.query.filter_by(
        user_id=session["user_id"]
    ).all()

    return render_template(
        "wishlist.html",
        wishlist_items=wishlist_items
    )


# ==================================================
# ORDERS PAGE
# ==================================================
@dashboard.route("/orders")
def orders():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    orders = Order.query.filter_by(
        buyer_id=session["user_id"]
    ).order_by(Order.id.desc()).all()

    return render_template(
        "orders.html",
        orders=orders
    )


# ==================================================
# MESSAGES PAGE
# ==================================================
@dashboard.route("/messages")
def messages():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    inbox = Message.query.filter(
        Message.receiver_id == session["user_id"]
    ).order_by(Message.id.desc()).all()

    return render_template(
        "messages.html",
        inbox=inbox
    )
# database.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ==================================================
# INITIALIZE DATABASE
# ==================================================
def init_db(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()


# ==================================================
# DELETE
# ==================================================
def delete_record(data):
    db.session.delete(data)
    db.session.commit()


# ==================================================
# SELECT
# ==================================================
def get_all(model):
    return model.query.all()


def get_by_id(model, record_id):
    return model.query.get(record_id)


def get_first(model, **filters):
    return model.query.filter_by(**filters).first()


def get_filter(model, **filters):
    return model.query.filter_by(**filters).all()


# ==================================================
# COUNT
# ==================================================
def count_records(model):
    return model.query.count()


# ==================================================
# SEARCH
# ==================================================
def search(model, column, keyword):
    return model.query.filter(
        column.ilike(f"%{keyword}%")
    ).all()


# ==================================================
# PAGINATION
# ==================================================
def paginate(model, page=1, per_page=10):
    return model.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )


# ==================================================
# CLOSE DB
# ==================================================
def close_db():
    db.session.remove()
# database.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

# ==================================================
# INITIALIZE DATABASE
# ==================================================
def init_db(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()
        _ensure_sqlite_columns()


def _ensure_sqlite_columns():
    """Ensure SQLite tables have required columns after model updates."""
    if db.engine.url.drivername != "sqlite":
        return

    required_columns = {
        "products": {
            "view_count": "INTEGER DEFAULT 0"
        },
        "users": {
            "location_name": "VARCHAR(200) DEFAULT 'Campus'",
            "latitude": "FLOAT DEFAULT 0.0",
            "longitude": "FLOAT DEFAULT 0.0"
        }
    }

    with db.engine.connect() as connection:
        for table_name, columns in required_columns.items():
            result = connection.execute(
                text(f"PRAGMA table_info('{table_name}')")
            )
            existing_columns = [row[1] for row in result.fetchall()]

            for column_name, definition in columns.items():
                if column_name not in existing_columns:
                    connection.execute(
                        text(
                            f"ALTER TABLE {table_name} ADD COLUMN {column_name} {definition}"
                        )
                    )


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
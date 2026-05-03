from pathlib import Path

pages = {
    r"d:\sem project\templates\login.html": '''{% extends 'base.html' %}

{% block title %}Login - CampusMart{% endblock %}

{% block search_bar %}{% endblock %}

{% block content %}
<section class="section" style="padding-top: 80px; padding-bottom: 80px;">
    <div class="container">
        <div class="form-card" style="max-width: 460px; margin: 0 auto;">
            <div class="section-title" style="margin-bottom: 12px;">Sign in to CampusMart</div>
            <p class="section-subtitle" style="margin-bottom: 30px;">Access your listings, messages, and orders with your student account.</p>

            <form action="{{ url_for('auth.login') }}" method="POST" class="form-row">
                <div class="form-group">
                    <label for="email">Email Address</label>
                    <input id="email" type="email" name="email" placeholder="Enter your email" required>
                </div>

                <div class="form-group">
                    <label for="password">Password</label>
                    <input id="password" type="password" name="password" placeholder="Enter your password" required>
                </div>

                <button type="submit" class="btn">Sign In</button>
            </form>

            <div style="margin-top: 20px; text-align: center; color: #6b7280;">
                <p>New to CampusMart? <a href="{{ url_for('auth.register') }}">Create an account</a></p>
            </div>
        </div>
    </div>
</section>
{% endblock %}
''',
    r"d:\sem project\templates\register.html": '''{% extends 'base.html' %}

{% block title %}Register - CampusMart{% endblock %}

{% block search_bar %}{% endblock %}

{% block content %}
<section class="section" style="padding-top: 80px; padding-bottom: 80px;">
    <div class="container">
        <div class="form-card" style="max-width: 560px; margin: 0 auto;">
            <div class="section-title" style="margin-bottom: 12px;">Create Your Account</div>
            <p class="section-subtitle" style="margin-bottom: 30px;">Join the campus marketplace and start buying or selling items today.</p>

            <form action="{{ url_for('auth.register') }}" method="POST" class="form-row">
                <div class="form-group">
                    <label for="name">Full Name</label>
                    <input id="name" type="text" name="name" placeholder="Enter full name" required>
                </div>

                <div class="form-group">
                    <label for="email">Email Address</label>
                    <input id="email" type="email" name="email" placeholder="Enter college email" required>
                </div>

                <div class="form-group">
                    <label for="phone">Phone Number</label>
                    <input id="phone" type="tel" name="phone" placeholder="Enter mobile number" required>
                </div>

                <div class="form-group">
                    <label for="college">College</label>
                    <input id="college" type="text" name="college" placeholder="Enter college name" required>
                </div>

                <div class="form-group">
                    <label for="department">Department</label>
                    <input id="department" type="text" name="department" placeholder="Enter department" required>
                </div>

                <div class="form-group">
                    <label for="password">Password</label>
                    <input id="password" type="password" name="password" placeholder="Enter a secure password" required>
                </div>

                <button type="submit" class="btn">Create Account</button>
            </form>

            <div style="margin-top: 20px; text-align: center; color: #6b7280;">
                <p>Already have an account? <a href="{{ url_for('auth.login') }}">Sign in</a></p>
            </div>
        </div>
    </div>
</section>
{% endblock %}
''',
    r"d:\sem project\templates\add_product.html": '''{% extends 'base.html' %}

{% block title %}Add Product - CampusMart{% endblock %}

{% block search_bar %}{% endblock %}

{% block content %}
<section class="section">
    <div class="container">
        <div class="form-card" style="max-width: 760px; margin: 0 auto;">
            <div class="section-title" style="margin-bottom: 8px;">Add New Product</div>
            <p class="section-subtitle" style="margin-bottom: 24px;">List your item for sale so other students can discover it quickly.</p>

            <form action="{{ url_for('product.add_product') }}" method="POST" class="form-row">
                <div class="form-group">
                    <label for="name">Product Name</label>
                    <input id="name" type="text" name="name" placeholder="Enter product name" required>
                </div>

                <div class="form-group">
                    <label for="category">Category</label>
                    <select id="category" name="category" required>
                        <option value="">Select Category</option>
                        <option>Books</option>
                        <option>Electronics</option>
                        <option>Notes</option>
                        <option>Bicycle</option>
                        <option>Furniture</option>
                        <option>Accessories</option>
                        <option>Study Materials</option>
                        <option>Other</option>
                    </select>
                </div>

                <div class="form-group">
                    <label for="price">Price (₹)</label>
                    <input id="price" type="number" name="price" min="0" step="0.01" placeholder="Enter price" required>
                </div>

                <div class="form-group">
                    <label for="image_url">Image URL</label>
                    <input id="image_url" type="url" name="image_url" placeholder="Paste a valid image URL (optional)">
                </div>

                <div class="form-group" style="grid-column: 1 / -1;">
                    <label for="description">Description</label>
                    <textarea id="description" name="description" placeholder="Describe the item, condition, and any important details"></textarea>
                </div>

                <button type="submit" class="btn" style="width: 100%;">Publish Product</button>
            </form>
        </div>
    </div>
</section>
{% endblock %}
''',
    r"d:\sem project\templates\edit-product.html": '''{% extends 'base.html' %}

{% block title %}Edit Product - CampusMart{% endblock %}

{% block search_bar %}{% endblock %}

{% block content %}
<section class="section">
    <div class="container">
        <div class="form-card" style="max-width: 760px; margin: 0 auto;">
            <div class="section-title" style="margin-bottom: 8px;">Edit Product</div>
            <p class="section-subtitle" style="margin-bottom: 24px;">Update the listing details and image for your product.</p>

            <form action="{{ url_for('product.edit_product', id=product.id) }}" method="POST" class="form-row">
                <div class="form-group">
                    <label for="name">Product Name</label>
                    <input id="name" type="text" name="name" value="{{ product.name }}" placeholder="Enter product name" required>
                </div>

                <div class="form-group">
                    <label for="category">Category</label>
                    <select id="category" name="category" required>
                        <option value="{{ product.category }}" selected>{{ product.category }}</option>
                        <option>Books</option>
                        <option>Electronics</option>
                        <option>Notes</option>
                        <option>Bicycle</option>
                        <option>Furniture</option>
                        <option>Accessories</option>
                        <option>Study Materials</option>
                        <option>Other</option>
                    </select>
                </div>

                <div class="form-group">
                    <label for="price">Price (₹)</label>
                    <input id="price" type="number" name="price" step="0.01" value="{{ product.price }}" placeholder="Enter price" required>
                </div>

                <div class="form-group">
                    <label for="image_url">Image URL</label>
                    <input id="image_url" type="url" name="image_url" value="{{ product.image or '' }}" placeholder="Paste a valid image URL to update">
                </div>

                <div class="form-group" style="grid-column: 1 / -1;">
                    <label for="description">Description</label>
                    <textarea id="description" name="description" placeholder="Enter product details">{{ product.description }}</textarea>
                </div>

                <button type="submit" class="btn" style="width: 100%;">Save Changes</button>
            </form>
        </div>
    </div>
</section>
{% endblock %}
''',
    r"d:\sem project\templates\product-details.html": '''{% extends 'base.html' %}

{% block title %}{{ product.name }} - CampusMart{% endblock %}

{% block search_bar %}{% endblock %}

{% block content %}
<section class="section">
    <div class="container">
        <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 32px; align-items: start;">
            <div class="card card-image" style="min-height: 420px;">
                {% if product.image %}
                <img src="{{ product.image }}" alt="{{ product.name }}">
                {% else %}
                <div style="display:grid; place-items:center; height:100%; color:#6b7280;">
                    <i class="fas fa-image" style="font-size: 48px;"></i>
                    <p style="margin-top: 12px;">No Image Available</p>
                </div>
                {% endif %}
            </div>

            <div>
                <div class="card-body">
                    <h1 class="card-title">{{ product.name }}</h1>
                    <div class="card-meta" style="margin-bottom: 20px; gap: 16px;">
                        <span class="badge">{{ product.category or 'General' }}</span>
                        <span class="badge" style="background: #d1fae5; color: #166534;">{{ product.status.title() }}</span>
                    </div>
                    <div class="price">₹{{ '%.2f' | format(product.price) }}</div>
                    <p class="card-text" style="margin-bottom: 24px;">{{ product.description or 'No description provided for this product.' }}</p>

                    <div class="card-meta" style="display: grid; gap: 10px; margin-bottom: 28px;">
                        <span class="text-muted"><strong>Seller:</strong> {{ product.owner.name }}</span>
                        <span class="text-muted"><strong>Contact:</strong> {{ product.owner.email }}</span>
                    </div>

                    {% if session.get('user_id') and session.get('user_id') != product.user_id %}
                    <div style="display: flex; flex-wrap: wrap; gap: 12px;">
                        <a href="#" class="btn">Add to Wishlist</a>
                        <a href="mailto:{{ product.owner.email }}" class="btn btn-secondary">Contact Seller</a>
                    </div>
                    {% endif %}

                    <div style="margin-top: 24px;">
                        <a href="{{ url_for('product.products') }}" class="btn btn-outline">Back to Products</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
{% endblock %}
''',
    r"d:\sem project\templates\dashboard.html": '''{% extends 'base.html' %}

{% block title %}Dashboard - CampusMart{% endblock %}

{% block content %}
<section class="section" style="padding-top: 40px; padding-bottom: 40px;">
    <div class="container">
        <div style="display: flex; flex-wrap: wrap; gap: 24px; justify-content: space-between; align-items: center; margin-bottom: 28px;">
            <div>
                <div class="section-title" style="margin-bottom: 8px;">Your Dashboard</div>
                <p class="section-subtitle">Track your active listings, orders, wishlist and recent product activity in one place.</p>
            </div>
            <a href="{{ url_for('product.add_product') }}" class="btn">Add Product</a>
        </div>

        <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));">
            <div class="card">
                <div class="card-body">
                    <h3 class="card-title">Total Listings</h3>
                    <p class="price">{{ total_products }}</p>
                    <p class="text-muted">Products you have listed on CampusMart.</p>
                </div>
            </div>
            <div class="card">
                <div class="card-body">
                    <h3 class="card-title">Available</h3>
                    <p class="price">{{ available_products }}</p>
                    <p class="text-muted">Items currently marked as available.</p>
                </div>
            </div>
            <div class="card">
                <div class="card-body">
                    <h3 class="card-title">Sold</h3>
                    <p class="price">{{ sold_products }}</p>
                    <p class="text-muted">Products already sold.</p>
                </div>
            </div>
            <div class="card">
                <div class="card-body">
                    <h3 class="card-title">Wishlist</h3>
                    <p class="price">{{ wishlist_count }}</p>
                    <p class="text-muted">Items saved for later.</p>
                </div>
            </div>
            <div class="card">
                <div class="card-body">
                    <h3 class="card-title">Orders</h3>
                    <p class="price">{{ orders_count }}</p>
                    <p class="text-muted">Recent purchases in your account.</p>
                </div>
            </div>
            <div class="card">
                <div class="card-body">
                    <h3 class="card-title">Messages</h3>
                    <p class="price">{{ messages_count }}</p>
                    <p class="text-muted">New conversations with buyers or sellers.</p>
                </div>
            </div>
        </div>

        <div class="section" style="padding-top: 36px; padding-bottom: 0;">
            <div class="section-title" style="font-size: 28px; margin-bottom: 16px;">Recent Listings</div>
            {% if recent_products %}
            <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));">
                {% for product in recent_products %}
                <div class="card">
                    <div class="card-image">
                        {% if product.image %}
                        <img src="{{ product.image }}" alt="{{ product.name }}">
                        {% else %}
                        <div style="display:grid; place-items:center; height:100%; color:#6b7280;"><i class="fas fa-box-open" style="font-size: 40px;"></i></div>
                        {% endif %}
                    </div>
                    <div class="card-body">
                        <h4 class="card-title">{{ product.name }}</h4>
                        <p class="card-text">{{ product.description[:95] ~ ('...' if product.description|length > 95 else '') }}</p>
                        <div style="display:flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap;">
                            <span class="badge">{{ product.category or 'General' }}</span>
                            <span class="price">₹{{ '%.2f' | format(product.price) }}</span>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
            {% else %}
            <div class="empty-state">
                <h3>No recent products yet</h3>
                <p>You don’t have any recent listings. Add a product to start selling on CampusMart.</p>
            </div>
            {% endif %}
        </div>
    </div>
</section>
{% endblock %}
''',
    r"d:\sem project\templates\my_products.html": '''{% extends 'base.html' %}

{% block title %}My Products - CampusMart{% endblock %}

{% block content %}
<section class="section">
    <div class="container">
        <div style="display: flex; flex-wrap: wrap; gap: 18px; justify-content: space-between; align-items: center; margin-bottom: 24px;">
            <div>
                <div class="section-title" style="margin-bottom: 8px;">My Products</div>
                <p class="section-subtitle">Manage your active listings and update product details from here.</p>
            </div>
            <a href="{{ url_for('product.add_product') }}" class="btn">Add New Product</a>
        </div>

        {% if products %}
        <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));">
            {% for product in products %}
            <div class="card">
                <div class="card-image">
                    {% if product.image %}
                    <img src="{{ product.image }}" alt="{{ product.name }}">
                    {% else %}
                    <div style="display:grid; place-items:center; height:100%; color:#6b7280;"><i class="fas fa-box" style="font-size: 36px;"></i></div>
                    {% endif %}
                </div>
                <div class="card-body">
                    <h3 class="card-title">{{ product.name }}</h3>
                    <div class="card-meta" style="gap: 12px; margin-bottom: 14px;">
                        <span class="badge">{{ product.category or 'General' }}</span>
                        <span class="badge" style="background: {{ 'rgba(16,185,129,0.12)' if product.status == 'available' else 'rgba(239,68,68,0.12)' }}; color: {{ '#166534' if product.status == 'available' else '#991b1b' }};">{{ product.status.title() }}</span>
                    </div>
                    <p class="card-text">₹{{ '%.2f' | format(product.price) }}</p>
                    <div style="display:flex; gap: 10px; flex-wrap: wrap; margin-top: 18px;">
                        <a href="{{ url_for('product.edit_product', id=product.id) }}" class="btn btn-secondary" style="flex:1;">Edit</a>
                        <a href="{{ url_for('product.delete_product', id=product.id) }}" class="btn btn-outline" style="flex:1;">Delete</a>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
        {% else %}
        <div class="empty-state">
            <h3>No products listed yet</h3>
            <p>Start listing your items so other students can find them.</p>
            <a href="{{ url_for('product.add_product') }}" class="btn">Add Your First Product</a>
        </div>
        {% endif %}
    </div>
</section>
{% endblock %}
''',
    r"d:\sem project\templates\messages.html": '''{% extends 'base.html' %}

{% block title %}Messages - CampusMart{% endblock %}

{% block search_bar %}{% endblock %}

{% block content %}
<section class="section">
    <div class="container" style="max-width: 980px;">
        <div style="margin-bottom: 26px; display:flex; flex-wrap:wrap; justify-content:space-between; gap: 16px; align-items:center;">
            <div>
                <div class="section-title" style="margin-bottom: 8px;">Messages</div>
                <p class="section-subtitle">View recent conversations and reply directly to sellers or buyers.</p>
            </div>
        </div>

        {% if inbox %}
        <div class="grid" style="grid-template-columns: 1fr; gap: 18px;">
            {% for message in inbox %}
            <div class="card">
                <div class="card-body">
                    <div style="display:flex; justify-content:space-between; flex-wrap:wrap; gap: 12px; margin-bottom: 14px;">
                        <div>
                            <h3 class="card-title" style="font-size: 20px; margin-bottom: 6px;">From: {{ message.sender.name }}</h3>
                            <p class="text-muted">{{ message.created_at.strftime('%d %b %Y %H:%M') }}</p>
                        </div>
                        <a href="mailto:{{ message.sender.email }}" class="btn btn-secondary">Reply</a>
                    </div>
                    <p class="card-text">{{ message.message }}</p>
                </div>
            </div>
            {% endfor %}
        </div>
        {% else %}
        <div class="empty-state">
            <h3>No messages yet</h3>
            <p>Once someone contacts you about a product, messages will appear here.</p>
            <a href="{{ url_for('product.products') }}" class="btn">Browse Products</a>
        </div>
        {% endif %}
    </div>
</section>
{% endblock %}
''',
    r"d:\sem project\templates\orders.html": '''{% extends 'base.html' %}

{% block title %}Orders - CampusMart{% endblock %}

{% block search_bar %}{% endblock %}

{% block content %}
<section class="section">
    <div class="container" style="max-width: 980px;">
        <div style="margin-bottom: 26px; display:flex; flex-wrap:wrap; justify-content:space-between; gap: 16px; align-items:center;">
            <div>
                <div class="section-title" style="margin-bottom: 8px;">Orders</div>
                <p class="section-subtitle">Track your purchases and view details for each order.</p>
            </div>
        </div>

        {% if orders %}
        <div class="grid" style="grid-template-columns: 1fr; gap: 18px;">
            {% for order in orders %}
            <div class="card">
                <div class="card-body" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap: 18px;">
                    <div>
                        <h3 class="card-title" style="margin-bottom: 8px;">{{ order.product.name }}</h3>
                        <p class="text-muted">Ordered on {{ order.created_at.strftime('%d %b %Y') }}</p>
                        <p class="price" style="margin-top: 12px;">₹{{ '%.2f' | format(order.product.price) }}</p>
                    </div>
                    <div style="display:flex; gap: 10px; flex-wrap:wrap; align-items:center;">
                        <span class="badge" style="background: {{ 'rgba(56,189,248,0.12)' if order.status == 'completed' else 'rgba(250,204,21,0.12)' if order.status == 'pending' else 'rgba(239,68,68,0.12)' }}; color: {{ '#0369a1' if order.status == 'completed' else '#92400e' if order.status == 'pending' else '#991b1b' }};">{{ order.status.title() }}</span>
                        <a href="{{ url_for('product.product_details', id=order.product.id) }}" class="btn btn-outline">View Product</a>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
        {% else %}
        <div class="empty-state">
            <h3>No orders yet</h3>
            <p>Your order history will appear here once you make a purchase.</p>
            <a href="{{ url_for('product.products') }}" class="btn">Browse Products</a>
        </div>
        {% endif %}
    </div>
</section>
{% endblock %}
''',
    r"d:\sem project\templates\profile.html": '''{% extends 'base.html' %}

{% block title %}Profile - CampusMart{% endblock %}

{% block search_bar %}{% endblock %}

{% block content %}
<section class="section">
    <div class="container" style="max-width: 640px;">
        <div class="form-card">
            <div class="section-title" style="margin-bottom: 8px;">My Profile</div>
            <p class="section-subtitle" style="margin-bottom: 24px;">View and manage your account information.</p>

            <div class="form-row">
                <div class="form-group"><label>Name</label><input type="text" value="{{ user.name }}" readonly></div>
                <div class="form-group"><label>Email</label><input type="email" value="{{ user.email }}" readonly></div>
                <div class="form-group"><label>Phone</label><input type="text" value="{{ user.phone or 'Not provided' }}" readonly></div>
                <div class="form-group"><label>College</label><input type="text" value="{{ user.college or 'Not provided' }}" readonly></div>
                <div class="form-group"><label>Department</label><input type="text" value="{{ user.department or 'Not provided' }}" readonly></div>
                <div class="form-group" style="grid-column: 1 / -1;"><label>Member Since</label><input type="text" value="{{ user.created_at.strftime('%B %Y') }}" readonly></div>
            </div>

            <div style="margin-top: 20px; text-align: right;">
                <a href="{{ url_for('dashboard.dashboard_home') }}" class="btn btn-outline">Back to Dashboard</a>
            </div>
        </div>
    </div>
</section>
{% endblock %}
''',
    r"d:\sem project\templates\wishlist.html": '''{% extends 'base.html' %}

{% block title %}Wishlist - CampusMart{% endblock %}

{% block search_bar %}{% endblock %}

{% block content %}
<section class="section">
    <div class="container">
        <div style="margin-bottom: 24px; display:flex; flex-wrap:wrap; justify-content:space-between; gap: 16px; align-items:center;">
            <div>
                <div class="section-title" style="margin-bottom: 8px;">Wishlist</div>
                <p class="section-subtitle">See the products you've saved for later.</p>
            </div>
        </div>

        {% if wishlist_items %}
        <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));">
            {% for item in wishlist_items %}
            <div class="card">
                <div class="card-image">
                    {% if item.product.image %}
                    <img src="{{ item.product.image }}" alt="{{ item.product.name }}">
                    {% else %}
                    <div style="display:grid; place-items:center; height:100%; color:#6b7280;"><i class="fas fa-heart" style="font-size: 42px;"></i></div>
                    {% endif %}
                </div>
                <div class="card-body">
                    <h3 class="card-title">{{ item.product.name }}</h3>
                    <p class="card-text">{{ item.product.description[:110] ~ ('...' if item.product.description|length > 110 else '') }}</p>
                    <div style="display:flex; justify-content:space-between; align-items:center; gap:12px; flex-wrap:wrap; margin-bottom:16px;">
                        <span class="price">₹{{ '%.2f' | format(item.product.price) }}</span>
                        <span class="badge">{{ item.product.category or 'General' }}</span>
                    </div>
                    <div style="display:flex; gap: 10px; flex-wrap: wrap;">
                        <a href="{{ url_for('product.product_details', id=item.product.id) }}" class="btn btn-outline" style="flex:1;">View</a>
                        <a href="#" class="btn btn-secondary" style="flex:1;">Remove</a>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
        {% else %}
        <div class="empty-state">
            <h3>Your wishlist is empty</h3>
            <p>Browse products and add the ones you love to your wishlist.</p>
            <a href="{{ url_for('product.products') }}" class="btn">Browse Products</a>
        </div>
        {% endif %}
    </div>
</section>
{% endblock %}
''',
    r"d:\sem project\templates\404.html": '''{% extends 'base.html' %}

{% block title %}404 Not Found{% endblock %}

{% block search_bar %}{% endblock %}

{% block content %}
<section class="section">
    <div class="container" style="max-width: 700px; text-align: center;">
        <div class="card" style="padding: 60px 30px;">
            <h1 class="section-title">404</h1>
            <p class="section-subtitle">The page you are looking for does not exist or has been moved.</p>
            <a href="{{ url_for('home') }}" class="btn" style="margin-top: 24px;">Back to Home</a>
        </div>
    </div>
</section>
{% endblock %}
''',
    r"d:\sem project\templates\500.html": '''{% extends 'base.html' %}

{% block title %}Server Error{% endblock %}

{% block search_bar %}{% endblock %}

{% block content %}
<section class="section">
    <div class="container" style="max-width: 700px; text-align: center;">
        <div class="card" style="padding: 60px 30px;">
            <h1 class="section-title">500</h1>
            <p class="section-subtitle">Something went wrong on our side. Please try again later.</p>
            <a href="{{ url_for('home') }}" class="btn" style="margin-top: 24px;">Back to Home</a>
        </div>
    </div>
</section>
{% endblock %}
''',
    r"d:\sem project\templates\products.html": '''{% extends 'base.html' %}

{% block title %}Products - CampusMart{% endblock %}

{% block content %}
<section class="section">
    <div class="container">
        <div style="display: flex; flex-wrap: wrap; gap: 18px; justify-content: space-between; align-items: center; margin-bottom: 26px;">
            <div>
                <div class="section-title" style="margin-bottom: 8px;">Explore Products</div>
                <p class="section-subtitle">Browse the campus marketplace for books, electronics, furniture and more.</p>
            </div>
            {% if session.get('user_id') %}
            <a href="{{ url_for('product.add_product') }}" class="btn">List an Item</a>
            {% endif %}
        </div>

        {% if products %}
        <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));">
            {% for product in products %}
            <div class="card">
                <div class="card-image">
                    {% if product.image %}
                    <img src="{{ product.image }}" alt="{{ product.name }}">
                    {% else %}
                    <div style="display:grid; place-items:center; height:100%; color:#6b7280;"><i class="fas fa-box-open" style="font-size: 40px;"></i></div>
                    {% endif %}
                </div>
                <div class="card-body">
                    <h3 class="card-title">{{ product.name }}</h3>
                    <div class="card-meta" style="gap: 10px; margin-bottom: 12px;">
                        <span class="badge">{{ product.category or 'General' }}</span>
                        <span class="price">₹{{ '%.2f' | format(product.price) }}</span>
                    </div>
                    <p class="card-text">{{ product.description or 'No description available.' }}</p>
                    <a href="{{ url_for('product.product_details', id=product.id) }}" class="btn" style="margin-top: 16px;">View Details</a>
                </div>
            </div>
            {% endfor %}
        </div>
        {% else %}
        <div class="empty-state">
            <h3>No products found</h3>
            <p>Try searching again, or check back later for new campus listings.</p>
        </div>
        {% endif %}
    </div>
</section>
{% endblock %}
'''
}

for path, content in pages.items():
    Path(path).write_text(content, encoding='utf-8')
print(f'Written {len(pages)} templates')

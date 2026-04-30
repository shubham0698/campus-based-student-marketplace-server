# Campus Mart

A secure peer-to-peer campus marketplace built for students to buy, sell, and exchange products within their college community.

Campus Mart streamlines second-hand commerce on campus by giving students a trusted platform for listing items, discovering affordable products, and communicating directly with verified buyers and sellers.

---

## Overview

Traditional student buying and selling often happens through informal channels such as messaging groups or word-of-mouth, which creates issues like poor visibility, pricing confusion, and trust concerns.

Campus Mart addresses these problems through a centralized digital marketplace tailored for educational institutions.

Students can use the platform to trade:

- Academic books  
- Electronics  
- Furniture  
- Stationery  
- Fashion items  
- Hostel essentials  
- Accessories  

---

## Tech Stack

### Backend
- **Framework**: Flask 3.1.0
- **Database**: SQLAlchemy with SQLite
- **Authentication**: Werkzeug (password hashing)
- **Server**: Gunicorn 23.0.0

### Frontend
- **Templating**: Jinja2 3.1.4
- **Styling**: CSS
- **Format**: HTML

### Libraries
- Flask-SQLAlchemy 3.1.1
- python-dotenv 1.0.1

---

## Key Features

### User Management
- ✅ Student registration and login  
- ✅ Secure password authentication  
- ✅ User profile management  
- ✅ Session-based access control  
- ✅ User roles and permissions

### Marketplace
- ✅ Create product listings  
- ✅ Add pricing and descriptions  
- ✅ Manage listing availability (available/sold status)  
- ✅ Edit or remove products  
- ⏳ Upload product images (model ready, UI implementation pending)

### Discovery
- ✅ View all products  
- ✅ View latest listings (sorted by creation date)  
- ✅ Browse products by category (advanced category filtering)
- ✅ Search products by keyword  
- ✅ Location-based nearest product results (distance-based sorting)  
- ✅ Personalized recommendations using collaborative filtering  
- ✅ Trending products (popularity-based ranking)  

### Communication
- ✅ Direct messaging between buyer and seller  
- ✅ Message inbox with received messages  
- ✅ Message history tracking

### Orders & Interest Tracking
- ✅ Purchase request tracking  
- ✅ Order status management (pending/confirmed/completed/cancelled)
- ✅ Wishlist functionality  
- ✅ Listing status updates (available/sold/reserved)  

### Dashboard & Analytics
- ✅ User dashboard with statistics  
- ✅ Total products count  
- ✅ Available vs sold products tracking  
- ✅ Wishlist count  
- ✅ Orders count  
- ✅ Messages count  
- ✅ Recent products display  

### Security & Reliability
- ✅ Input validation  
- ✅ Structured database design  
- ✅ Secure backend architecture  
- ✅ Authorization checks on protected routes  
- ✅ SQL injection prevention via ORM  

---

## Database Schema

### Users Table
- `id` (Primary Key)
- `name` - Student name
- `email` - Unique email address
- `phone` - Contact number
- `college` - College/Institution name
- `department` - Academic department
- `password` - Hashed password
- `location_name` - Campus location (hostel/block/area) - **NEW for location-based search**
- `latitude` - GPS latitude coordinate - **NEW for distance calculation**
- `longitude` - GPS longitude coordinate - **NEW for distance calculation**
- `created_at` - Account creation timestamp

### Products Table
- `id` (Primary Key)
- `user_id` (Foreign Key) - Product seller
- `name` - Product name
- `category` - Product category
- `price` - Selling price
- `description` - Product details
- `image` - Image file path
- `status` - available/sold/reserved
- `view_count` - Product views counter - **NEW for trending/recommendations**
- `created_at` - Listing creation date

### Orders Table
- `id` (Primary Key)
- `buyer_id` (Foreign Key) - Buyer user ID
- `product_id` (Foreign Key) - Product reference
- `status` - pending/confirmed/completed/cancelled
- `created_at` - Order creation date

### Wishlist Table
- `id` (Primary Key)
- `user_id` (Foreign Key) - User who wishlisted
- `product_id` (Foreign Key) - Wishlisted product
- `created_at` - Wishlist creation date

### Messages Table
- `id` (Primary Key)
- `sender_id` (Foreign Key) - Message sender
- `receiver_id` (Foreign Key) - Message receiver
- `message` - Message content
- `created_at` - Message timestamp

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Steps

1. **Clone/Download the repository**
   ```bash
   cd d:\sem project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables** (create `.env` file)
   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here
   ```

5. **Run the application**
   ```bash
   python app.py
   ```
   Or with Gunicorn:
   ```bash
   gunicorn app:app
   ```

6. **Access the application**
   - Open browser and navigate to `http://localhost:5000`

---

## 🚀 Advanced Discovery Features

### 1. Keyword Search
**Route**: `/search?q=<keyword>`

Search for products across the marketplace using keywords in product names and descriptions.

**Features:**
- Real-time search functionality
- Searches in product name and description
- Results sorted by newest first
- Available products only
- Clean results display with product details

**Example:**
```
Search for "laptop" → Find all laptops on sale
Search for "engineering books" → Find all related books
```

---

### 2. Category Filtering
**Routes**: 
- `/categories` - Browse all available categories
- `/category/<category_name>` - View products in specific category

Organize products by category for easier browsing and discovery.

**Features:**
- View all product categories
- Filter products by category
- Category card UI with hover effects
- Result count display
- Responsive category browsing

**Available Categories:**
- Books
- Electronics
- Furniture
- Stationery
- Fashion
- Hostel Essentials
- Accessories
- And more (dynamic based on listings)

---

### 3. Location-Based Search (Nearest First)
**Route**: `/nearest?distance=<km>&limit=<count>`

Find products nearest to your campus location using Haversine distance calculation.

**Features:**
- Distance-based sorting using Haversine formula
- Customizable search radius (default: 50km)
- User location stored during registration
- Seller location display on each product
- Faster handover and lower travel effort

**Algorithm:**
1. Retrieve user's GPS coordinates
2. Calculate distance to each product seller
3. Filter by maximum distance
4. Sort by nearest first
5. Return limited results

**How to Use:**
1. Set your location during registration (hostel/block/campus area)
2. Enter GPS coordinates (optional but recommended for accuracy)
3. Visit `/nearest` to see products sorted by distance
4. Adjust distance radius to expand/narrow search

---

### 4. Personalized Recommendations
**Route**: `/recommendations?limit=<count>`

Get AI-powered product recommendations using collaborative filtering algorithm.

**Features:**
- Learns from user interactions (wishlist, purchases, views)
- Finds similar users based on interaction patterns
- Recommends products liked by similar users
- Excludes already viewed/purchased items
- Trending products as fallback

**Recommendation Algorithm:**
1. Build user-product interaction matrix
2. Find similar users using cosine similarity
3. Score products liked by similar users
4. Rank by aggregated similarity scores
5. Return top N recommendations

**Interaction Weights:**
- Wishlist interaction: +1 point
- Purchase order: +2 points  
- Product view: +0.1 point (normalized)

**Example:**
```
If User A and User B both liked "Engineering Books"
and User B also liked "Calculators"
→ Recommend "Calculators" to User A
```

---

### 5. Trending Products
**Route**: `/trending?limit=<count>`

Discover the most popular products on Campus Mart based on views and interactions.

**Features:**
- Popularity score calculation
- Dynamic ranking based on views, wishlists, and orders
- Real-time trending updates
- Most viewed products first
- Community-driven discovery

**Popularity Score Calculation:**
```
Score = (view_count × 1) + (wishlist_count × 5) + (order_count × 10)
```

---

## Smart Recommendation System

Campus Mart uses a **Collaborative Filtering Recommendation Engine** to suggest relevant products to users based on similar student interests and interactions.

### How It Works

The system learns from:

- Wishlist activity  
- Purchase history  
- Product clicks/views  
- Search behavior  
- Similar users with common interests  

### Example

If User A and User B both liked engineering books, and User B also liked a calculator, the system may recommend that calculator to User A.

### Benefits

- Personalized homepage feed  
- Better product discovery  
- Faster buying decisions  
- Improved engagement  

---

## Location-Based Search (Nearest First)

Campus Mart prioritizes products nearest to the buyer for faster pickup and easier transactions.

### How It Works

During registration or product listing:

- User hostel / block / department / campus area is stored  
- Seller location coordinates are saved  
- Buyer searches products  
- Results are sorted by nearest distance first  

### Example

If the buyer is in Hostel A:

1. Products in Hostel A  
2. Products in nearby Hostel B  
3. Products in farther campus zones  

### Benefits

- Faster handover  
- Lower travel effort  
- Better local trust network  

---

## Implementation Approach

### Collaborative Filtering Algorithm

We use **User-Based Collaborative Filtering**.

### Data Matrix Example

| User | Book | Laptop | Chair | Calculator |
|------|------|--------|-------|------------|
| A | 1 | 0 | 1 | 0 |
| B | 1 | 1 | 1 | 1 |
| C | 0 | 1 | 0 | 1 |

Where:

- `1` = interacted / liked / bought  
- `0` = no interaction  

### Steps

1. Build user-product interaction matrix  
2. Find similar users using cosine similarity  
3. Recommend products liked by similar users  
4. Exclude already purchased items  

### Python Libraries (for future implementation)

```bash
pip install pandas scikit-learn numpy
````

### Sample Logic

```python
from sklearn.metrics.pairwise import cosine_similarity
```

---

## Location Search Implementation

Store latitude and longitude in product table:

```sql
latitude FLOAT,
longitude FLOAT
```

Use **Haversine Formula** to calculate distance.

### Formula

Distance between two coordinates using Earth radius.

### Python Example

```python
import math
```

Then sort products by shortest distance.

---

## Technology Stack

| Layer      | Technology                         |
| ---------- | ---------------------------------- |
| Frontend   | HTML5, CSS3, JavaScript, Bootstrap |
| Backend    | Python, Flask                      |
| Database   | SQLite / PostgreSQL                |
| ORM        | SQLAlchemy                         |
| ML Engine  | Scikit-learn                       |
| Deployment | Localhost / Cloud Ready            |

---

## System Architecture

```text
Client Browser
     ↓
Frontend Interface
     ↓
Flask Application Server
     ↓
Recommendation Engine + Search Engine
     ↓
SQLAlchemy ORM
     ↓
Database
```

---

## Project Structure

```text
campus-mart/
├── app.py
├── database.py
├── requirements.txt
├── README.md
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/
└── templates/
    ├── index.html
    ├── login.html
    ├── register.html
    ├── dashboard.html
    └── product.html
```

---

## Future Enhancements

* Hybrid recommendation system
* Real-time chat
* College email verification
* Product ratings and reviews
* Mobile application
* AI fraud detection

---

## Contributors

Developed by the Campus Mart Team.

---

## License

This project is intended for academic and educational use.

```
```
 

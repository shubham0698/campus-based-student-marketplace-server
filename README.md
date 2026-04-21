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

## Key Features

### User Management
- Student registration and login  
- Secure password authentication  
- User profile management  
- Session-based access control  

### Marketplace
- Create product listings  
- Upload product images  
- Add pricing and descriptions  
- Manage listing availability  
- Edit or remove products  

### Discovery
- Search products by keyword  
- Browse by category  
- View latest listings  
- Location-based nearest product results  
- Personalized recommendations using collaborative filtering  

### Communication
- Direct messaging between buyer and seller  
- Product inquiry support  

### Orders & Interest Tracking
- Purchase requests  
- Wishlist functionality  
- Listing status updates  

### Security & Reliability
- Input validation  
- Structured database design  
- Secure backend architecture  

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

### Python Libraries

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
 

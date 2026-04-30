# recommendations.py

import numpy as np
from math import radians, sin, cos, sqrt, atan2
from models import User, Product, Wishlist, Order


# ==================================================
# HAVERSINE DISTANCE CALCULATION
# ==================================================
def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate distance between two coordinates using Haversine formula.
    Returns distance in kilometers.
    """
    R = 6371  # Earth's radius in kilometers
    
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    
    return R * c


# ==================================================
# LOCATION-BASED SEARCH
# ==================================================
def get_nearest_products(user_id, max_distance=50, limit=10):
    """
    Get products nearest to user's location.
    
    Args:
        user_id: Current user's ID
        max_distance: Maximum distance in kilometers (default: 50km)
        limit: Number of products to return
    
    Returns:
        List of products sorted by distance (nearest first)
    """
    user = User.query.get(user_id)
    
    if not user or (user.latitude == 0.0 and user.longitude == 0.0):
        # If user location not set, return latest products
        return Product.query.filter_by(status="available").order_by(
            Product.created_at.desc()
        ).limit(limit).all()
    
    all_products = Product.query.filter_by(status="available").all()
    
    # Calculate distance for each product
    products_with_distance = []
    
    for product in all_products:
        seller = product.owner
        
        if seller and not (seller.latitude == 0.0 and seller.longitude == 0.0):
            distance = haversine_distance(
                user.latitude,
                user.longitude,
                seller.latitude,
                seller.longitude
            )
            
            if distance <= max_distance:
                products_with_distance.append((product, distance))
    
    # Sort by distance
    products_with_distance.sort(key=lambda x: x[1])
    
    # Return only products, limited by limit parameter
    return [p[0] for p in products_with_distance[:limit]]


# ==================================================
# BUILD USER-PRODUCT INTERACTION MATRIX
# ==================================================
def build_interaction_matrix():
    """
    Build user-product interaction matrix.
    Interactions include: wishlists, orders, and product views.
    
    Returns:
        Tuple of (matrix, user_list, product_list)
    """
    users = User.query.all()
    products = Product.query.filter_by(status="available").all()
    
    if not users or not products:
        return None, [], []
    
    user_list = [u.id for u in users]
    product_list = [p.id for p in products]
    
    user_index = {uid: idx for idx, uid in enumerate(user_list)}
    product_index = {pid: idx for idx, pid in enumerate(product_list)}
    
    # Create matrix (users x products)
    matrix = np.zeros((len(users), len(products)))
    
    # Add wishlist interactions
    wishlists = Wishlist.query.all()
    for wishlist in wishlists:
        if wishlist.user_id in user_index and wishlist.product_id in product_index:
            user_idx = user_index[wishlist.user_id]
            product_idx = product_index[wishlist.product_id]
            matrix[user_idx][product_idx] += 1
    
    # Add order interactions (weighted more heavily)
    orders = Order.query.all()
    for order in orders:
        if order.buyer_id in user_index and order.product_id in product_index:
            user_idx = user_index[order.buyer_id]
            product_idx = product_index[order.product_id]
            matrix[user_idx][product_idx] += 2
    
    # Add view count interactions
    for product in products:
        if product.id in product_index:
            product_idx = product_index[product.id]
            if product.view_count > 0:
                # Normalize view count
                for user_idx in range(len(users)):
                    if matrix[user_idx][product_idx] == 0:
                        matrix[user_idx][product_idx] += min(product.view_count / 10, 1)
    
    return matrix, user_list, product_list


# ==================================================
# CALCULATE COSINE SIMILARITY
# ==================================================
def cosine_similarity(vec1, vec2):
    """
    Calculate cosine similarity between two vectors.
    
    Args:
        vec1: First vector
        vec2: Second vector
    
    Returns:
        Similarity score (0-1)
    """
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0
    
    return dot_product / (norm_vec1 * norm_vec2)


# ==================================================
# FIND SIMILAR USERS
# ==================================================
def find_similar_users(user_id, num_similar=5):
    """
    Find users similar to the given user based on interactions.
    
    Args:
        user_id: Target user's ID
        num_similar: Number of similar users to return
    
    Returns:
        List of similar user IDs with similarity scores
    """
    matrix, user_list, product_list = build_interaction_matrix()
    
    if matrix is None or user_id not in user_list:
        return []
    
    user_idx = user_list.index(user_id)
    user_vector = matrix[user_idx]
    
    similarities = []
    
    for idx, uid in enumerate(user_list):
        if uid != user_id:
            similarity = cosine_similarity(user_vector, matrix[idx])
            similarities.append((uid, similarity))
    
    # Sort by similarity (descending)
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    return similarities[:num_similar]


# ==================================================
# COLLABORATIVE FILTERING RECOMMENDATIONS
# ==================================================
def get_recommendations(user_id, num_recommendations=5):
    """
    Get product recommendations using collaborative filtering.
    
    Algorithm:
    1. Find similar users based on interaction history
    2. Find products liked by similar users
    3. Exclude products already liked by current user
    4. Rank by aggregated similarity scores
    
    Args:
        user_id: Target user's ID
        num_recommendations: Number of recommendations to return
    
    Returns:
        List of recommended products
    """
    # Get current user's liked products
    user_wishlists = Wishlist.query.filter_by(user_id=user_id).all()
    user_orders = Order.query.filter_by(buyer_id=user_id).all()
    
    liked_product_ids = set()
    for wishlist in user_wishlists:
        liked_product_ids.add(wishlist.product_id)
    for order in user_orders:
        liked_product_ids.add(order.product_id)
    
    # Find similar users
    similar_users = find_similar_users(user_id, num_similar=10)
    
    if not similar_users:
        # Fallback: return trending products
        return Product.query.filter_by(status="available").order_by(
            Product.view_count.desc()
        ).limit(num_recommendations).all()
    
    # Get products liked by similar users
    recommendation_scores = {}
    
    for similar_uid, similarity_score in similar_users:
        similar_user_wishlists = Wishlist.query.filter_by(user_id=similar_uid).all()
        similar_user_orders = Order.query.filter_by(buyer_id=similar_uid).all()
        
        for wishlist in similar_user_wishlists:
            if wishlist.product_id not in liked_product_ids:
                if wishlist.product_id not in recommendation_scores:
                    recommendation_scores[wishlist.product_id] = 0
                recommendation_scores[wishlist.product_id] += similarity_score
        
        for order in similar_user_orders:
            if order.product_id not in liked_product_ids:
                if order.product_id not in recommendation_scores:
                    recommendation_scores[order.product_id] = 0
                recommendation_scores[order.product_id] += similarity_score * 2
    
    # Sort by score
    sorted_recommendations = sorted(
        recommendation_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )
    
    # Get product objects
    recommended_products = []
    for product_id, score in sorted_recommendations:
        product = Product.query.get(product_id)
        if product and product.status == "available":
            recommended_products.append(product)
        
        if len(recommended_products) >= num_recommendations:
            break
    
    return recommended_products


# ==================================================
# TRENDING PRODUCTS (POPULARITY-BASED)
# ==================================================
def get_trending_products(limit=10):
    """
    Get trending products based on views and interactions.
    
    Args:
        limit: Number of products to return
    
    Returns:
        List of trending products
    """
    products = Product.query.filter_by(status="available").all()
    
    # Calculate popularity score
    products_with_score = []
    
    for product in products:
        wishlist_count = Wishlist.query.filter_by(product_id=product.id).count()
        order_count = Order.query.filter_by(product_id=product.id).count()
        
        popularity_score = (product.view_count * 1) + (wishlist_count * 5) + (order_count * 10)
        
        products_with_score.append((product, popularity_score))
    
    # Sort by popularity
    products_with_score.sort(key=lambda x: x[1], reverse=True)
    
    return [p[0] for p in products_with_score[:limit]]

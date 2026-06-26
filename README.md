# 🛍️ Vastra – Fashion E-Commerce Website

Vastra is a full-stack fashion e-commerce web application built using Django. The platform allows users to browse products, manage their cart, create accounts, place orders, and securely pay online — all through a modern and responsive interface.

---

## 🚀 Features

### 🔐 User Authentication
- User Registration (`Register here` link on Login page)
- User Login (Username + Password)
- User Logout
- Session Management
- Navbar dynamically updates with username and logout button when logged in

---

### 🏠 Home Page
- **Hero Section** — Full-width banner with tagline *"Elevate Your Fashion Game"* and a *Shop Now* CTA button
- **Featured Categories** — Visual cards for Men, Women, Shoes, and Accessories
- **Why Choose Vastra?** — Highlights: Free Shipping, Secure Payments, Easy Returns, Premium Quality
- **Trending Products** — Showcases top products (Classic Hoodie, Denim Jacket, Sneakers) with *Add to Cart* buttons
- **Stay Updated** — Newsletter subscription section with email input
- **Footer** — Links for Shop (Men, Women, Shoes, Accessories), Company (About Us, Contact Us), and Legal (Privacy Policy, Terms & Conditions)

---

### 🛒 Product Browsing
- **Category Pages** — Dedicated pages per category (e.g., Men's Collection)
- **Product Cards** — Display product image, star ratings, name, price, and a *View Product* button
- **New Badge** — "New" tag displayed on newly added products
- **Product Detail Page**
  - Large product image
  - Product name and price
  - Full product description
  - Stock availability count
  - *Add to Cart* button
  - Toast notification on successful cart addition (e.g., *'Faded Indigo' Hoodie added to your cart*)
- **Search Bar** — Search products from the navbar

---

### 🛒 Shopping Cart
- Add to Cart from product listing and product detail pages
- Cart item counter shown in Navbar (e.g., *Cart (3)*)
- **Cart Page**
  - Product image, name, and price per item
  - Quantity controls (`-` / `+`) per item
  - Per-item subtotal calculation
  - *Remove Item* button (red)
  - **Price Details Sidebar**
    - Items count and total
    - Shipping: **FREE**
    - Platform Fee: ₹0
    - Total Amount
  - *Proceed to Checkout* button

---

### 📦 Checkout & Orders
- **Checkout Page**
  - Saved delivery address display (Name, Phone, Address, City, State, Pincode)
  - *Change Address* option
  - Order Items list with images, quantities, and prices
  - **Order Summary Sidebar** with total amount and shipping status
  - **Payment Method Selection**
    - Cash on Delivery
    - Razorpay (Online Payment)
  - *Continue* button to proceed with selected payment

---

### 💳 Razorpay Payment Integration
- **Razorpay Payment Page** — Shows total amount, gateway (Razorpay), and currency (INR)
- *Pay Securely* button (blue) with Razorpay Secure Checkout protection badge
- **Razorpay Checkout Modal**
  - Price Summary card
  - Payment Options: Cards, Netbanking, Wallet, Pay Later
  - Card input form (Card Number, MM/YY, CVV)
  - Save card option (RBI guidelines compliant)
  - *Continue* button
  - Secured by Razorpay branding

---

### 👤 User Profile
- **My Account Dashboard** with sidebar navigation:
  - Profile
  - My Orders
  - Addresses
  - Payment Methods
  - Logout
- **Profile Details Page**
  - Full Name, Email, Phone
  - Address, City, State, Pincode
  - *Edit Profile* button

---

### 📋 My Orders
- Order history listed in reverse chronological order
- Each order card displays:
  - Order number (e.g., *Order #6*)
  - Order date and time
  - Total Amount
  - Payment Method (Cash on Delivery / Razorpay)
  - Order Status badge (e.g., **Placed** — green)

---

### 🛠️ Admin Panel
- Django Admin Dashboard
- Manage Products (add, edit, delete)
- Manage Users
- Manage Orders
- Manage Categories

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML5, CSS3, JavaScript |
| Database | SQLite (Current), MySQL (Planned) |
| Payments | Razorpay |
| Version Control | Git, GitHub |

---

## 📂 Project Structure

```
vastra/
│
├── accounts/          # User auth, profile, addresses
├── cart/              # Cart logic and views
├── checkout/          # Checkout and order placement
├── orders/            # Order history and tracking
├── shop/              # Product listings and detail pages
├── static/            # CSS, JS, images
├── templates/         # HTML templates
├── media/             # Uploaded product images
├── manage.py
└── db.sqlite3
```

---

## ⚙️ Installation

### 1. Clone Repository
```bash
git clone https://github.com/PaRaG2314/-Vastra.git
```

### 2. Move Into Project
```bash
cd -Vastra
```

### 3. Create Virtual Environment
```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 5. Install Dependencies
```bash
pip install -r requirements.txt
```

### 6. Run Migrations
```bash
python manage.py migrate
```

### 7. Start Development Server
```bash
python manage.py runserver
```

---

## 📸 Screenshots

### 🏠 Home Page — Hero Section
![Home Page](screenshots/Home_Page.png)

### 🗂️ Featured Categories & Why Choose Vastra
![Home Page 2](screenshots/Home_Page_2.png)

### 🔥 Trending Products
![Trending](screenshots/Trending.png)

### 👕 Men's Collection — Product Listing
![Product Section](screenshots/Product_Section.png)

### 🧥 Product Detail Page
![Product Detail](screenshots/Product_Detail.png)

### 🛒 Cart Page
![Cart](screenshots/Cart.png)

### 📦 Checkout Page
![Checkout](screenshots/Checkout.png)

### 💳 Razorpay — Secure Payment Page
![Razorpay](screenshots/Razorpay.png)

### 💳 Razorpay — Payment Modal
![Razorpay Modal](screenshots/Razorpay_2.png)

### 👤 User Profile
![User Page](screenshots/User_Page.png)

### 📋 My Orders
![My Orders](screenshots/My_Orders.png)

### 🔐 Login Page
![Login](screenshots/Login.png)

### 📬 Newsletter & Footer
![Footer](screenshots/Footer.png)

---

## 🎯 Roadmap / Future Improvements

- [x] ~~Razorpay Integration~~ ✅ Done
- [x] ~~Product Search~~ ✅ Done
- [ ] Multiple Address Support
- [ ] Wishlist
- [ ] Product Reviews & Ratings (user-submitted)
- [ ] Email Notifications (order confirmation)
- [ ] Order Tracking (Shipped, Out for Delivery, Delivered statuses)
- [ ] MySQL Deployment
- [ ] Coupon & Discount Codes
- [ ] Size & Color Selection on Product Page

---

## 👨‍💻 Developer

**Parag Pratim Pan**
Final Year Computer Science Engineering Student
Chitkara University

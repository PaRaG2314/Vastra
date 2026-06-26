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

![Login](Project%20Screenshots/Login.png)

---

### 🏠 Home Page — Hero Section
- Full-width banner with tagline *"Elevate Your Fashion Game"* and a *Shop Now* CTA button

![Home Page](Project%20Screenshots/Home_Page.png)

### 🗂️ Featured Categories & Why Choose Vastra
- **Featured Categories** — Visual cards for Men, Women, Shoes, and Accessories
- **Why Choose Vastra?** — Highlights: Free Shipping, Secure Payments, Easy Returns, Premium Quality

![Home Page 2](Project%20Screenshots/Home_Page__2.png)

### 🔥 Trending Products
- Showcases top products (Classic Hoodie, Denim Jacket, Sneakers) with *Add to Cart* buttons directly from the home page

![Trending](Project%20Screenshots/Trending.png)

### 📬 Newsletter & Footer
- **Stay Updated** — Newsletter subscription section with email input
- **Footer** — Links for Shop (Men, Women, Shoes, Accessories), Company (About Us, Contact Us), and Legal (Privacy Policy, Terms & Conditions)

![Footer](Project%20Screenshots/Footer.png)

---

### 👕 Product Browsing
- **Category Pages** — Dedicated pages per category (e.g., Men's Collection)
- **Product Cards** — Display product image, star ratings, name, price, and a *View Product* button
- **New Badge** — "New" tag displayed on newly added products
- **Search Bar** — Search products from the navbar

![Product Section](Project%20Screenshots/Product_Section.png)

### 🧥 Product Detail Page
- Large product image
- Product name and price
- Full product description
- Stock availability count
- *Add to Cart* button
- Toast notification on successful cart addition (e.g., *'Faded Indigo' Hoodie added to your cart*)

![Product Detail](Project%20Screenshots/Product_Detail.png)

---

### 🛒 Shopping Cart
- Add to Cart from product listing and product detail pages
- Cart item counter shown in Navbar (e.g., *Cart (3)*)
- Product image, name, and price per item
- Quantity controls (`-` / `+`) per item with per-item subtotal
- *Remove Item* button (red)
- **Price Details Sidebar** — Items total, Shipping FREE, Platform Fee ₹0, Total Amount
- *Proceed to Checkout* button

![Cart](Project%20Screenshots/Cart.png)

---

### 📦 Checkout Page
- Saved delivery address display (Name, Phone, Address, City, State, Pincode)
- *Change Address* option
- Order Items list with images, quantities, and prices
- **Order Summary Sidebar** with total amount and shipping status
- **Payment Method Selection** — Cash on Delivery or Razorpay (Online Payment)
- *Continue* button to proceed with selected payment

![Checkout](Project%20Screenshots/Checkout.png)

---

### 💳 Razorpay Payment Integration
- **Secure Payment Page** — Shows total amount, gateway (Razorpay), and currency (INR)
- *Pay Securely* button with Razorpay Secure Checkout protection badge

![Razorpay](Project%20Screenshots/Razorpay.png)

- **Razorpay Checkout Modal**
  - Price Summary card
  - Payment Options: Cards, Netbanking, Wallet, Pay Later
  - Card input form (Card Number, MM/YY, CVV)
  - Save card option (RBI guidelines compliant)
  - Secured by Razorpay branding

![Razorpay Modal](Project%20Screenshots/Razorpay_2.png)

---

### 👤 User Profile
- **My Account Dashboard** with sidebar navigation: Profile, My Orders, Addresses, Payment Methods, Logout
- Profile Details — Full Name, Email, Phone, Address, City, State, Pincode
- *Edit Profile* button

![User Page](Project%20Screenshots/User_Page.png)

---

### 📋 My Orders
- Order history listed in reverse chronological order
- Each order card shows order number, date & time, total amount, payment method, and status badge (e.g., **Placed** — green)

![My Orders](Project%20Screenshots/My_Orders.png)

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
git clone https://github.com/PaRaG2314/Vastra.git
```

### 2. Move Into Project
```bash
cd Vastra
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

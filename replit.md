# The Fidget Shop

## Overview
A static website showcasing fidget toys and products. The site features a product gallery with interactive cards and a clean, modern design.

## Project Architecture
- **Type**: E-commerce website with Flask backend
- **Frontend**: Pure HTML5, CSS3, and vanilla JavaScript
- **Backend**: Flask server with email functionality and CORS support
- **Server**: Flask app running on port 5000
- **Deployment**: Web application deployment

## File Structure
- `index.html` - Main homepage with featured products
- `page1.html` - About Us page
- `page2.html` - Contact page
- `page3.html` - Our Collection page
- `page4.html` - All Products page (with Videos and Accessories links)
- `page5.html` - Our Favorites page
- `page6.html` - Shipping FAQ page
- `page7.html` - Shopping Cart page with color display
- `page8.html` - Videos page with HTML5 video modals
- `page9.html` - Accessories page
- `page10.html` - Checkout page with order form
- `styles.css` - Global styles including cart, video cards, color swatches, and category buttons
- `script.js` - Interactive JavaScript for modals, cart functionality, color selection, banner notifications, and video playback
- `server.py` - Flask server with email API endpoint and cache control headers
- Image assets: `spiral.png`, `inout.png`, `gearshift.png`, `hexagon.png`, `spotlight.png`, `mattress.png`, `rory.png`, `favicon.ico`

## Features
- Responsive product gallery with grid layout
- Interactive modal popups for product details
- **Shopping cart functionality** with localStorage persistence
- **Fixed cart button** in bottom right corner showing item count (always visible)
- **Color/gradient selector** for fidgets with 9 options (beige, red-orange gradient, blue-purple gradient, yellow, red, rainbow gradient, blue, black, white)
- **Color display in cart** - selected color/gradient shown for each cart item
- **Banner notifications** when adding items to cart (no alert popups)
- Add to Cart feature on product modals (fully functional)
- Cart page with item management, color display, and total calculations
- **Checkout page** with complete order form (page10.html)
- **Video gallery page** with HTML5 video modal popups (local MP4 support)
- **Accessories page** with additional products
- **Profile cards** with circular images for Rory and Haydan on About Us page
- **Social media icons** (Twitter, Instagram, YouTube) on Contact page
- **Email contact form** sends to haydandebonis@outlook.com via Flask backend
- Category navigation buttons on All Products page
- Multi-page navigation
- Modern dark theme design with blue gradient accents
- All products priced at $4.50

## Recent Changes
- 2025-11-20: Converted to Flask server for email handling (server.py)
- 2025-11-20: Implemented banner notification system to replace alert() popups
- 2025-11-20: Created color/gradient selector with 9 visual swatches for fidgets
- 2025-11-20: Built checkout page (page10.html) accessible from shopping cart
- 2025-11-20: Repositioned cart button to bottom right corner (fixed position, always visible)
- 2025-11-20: Added selected color/gradient display in shopping cart items
- 2025-11-20: Updated About Us page with profile cards featuring circular images for Rory and Haydan
- 2025-11-20: Added social media icons (Twitter, Instagram, YouTube) to contact page
- 2025-11-20: Converted video player from YouTube iframe to HTML5 video element for local MP4 files
- 2025-11-20: Fixed FAQ answer cutoff issue with proper padding
- 2025-11-20: Fixed logo sizing to display on one line without disrupting navigation
- 2025-11-20: Set up email contact form to send to haydandebonis@outlook.com with proper error handling
- 2025-11-20: Added shopping cart functionality with localStorage
- 2025-11-20: Created cart page (page7.html) with checkout link
- 2025-11-20: Created Videos page (page8.html) with video modals
- 2025-11-20: Created Accessories page (page9.html)
- 2025-11-20: Updated all product prices to $4.50
- 2025-11-18: Applied custom blue gradient theme with Inter font
- 2025-11-18: Made hero sections on pages 3 and 5 full-screen like homepage
- 2025-11-18: Added interactive FAQ accordion with smooth animations
- 2025-11-18: Initial Replit environment setup

## Setup Requirements
- **SMTP Configuration**: To enable email functionality, set up the following secrets in Replit:
  - `SMTP_SERVER` (default: smtp.gmail.com)
  - `SMTP_PORT` (default: 587)
  - `SMTP_USER` (your email address)
  - `SMTP_PASSWORD` (your email password or app-specific password)
- **Video Files**: Upload local MP4 files for product videos (e.g., thespiral.mp4, gearshifter.mp4) to enable video playback

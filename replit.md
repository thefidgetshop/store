# The Fidget Shop

## Overview
A static website showcasing fidget toys and products. The site features a product gallery with interactive cards and a clean, modern design.

## Project Architecture
- **Type**: Static HTML/CSS/JavaScript website
- **Frontend**: Pure HTML5, CSS3, and vanilla JavaScript
- **Server**: Python HTTP server for local development
- **Deployment**: Static site deployment

## File Structure
- `index.html` - Main homepage with featured products
- `page1.html` - About Us page
- `page2.html` - Contact page
- `page3.html` - Our Collection page
- `page4.html` - All Products page (with Videos and Accessories links)
- `page5.html` - Our Favorites page
- `page6.html` - Shipping FAQ page
- `page7.html` - Shopping Cart page (NEW)
- `page8.html` - Videos page with video modals (NEW)
- `page9.html` - Accessories page (NEW)
- `styles.css` - Global styles including cart, video cards, and category buttons
- `script.js` - Interactive JavaScript for modals, cart functionality, and video playback
- `server.py` - Python HTTP server with cache control headers
- Image assets: `spiral.png`, `inout.png`, `gearshift.png`, `hexagon.png`, `spotlight.png`, `mattress.png`, `rory.png`, `favicon.ico`

## Features
- Responsive product gallery with grid layout
- Interactive modal popups for product details
- **Shopping cart functionality** with localStorage persistence
- Cart button in header showing item count on all pages
- Add to Cart feature on product modals (fully functional)
- Cart page with item management and total calculations
- **Video gallery page** with video modal popups
- **Accessories page** with additional products
- Category navigation buttons on All Products page
- Multi-page navigation
- Modern dark theme design with blue gradient accents
- All products priced at $4.50

## Recent Changes
- 2025-11-20: Added shopping cart functionality with localStorage
- 2025-11-20: Created cart page (page7.html) with checkout button (coming soon)
- 2025-11-20: Created Videos page (page8.html) with video modals
- 2025-11-20: Created Accessories page (page9.html)
- 2025-11-20: Added cart button to header on all pages
- 2025-11-20: Changed "Buy Now" to "Add to Cart" and made it functional
- 2025-11-20: Updated all product prices to $4.50
- 2025-11-20: Added more product cards to all product pages
- 2025-11-20: Added Videos and Accessories category buttons to All Products page
- 2025-11-18: Applied custom blue gradient theme with Inter font
- 2025-11-18: Made hero sections on pages 3 and 5 full-screen like homepage
- 2025-11-18: Added interactive FAQ accordion with smooth animations
- 2025-11-18: Styled contact form with gradient buttons
- 2025-11-18: Initial Replit environment setup

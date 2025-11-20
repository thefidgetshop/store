document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("productModal");
    const modalImg = document.getElementById("modalImage");
    const modalTitle = document.getElementById("modalTitle");
    const modalDesc = document.getElementById("modalDescription");
    const modalPrice = document.getElementById("modalPrice");
    const closeBtn = document.querySelector(".close-btn");
    const addToCartBtn = document.getElementById("addToCartBtn");

    updateCartCount();

    document.querySelectorAll(".see-more-btn").forEach(btn => {
        btn.addEventListener("click", e => {
            const card = e.target.closest(".product-card") || e.target.closest(".product-item");

            modalImg.src = card.querySelector("img").src;
            modalTitle.textContent = card.querySelector("h4").textContent;
            modalDesc.textContent = card.querySelector("p").textContent;
            modalPrice.textContent = card.dataset.price || "$4.50";

            modal.style.display = "flex";
        });
    });

    if (closeBtn) {
        closeBtn.addEventListener("click", () => {
            modal.style.display = "none";
        });
    }

    if (modal) {
        modal.addEventListener("click", e => {
            if (e.target === modal) modal.style.display = "none";
        });
    }

    if (addToCartBtn) {
        addToCartBtn.addEventListener("click", () => {
            const item = {
                name: modalTitle.textContent,
                price: modalPrice.textContent,
                image: modalImg.src
            };
            addToCart(item);
            modal.style.display = "none";
            alert("Added to cart!");
        });
    }

    const videoModal = document.getElementById("videoModal");
    const videoFrame = document.getElementById("videoFrame");
    const videoTitle = document.getElementById("videoTitle");
    const videoCloseBtn = document.getElementById("videoCloseBtn");

    document.querySelectorAll(".watch-btn").forEach(btn => {
        btn.addEventListener("click", e => {
            const card = e.target.closest(".video-card");
            videoTitle.textContent = card.querySelector("h4").textContent;
            videoFrame.src = card.dataset.video;
            videoModal.style.display = "flex";
        });
    });

    if (videoCloseBtn) {
        videoCloseBtn.addEventListener("click", () => {
            videoModal.style.display = "none";
            videoFrame.src = "";
        });
    }

    if (videoModal) {
        videoModal.addEventListener("click", e => {
            if (e.target === videoModal) {
                videoModal.style.display = "none";
                videoFrame.src = "";
            }
        });
    }

    if (window.location.pathname.includes("page7.html")) {
        loadCart();
    }
});

function addToCart(item) {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    cart.push(item);
    localStorage.setItem("cart", JSON.stringify(cart));
    updateCartCount();
}

function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem("cart")) || [];
    const cartCountElements = document.querySelectorAll("#cartCount");
    cartCountElements.forEach(el => {
        el.textContent = cart.length;
    });
}

function loadCart() {
    const cart = JSON.parse(localStorage.getItem("cart")) || [];
    const cartItems = document.getElementById("cartItems");
    const cartEmpty = document.getElementById("cartEmpty");
    const cartSummary = document.getElementById("cartSummary");

    if (cart.length === 0) {
        cartEmpty.style.display = "block";
        cartSummary.style.display = "none";
        return;
    }

    cartEmpty.style.display = "none";
    cartSummary.style.display = "block";

    cartItems.innerHTML = "";
    let total = 0;

    cart.forEach((item, index) => {
        const price = parseFloat(item.price.replace("$", ""));
        total += price;

        const itemDiv = document.createElement("div");
        itemDiv.className = "cart-item";
        itemDiv.innerHTML = `
            <img src="${item.image}" alt="${item.name}">
            <div class="cart-item-details">
                <h4>${item.name}</h4>
                <p class="cart-item-price">${item.price}</p>
            </div>
            <button class="remove-btn" onclick="removeFromCart(${index})">Remove</button>
        `;
        cartItems.appendChild(itemDiv);
    });

    document.getElementById("subtotal").textContent = "$" + total.toFixed(2);
    document.getElementById("total").textContent = "$" + total.toFixed(2);
}

function removeFromCart(index) {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    cart.splice(index, 1);
    localStorage.setItem("cart", JSON.stringify(cart));
    updateCartCount();
    loadCart();
}

document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("productModal");
    const modalImg = document.getElementById("modalImage");
    const modalTitle = document.getElementById("modalTitle");
    const modalDesc = document.getElementById("modalDescription");
    const closeBtn = document.querySelector(".close-btn");

    document.querySelectorAll(".see-more-btn").forEach(btn => {
        btn.addEventListener("click", e => {
            const card = e.target.closest(".product-card") || e.target.closest(".product-item");

            modalImg.src = card.querySelector("img").src;
            modalTitle.textContent = card.querySelector("h4").textContent;
            modalDesc.textContent = card.querySelector("p").textContent;

            modal.style.display = "flex";
        });
    });

    closeBtn.addEventListener("click", () => {
        modal.style.display = "none";
    });

    modal.addEventListener("click", e => {
        if (e.target === modal) modal.style.display = "none";
    });
});

const container = document.querySelector('.image-container');

function scrollImages() {
    const firstChild = container.firstElementChild;
    container.appendChild(firstChild);
}

setInterval(scrollImages, 3000);

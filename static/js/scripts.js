/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

// counter
const increase = document.querySelector(".increase");
const decrease = document.querySelector(".decrease");
const counterValue = document.querySelector(".counter-value");

increase.addEventListener("click", handleIncrease);
decrease.addEventListener("click", handleDecrease);

function handleDecrease(event) {
    if (counterValue.textContent === "1") {
        return;
    }
    counterValue.textContent = Number(counterValue.textContent) - 1;
}

function handleIncrease(event) {
    counterValue.textContent = Number(counterValue.textContent) + 1;
}



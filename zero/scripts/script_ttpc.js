const box = document.querySelector('.box');
const slider = document.querySelector('.slider');
const slides = Array.from(slider.querySelectorAll('img'));
const slideCount = slides.length/3;
let slideIndex = 0;


function nextSlide(){
  slideIndex = (slideIndex + 1) % slideCount;
  slide();
}

const slide = () => {
  const imageHeight = box.clientHeight + box.clientHeight/90 + 50;
  const slideOffsetH = -slideIndex * imageHeight;
  slider.style.transform = `translateY(${slideOffsetH}px)`;
}

window.addEventListener('load', () => {
  slide();
});

document.getElementById("upButton").addEventListener("click", function() {
  nextSlide();
});



const box = document.querySelector('.box');
const slider = document.querySelector('.slider');
const slides = Array.from(slider.querySelectorAll('.box'));
const slideCount = slides.length;
let slideIndex = 0;
let timer = 0;

function nextSlide() {
  slideIndex = (slideIndex + 1) % slideCount;
  slide();
  const currentSlide = slides[slideIndex];
  const interval = parseInt(currentSlide.getAttribute('data-interval'));
  
  // Очищаем предыдущий таймер и устанавливаем новый интервал
  clearInterval(timer);
  timer = setInterval(nextSlide, interval);
}

const slide = () => {
  // const slideHeight = slide.clientHeight;
  const imageHeight = box.clientHeight;
  const slideOffsetH = -slideIndex * imageHeight;
  // const slideOffsetH = slideHeight/slideCount;
  slider.style.transform = `translateY(${slideOffsetH}px)`;
}

window.addEventListener('load', () => {
  slide();
  const currentSlide = slides[slideIndex];
  const interval = parseInt(currentSlide.getAttribute('data-interval'));
  
  // Устанавливаем интервал для первого слайда
  timer = setInterval(nextSlide, interval);
});

function updateProgressBar(value) {
  progressBar.style.width = value + '%';
}

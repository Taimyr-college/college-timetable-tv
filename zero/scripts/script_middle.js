const box = document.querySelector('.box');
const slider = document.querySelector('.slider');
const slides = Array.from(slider.querySelectorAll('.box'));
const progressBar = document.querySelector('.progress-bar-inner');
const slideCount = slides.length;
let slideIndex = 0;
let time = 0;
let speed = 10;
let step = 0;
let timer = 60000;

setInterval(seconds, speed);
setInterval(nextSlide, timer);

function nextSlide(){
  speed *= -1
  slideIndex = (slideIndex + 1) % slideCount;
  slide();
}

function seconds(){
  progress(time);
  time += speed;
}

function progress(sec){
  updateProgressBar(step);
  step = (sec/timer)*100;
}

const slide = () => {
  const imageHeight = box.clientHeight + box.clientHeight/90;
  const slideOffsetH = -slideIndex * imageHeight;
  slider.style.transform = `translateY(${slideOffsetH}px)`;
}

function updateProgressBar(value) {
  progressBar.style.width = value + '%';
}

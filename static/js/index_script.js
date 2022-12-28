
window.onload = () =>{/*window載入時套用上方的命令*/

  if(window.scrollY > 80){
    document.querySelector('.header .header-2').classList.add('active');
  }else{
    document.querySelector('.header .header-2').classList.remove('active');
  }
}

var swiper = new Swiper(".books-slider", {
  loop:true,
  centeredSlides: true,
  autoHeight: true,
  observer: true, //修改swiper自己或子元素时，自动初始化swiper，主要是这两行
  observeParents: true, //修改swiper的父元素时，自动初始化swiper
  autoplay: {
    delay: 9500,
    disableOnInteraction: false,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});

var swiper = new Swiper(".featured-slider", {
  spaceBetween: 10,
  loop:true,
  centeredSlides: true,
  autoHeight: true,
  observer: true, //修改swiper自己或子元素时，自动初始化swiper，主要是这两行
  observeParents: true, //修改swiper的父元素时，自动初始化swiper
  autoplay: {
    delay: 9500,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    450: {
      slidesPerView: 2,
    },
    768: {
      slidesPerView: 3,
    },
    1024: {
      slidesPerView: 4,
    },
  },
});

var swiper = new Swiper(".arrivals-slider", {
  spaceBetween: 10,
  loop:true,
  centeredSlides: true,
  autoHeight: true,
  observer: true, //修改swiper自己或子元素时，自动初始化swiper，主要是这两行
  observeParents: true, //修改swiper的父元素时，自动初始化swiper
  autoplay: {
    delay: 9500,
    disableOnInteraction: false,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 4,
    },
  },
});

var swiper = new Swiper(".reviews-slider", {
  spaceBetween: 10,
  grabCursor:true,
  loop:true,
  centeredSlides: true,
  autoHeight: true,
  observer: true, //修改swiper自己或子元素时，自动初始化swiper，主要是这两行
  observeParents: true, //修改swiper的父元素时，自动初始化swiper
  autoplay: {
    delay: 9500,
    disableOnInteraction: false,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});

var swiper = new Swiper(".blogs-slider", {
  spaceBetween: 10,
  grabCursor:true,
  loop:true,
  centeredSlides: true,
  autoHeight: true,
  observer: true, //修改swiper自己或子元素时，自动初始化swiper，主要是这两行
  observeParents: true, //修改swiper的父元素时，自动初始化swiper
  autoplay: {
    delay: 9500,
    disableOnInteraction: false,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});


 
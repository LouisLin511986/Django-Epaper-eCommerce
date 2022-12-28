searchForm = document.querySelector('.search-form');/*{搜尋畫面}querySelector()方法返回與 CSS 選擇器匹配的第一個元素 :https://www.w3schools.com/jsref/met_document_queryselector.asp。*/

document.querySelector('#search-btn').onclick = () =>{
  searchForm.classList.toggle('active');/*{彈出及退出}classList.toggle~~在元素的兩個類之間切換：{前}有2種模式 :正常模式於css150、另一種為max*width:768px時(display: none;) 於css780(display: inline-block;)，{後}~css798(top:115%;) :https://www.w3schools.com/jsref/prop_element_classlist.asp*/
}

let loginForm = document.querySelector('.login-form-container');/*登入畫面*/

window.onscroll = () =>{/*onscroll 事件在元素的滾動條被滾動時發生 :https://www.w3schools.com/jsref/event_onscroll.asp。*/

  searchForm.classList.remove('active');/*remove()方法從 DOM 中刪除指定的元素 :https://www.w3schools.com/jsref/met_element_remove.asp。*/

  if(window.scrollY > 80){/*scrollY屬性返回文檔從窗口左上角滾動的像素 :https://www.w3schools.com/jsref/prop_win_scrolly.asp。*/
    document.querySelector('.header .header-2').classList.add('active');/*若捲動像素>80，則增加css174(.header .header-2.active{position:fixed;top:0; left:0; right:0;z-index: 1000;})*/
  }else{
    document.querySelector('.header .header-2').classList.remove('active');/*反之則移除*/
  }

}

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

var swiper = new Swiper(".reviews-slider", {
  spaceBetween: 10,
  grabCursor:true,
  loop:true,
  centeredSlides: true,
  autoHeight: true,
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


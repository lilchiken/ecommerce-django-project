(function($) {
  
  "use strict";

  // Preloader
  function stylePreloader() {
    $('body').addClass('preloader-deactive');
  }

  // Background Image
  const bgSelector = $("[data-bg-img]");
  bgSelector.each(function (index, elem) {
    let element = $(elem),
      bgSource = element.data('bg-img');
    element.css('background-image', 'url(' + bgSource + ')');
  });

  // Background Color
  $('[data-bg-color]').each(function() {
    $(this).css('background-color', $(this).data("bg-color"));
  });
  // Height
  $('[data-height]').each(function() {
    $(this).css('height', $(this).data("height"));
  });
  // Width
  $('[data-width]').each(function() {
    $(this).css('width', $(this).data("width"));
  });
  // Margin Top
  $('[data-margin-top]').each(function() {
    $(this).css('margin-top', $(this).data("margin-top"));
  });
  // Margin Bottom
  $('[data-margin-bottom]').each(function() {
    $(this).css('margin-bottom', $(this).data("margin-bottom"));
  });
  // Padding Top
  $('[data-padding-top]').each(function() {
    $(this).css('padding-top', $(this).data("padding-top"));
  });
  // Padding Bottom
  $('[data-padding-bottom]').each(function() {
    $(this).css('padding-bottom', $(this).data("padding-bottom"));
  });

  // Off Canvas JS
  var canvasWrapper = $(".off-canvas-wrapper");
  $(".btn-menu").on('click', function() {
    canvasWrapper.addClass('active');
    $("body").addClass('fix');
  });

  $(".close-action > .btn-menu-close, .off-canvas-overlay").on('click', function() {
    canvasWrapper.removeClass('active');
    $("body").removeClass('fix');
  });

  // Sticky Header Js
  var headroom = $(".sticky-header");
  headroom.headroom({
    offset: 280,
    tolerance: 5,
    classes: {
      initial: "headroom",
      pinned: "slideDown",
      unpinned: "slideUp",
      notTop: "sticky"
    }
  });

  //Responsive Slicknav JS
  $('.main-menu').slicknav({
    appendTo: '.res-mobile-menu',
    closeOnClick: false,
    removeClasses: true,
    closedSymbol: '<i class="fa fa-plus"></i>',
    openedSymbol: '<i class="fa fa-minus"></i>'
  });

  // Menu Activeion Js
  var cururl = window.location.pathname;
  var curpage = cururl.substr(cururl.lastIndexOf('/') + 1);
  var hash = window.location.hash.substr(1);
  if((curpage == "" || curpage == "/" || curpage == "admin") && hash=="")
    {
    } else {
      $(".header-navigation-area li").each(function()
    {
      $(this).removeClass("active");
    });
    if(hash != "")
      $(".header-navigation-area li a[href='"+hash+"']").parents("li").addClass("active");
    else
    $(".header-navigation-area li a[href='"+curpage+"']").parents("li").addClass("active");
  }

  // Notification Js
  var nToggle = $('.notification-close-btn');
  nToggle.on('click', function(){
    $('.top-notification-bar').slideToggle();
  })

  // Header JS
  $(".currency-menu .title").on('click', function() {
    $(".currency-dropdown").toggleClass("show").focus();
  });
  $(".user-menu .title").on('click', function() {
    $(".user-dropdown").toggleClass("show").focus();
  });
  $(".header-search .search-toggle").on('click', function() {
    $(".header-search-form").toggleClass("search-open").focus();
  });
  $(".search-toggle").on('click', function() {
    $(".header-search").toggleClass("open").focus();
  });
  $(".header-mini-cart .mini-cart-toggle").on('click', function() {
    $(".mini-cart-dropdown").toggleClass("show").focus();
  });

  // Popup Quick View JS
  var popupProduct = $(".product-quick-view-modal");
  $(".add-quick-view").on('click', function() {
    popupProduct.addClass('active');
    $("body").addClass("fix");
  });
  $(".btn-close, .canvas-overlay").on('click', function() {
    popupProduct.removeClass('active');
    $("body").removeClass("fix");
  });

  // Review Form JS
  $(".review-write-btn").on('click', function() {
    $(".reviews-form-area, .review-write-btn").toggleClass("show").focus();
  });

  // Swiper Slider Js
    var carouselSlider = new Swiper('.default-slider-container', {
      slidesPerView : 1,
      slidesPerGroup: 1,
      loop: true,
      speed: 500,
      spaceBetween : 0,
      effect: 'fade',
      fadeEffect: {
        crossFade: true,
      },
      autoplay: {
        delay: 4000,
      },
      navigation: {
          nextEl: '.default-slider-container .swiper-button-next',
          prevEl: '.default-slider-container .swiper-button-prev',
      },
    });
    $(".default-slider-container").hover(function() {
      (this).swiper.autoplay.stop();
    }, function() {
      (this).swiper.autoplay.start();
    });

  // Product Slider Js
    var productSlider = new Swiper('.product-slider-container', {
      slidesPerGroup: 2,
      loop: true,
      speed: 600,
      navigation: {
        nextEl: '.product-slider-container .swiper-button-next',
        prevEl: '.product-slider-container .swiper-button-prev',
      },
      pagination: {
        el: '.product-swiper-pagination .swiper-pagination',
        clickable: 'true',
      },
      breakpoints: {
        1200: {
          slidesPerView : 4,
          spaceBetween: 30,
        },
        992: {
          slidesPerView : 3,
          spaceBetween: 30,
        },
        576: {
          slidesPerView : 2,
          spaceBetween: 30,
        },
        0: {
          slidesPerView : 1,
          spaceBetween: 30,
        },
      }
    });
    $(".product-slider-container").hover(function() {
      (this).swiper.autoplay.stop();
    }, function() {
      (this).swiper.autoplay.start();
    });

  // Post Slider Js
    var swiper = new Swiper('.post-slider-container', {
      slidesPerGroup: 1,
      spaceBetween: 30,
      speed: 600,
      navigation: {
        nextEl: '.post-slider-container .swiper-button-next',
        prevEl: '.post-slider-container .swiper-button-prev',
      },
      breakpoints: {
        992: {
          slidesPerView : 3,
        },
        748: {
          slidesPerView : 2,
        },
        0: {
          slidesPerView : 1,
        },
      }
    });

  // Brand Logo Slider Js
    var swiper = new Swiper('.brand-logo-slider-container', {
      autoplay: {
        delay: 4000,
      },
      lope: true,
      slidesPerGroup: 1,
      speed: 500,
      breakpoints: {
        1200: {
          slidesPerView : 5,
          spaceBetween : 0,
        },
        992: {
          slidesPerView : 4,
          spaceBetween : 0,
        },
        576: {
          slidesPerView : 3,
          spaceBetween : 0,
        },
        480: {
          slidesPerView : 2,
          spaceBetween : 0,
        },
        0: {
          slidesPerView : 1,
          spaceBetween : 0,
        },
      }
    });

  // Product Single Thumb Slider2 Js
    var ProductNav = new Swiper('.single-product-nav-slider', {
      loop: true,
      slidesPerGroup: 1,
      watchSlidesVisibility: true,
      watchSlidesProgress: true,
      navigation: {
        nextEl: '.single-product-nav-slider .swiper-button-next',
        prevEl: '.single-product-nav-slider .swiper-button-prev',
      },
      breakpoints: {
        576: {
          slidesPerView : 3,
          spaceBetween: 14,
        },
        0: {
          slidesPerView : 2,
          spaceBetween: 15,
        },
      }
    });
    var ProductThumb = new Swiper('.single-product-thumb-slider', {
      effect: 'fade',
      loop: true,
      fadeEffect: {
        crossFade: true,
      },
      thumbs: {
        swiper: ProductNav
      }
    });

  // Fancybox Js
  $('.image-popup').fancybox();
  $('.video-popup').fancybox();

  // Aos Js
  AOS.init({
    once: true,
    duration: 1200,
  });

  // Parallax Scene Js
  $('.scene').each(function () {
    new Parallax($(this)[0]);
  });

  // Product Quantity JS
  var proQty = $(".pro-qty");
  proQty.append('<div class="inc qty-btn">+</div>');
  proQty.append('<div class= "dec qty-btn">-</div>');
  $('.qty-btn').on('click', function (e) {
    e.preventDefault();
    var $button = $(this);
    var oldValue = $button.parent().find('input').val();
    if ($button.hasClass('inc')) {
      var newVal = parseFloat(oldValue) + 1;
    } else {
      // Don't allow decrementing below zero
      if (oldValue > 1) {
        var newVal = parseFloat(oldValue) - 1;
      } else {
        newVal = 1;
      }
    }
    $button.parent().find('input').val(newVal);
  });

  // Countdown Js 
  $(".ht-countdown").each(function(index, element) {
    var $element = $(element),
    $date = $element.data('date');
    $element.countdown($date, function(event) {
      var $this = $(this).html(event.strftime(''
      +
      '<div class="countdown-item"><span class="countdown-item__time">%D</span><span class="countdown-item__label">days</span></div>' +
      '<div class="countdown-item"><span class="countdown-item__time">%H</span><span class="countdown-item__label">Hour</span></div>' +
      '<div class="countdown-item"><span class="countdown-item__time">%M</span><span class="countdown-item__label">Min</span></div>' +
      '<div class="countdown-item"><span class="countdown-item__time">%S</span><span class="countdown-item__label">Sec</span></div>'));
    });
  });

  // Ajax Contact Form JS
  var form = $('#contact-form');
  var formMessages = $('.form-message');

  $(form).submit(function(e) {
    e.preventDefault();
    var formData = form.serialize();
    $.ajax({
      type: 'POST',
      url: form.attr('action'),
      data: formData
    }).done(function(response) {
      // Make sure that the formMessages div has the 'success' class.
      $(formMessages).removeClass('alert alert-danger');
      $(formMessages).addClass('alert alert-success fade show');

      // Set the message text.
      formMessages.html("<button type='button' class='btn-close' data-bs-dismiss='alert'>&times;</button>");
      formMessages.append(response);

      // Clear the form.
      $('#contact-form input,#contact-form textarea').val('');
    }).fail(function(data) {
      // Make sure that the formMessages div has the 'error' class.
      $(formMessages).removeClass('alert alert-success');
      $(formMessages).addClass('alert alert-danger fade show');

      // Set the message text.
      if (data.responseText !== '') {
        formMessages.html("<button type='button' class='btn-close' data-bs-dismiss='alert'>&times;</button>");
        formMessages.append(data.responseText);
      } else {
        $(formMessages).text('Oops! An error occurred and your message could not be sent.');
      }
    });
  });

  function scrollToTop() {
    var $scrollUp = $('#scroll-to-top'),
      $lastScrollTop = 0,
      $window = $(window);
      $window.on('scroll', function () {
      var st = $(this).scrollTop();
        if (st > $lastScrollTop) {
            $scrollUp.removeClass('show');
        } else {
          if ($window.scrollTop() > 120) {
            $scrollUp.addClass('show');
          } else {
            $scrollUp.removeClass('show');
          }
        }
        $lastScrollTop = st;
    });
    $scrollUp.on('click', function (evt) {
      $('html, body').animate({scrollTop: 0}, 50);
      evt.preventDefault();
    });
  }
  scrollToTop();
  
/* ==========================================================================
   When document is loading, do
   ========================================================================== */
  var varWindow = $(window);
  varWindow.on('load', function() {
    stylePreloader();
  });

})(window.jQuery);
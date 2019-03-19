$(function () {

    var swiper = new Swiper('#swiper-container', {
        pagination: '.swiper-pagination',
        paginationClickable: true,
        spaceBetween: 30,
        centeredSlides: false,
        autoplay: 2500,
        autoplayDisableOnInteraction: false
    })


    $('.list li').mouseover(function () {
        $(this).children('.subNav').css('display','block')
    })
       $('.list li').mouseout(function () {
        $(this).children('.subNav').css('display','none')
    })


})
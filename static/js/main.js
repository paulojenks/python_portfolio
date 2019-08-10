$(document).ready(function () {
    //find div
    let div = $('div.nav-menu');
    //find ul width
    let liNum = $(div).find('img').length;
    let speed = 500;
    let containerWidth = 600;
    let itemWidth = 212;
    //Remove scrollbars
    if (liNum < 3) {
        $('#left-arrows').attr("src", "");
        $('#right-arrows').attr("src", "");
    }
    $(div).css({overflow: 'hidden'});
    $('div.right-arrow').click(function (e) {
        if (($(div).scrollLeft() + itemWidth) < (liNum * itemWidth)) {
            $(div).animate({
                scrollLeft: '+=' + itemWidth
            }, speed);
        }
    });
    $('div.left-arrow').click(function (e) {
        if (($(div).scrollLeft() + containerWidth) > containerWidth) {
            $(div).animate({
                scrollLeft: '-=' + itemWidth
            }, speed);
        }
    });

    let slideIndex = 1;
    showDivs(slideIndex);

    $('.nav-menu-item').mouseenter(onHover()).mouseleave(offHover());
    function onHover() {
        let srcId = event.srcElement.id;
        let locId = "images/" + srcId + "-white.jpg";
        $("#" + srcId).attr('src', '{{ baseURL }}' + locId);
    }

    function offHover() {
        let srcId = event.srcElement.id;
        let locId = "images/" + srcId + ".jpg";
        $("#" + srcId).attr('src', '{{ baseURL }}' + locId);
    }


    function currentDiv(n) {
        showDivs(slideIndex = n);
    }

    function showDivs(n) {
        let i;
        let x = document.getElementsByClassName("display-img");
        let dots = document.getElementsByClassName("nav-menu-item");
        if (n > x.length) {
            slideIndex = 1
        }
        if (n < 1) {
            slideIndex = x.length
        }
        for (i = 0; i < x.length; i++) {
            x[i].style.display = "none";
        }
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" w3-opacity-off", "");
        }
        x[slideIndex - 1].style.display = "block";
        dots[slideIndex - 1].className += " w3-opacity-off";
    }
});
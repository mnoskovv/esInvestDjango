var index = -1;

$(document).ready(function () {
    $('.ham_btn').on('click', function () {
        $('.ham_line1').toggleClass('active_hl1');
        $('.ham_line2').toggleClass('active_hl2');
        $('.ham_line3').toggleClass('active_hl3');
        $('.mobile_menu').toggleClass('active');
    });

    checkSelected();

    $('.curency_btn').on('click', function () {
        if ($(this).hasClass('active')) {
            return;
        }
        $('.curency_chb').prop('checked', false);
        $('#' + $(this).attr('for')).prop('checked', true);

        checkSelected();
    });

    $('.tab_arrow').on('click', function () {
        var tab_class = '.switcher' + $(this).attr('table-num');
        var tab_pane = '.tab-pane' + $(this).attr('table-num');
        for (var i = 0; i < $(tab_class).length; i++) {
            if ($(tab_class).eq(i).hasClass('active')) {
                index = i;
                break;
            }
        }

        if ($(this).attr('direction') === 'next') {
            if (index < $(tab_class).length - 1) {
                index++;
            } else {
                index = 0;
            }
        } else {
            if (index > 0) {
                index--;
            } else {
                index = $(tab_class).length - 1;
            }
        }

        if (index > -1) {
            for (var i = 0; i < $(tab_class).length; i++) {
                if (i === index) {
                    $(tab_class).eq(i).addClass('active');
                    $(tab_pane).eq(i).removeClass('fade');
                    $(tab_pane).eq(i).addClass('active');                    
                } else {
                    $(tab_class).eq(i).removeClass('active');
                    $(tab_pane).eq(i).removeClass('active');
                    $(tab_pane).eq(i).addClass('fade');
                }
            }
        }
        return false;
    });
    
    var c4 = $('.progres');

    c4.circleProgress({
        startAngle: Math.PI * 2,
        value: 0.75,
        lineCap: 'round',
        emptyFill: '#e5e6f2',
        size: 165,
        fill: {color: '#000c81'}
    });
});

function checkSelected() {
    for (var i = 0; i < $('.curency_chb').length; i++) {
        if ($('.curency_chb').eq(i).prop('checked')) {
            $('.curency_btn').eq(i).addClass('active');
        } else {
            $('.curency_btn').eq(i).removeClass('active');
        }
    }
}


var lipicam = {};
(function (module) {

    'use strict';

    var timeoutId;
    var timeout = 500;
    var camElm;
    var camActionSelector = '#cam-action';
    var status = false;

    function update() {
        camElm.src = "/cam/stream?" + Date.now();
        timeoutId = setTimeout(update, timeout)
    }

    module.toggle = function () {
        if (status) {
            module.stop();
        } else {
            module.start();
        }
    };

    module.start = function () {
        if (status) {
            return;
        }
        status = true;
        update();
        $(camActionSelector).text('stop');
    };

    module.stop = function () {
        if (!status) {
            return;
        }
        clearTimeout(timeoutId);
        status = false;
        $(camActionSelector).text('start');
    };

    module.init = function () {
        camElm = document.querySelector('#cam');
        module.start();
    };

})(lipicam);

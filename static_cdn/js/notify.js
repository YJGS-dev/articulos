const notify = new Notyf({
    duration:10000,
    position: {
        x: 'right',
        y: 'top',
    },
    types: [
        {
            type: 'primary',
            background: '#c600d0',
            dismissible: false
        },
        {
            type: 'info',
            background: '#646ad0',
            dismissible: false
        },
        {
            type: 'success',
            background: '#4ad040',
            dismissible: false
        },
        {
            type: 'warning',
            background: '#d0c21b',
            dismissible: false
        },
        {
            type: 'error',
            background: '#d05454',
            dismissible: false
        },
    ]
});

notification = {
    primary: function (message) {
        notify.open({
            type: 'primary',
            message: message
        });
    },
    info: function (message) {
        notify.open({
            type: 'info',
            message: message
        });
    },
    success: function (message) {
        notify.open({
            type: 'success',
            message: message
        });
    },
    warning: function (message) {
        notify.open({
            type: 'warning',
            message: message
        });
    },
    error: function (message) {
        notify.open({
            type: 'error',
            message: message
        });
    }
};
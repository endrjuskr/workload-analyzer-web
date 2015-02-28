$(document).ready(function () {
    History.pushState({init: true}, null, null);
});

function render(py_function, params) {
    var stateObj = {init: false, render_fun: py_function.toString(), params: params};
    History.pushState(stateObj, null, null);
}

History.Adapter.bind(window, 'statechange', function () {
    var hist_state = History.getState().data;
    if (hist_state) {
        if (hist_state.init)
            Dajaxice.app.dashboard_ajax(render_response, EMPTY_DIC);
        else {
            var startBody = hist_state.render_fun.indexOf('{') + 1;
            var endBody = hist_state.render_fun.lastIndexOf('}');
            var startArgs = hist_state.render_fun.indexOf('(') + 1;
            var endArgs = hist_state.render_fun.indexOf(')');
            var render_fun = new Function(hist_state.render_fun.substring(startArgs, endArgs), hist_state.render_fun.substring(startBody, endBody));
            render_fun(render_response, hist_state.params);
        }
    }
    else
        console.log("Dotarłeś do końca internetu");
});

function render_response(data) {
    if (data.status = OK_RETURN_CODE)
        $("#main_content").html(data.view);
    else {
        //TODO add alert API
        alert(data.view);
    }
}
function submit_new_execution_comment() {
    render(Dajaxice.workload.add_execution_comment_submit, {'form': $('#comment_form').serialize(true)});
}

function submit_new_workload_comment(id) {
    render(Dajaxice.workload.add_workload_comment_submit, {'form': $('#comment_form').serialize(true), 'workload_id': id});
}


function submit_edit_child(child_id) {
    render(Dajaxice.app.edit_child_submit, {'form': $('#piggy_form').serialize(true), 'child_id': child_id});
}

function remove_child(id) {
    render(Dajaxice.app.remove_child, {'child_id': id});
}

function new_execution_comment(id) {
    render(Dajaxice.workload.add_execution_comment_form, {'execution_id': id});
}

function view_workload(id) {
    render(Dajaxice.workload.view_workload, {'workload_id': id});
}

function view_workloads() {
    var searchIDs = $("input:checkbox:checked").map(function(){
      return $(this).val();
    }).get();
    if(searchIDs.length == 0) {
        return;
    }
    render(Dajaxice.workload.view_workloads, {'workloads': searchIDs});
}


function new_workload_comment(id) {
    render(Dajaxice.workload.add_workload_comment_form, {'workload_id': id});
}
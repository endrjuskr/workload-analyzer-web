function submit_new_child() {
    render(Dajaxice.app.new_child_submit, {'form': $('#piggy_form').serialize(true)});
}
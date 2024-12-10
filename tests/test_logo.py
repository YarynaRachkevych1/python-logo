from python_logo import run


def test_forward():
    forward_input = "forward 100"
    forward_alias_input = "fd 100"
    forward_response = [{"name": "forward", "value": 100}]
    assert list(run(forward_input)) == forward_response
    assert list(run(forward_alias_input)) == forward_response


def test_backward():
    backward_input = "backward 100"
    backward_alias_input = "bk 100"
    backward_response = [{"name": "backward", "value": 100}]
    assert list(run(backward_input)) == backward_response
    assert list(run(backward_alias_input)) == backward_response


def test_left():
    left_input = "left 90"
    left_alias_input = "lt 90"
    left_response = [{"name": "left", "value": 90}]
    assert list(run(left_input)) == left_response
    assert list(run(left_alias_input)) == left_response


def test_right():
    right_input = "right 90"
    right_alias_input = "rt 90"
    right_response = [{"name": "right", "value": 90}]
    assert list(run(right_input)) == right_response
    assert list(run(right_alias_input)) == right_response


def test_showturtle():
    showturtle_input = "showturtle"
    showturtle_alias_input = "st"
    showturtle_response = [{"name": "showturtle"}]
    assert list(run(showturtle_input)) == showturtle_response
    assert list(run(showturtle_alias_input)) == showturtle_response


def test_hideturtle():
    hideturtle_input = "hideturtle"
    hideturtle_alias_input = "ht"
    hideturtle_response = [{"name": "hideturtle"}]
    assert list(run(hideturtle_input)) == hideturtle_response
    assert list(run(hideturtle_alias_input)) == hideturtle_response


def test_penup():
    penup_input = "penup"
    penup_alias_input = "pu"
    penup_response = [{"name": "penup"}]
    assert list(run(penup_input)) == penup_response
    assert list(run(penup_alias_input)) == penup_response


def test_pendown():
    pendown_input = "pendown"
    pendown_alias_input = "pd"
    pendown_response = [{"name": "pendown"}]
    assert list(run(pendown_input)) == pendown_response
    assert list(run(pendown_alias_input)) == pendown_response


def test_repeat():
    repeat_input = "repeat 4 [forward 100 right 90]"
    repeat_response = [
        {"name": "forward", "value": 100},
        {"name": "right", "value": 90},
        {"name": "forward", "value": 100},
        {"name": "right", "value": 90},
        {"name": "forward", "value": 100},
        {"name": "right", "value": 90},
        {"name": "forward", "value": 100},
        {"name": "right", "value": 90},
    ]
    assert list(run(repeat_input)) == repeat_response


def test_if():
    if_true_input = "if true [forward 100]"
    if_true_response = [{"name": "forward", "value": 100}]
    if_false_input = "if false [forward 100]"
    if_false_response = []
    assert list(run(if_true_input)) == if_true_response
    assert list(run(if_false_input)) == if_false_response


def test_else():
    else_input = "if false [forward 100] else [right 90]"
    else_response = [{"name": "right", "value": 90}]
    assert list(run(else_input)) == else_response


def test_variables():
    variables_input = "make var 100 forward :var"
    variables_response = [{"name": "forward", "value": 100}]
    variables_expr_input = "make var 20 + 20 + 20 forward :var"
    variables_expr_response = [{"name": "forward", "value": 60}]
    assert list(run(variables_input)) == variables_response
    assert list(run(variables_expr_input)) == variables_expr_response


def test_all():
    logo_input = """
        forward 20
        fd 30
        backward 40
        bk 50
        left 60
        lt 70
        right 80
        rt 90
        hideturtle
        ht
        showturtle
        st
        penup
        pu
        pendown
        pd
        make varrpt 4
        make varfd 100
        repeat :varrpt [forward :varfd right 90]
        if true [forward 100]
        if false [forward 100]
    """
    logo_response = [
        {"name": "forward", "value": 20},
        {"name": "forward", "value": 30},
        {"name": "backward", "value": 40},
        {"name": "backward", "value": 50},
        {"name": "left", "value": 60},
        {"name": "left", "value": 70},
        {"name": "right", "value": 80},
        {"name": "right", "value": 90},
        {"name": "hideturtle"},
        {"name": "hideturtle"},
        {"name": "showturtle"},
        {"name": "showturtle"},
        {"name": "penup"},
        {"name": "penup"},
        {"name": "pendown"},
        {"name": "pendown"},
        {"name": "forward", "value": 100},
        {"name": "right", "value": 90},
        {"name": "forward", "value": 100},
        {"name": "right", "value": 90},
        {"name": "forward", "value": 100},
        {"name": "right", "value": 90},
        {"name": "forward", "value": 100},
        {"name": "right", "value": 90},
        {"name": "forward", "value": 100},
    ]
    assert list(run(logo_input)) == logo_response

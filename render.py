from flask import render_template, g, session

ltabs=[
]

rtabs=[
]

def render(template, **kwargs):
    kwargs['g'] = g
    if g.user_id is not None:
        kwargs['ltabs'] = ltabs
        kwargs['rtabs'] = rtabs
        kwargs['current_tab'] = ''
    return render_template(template, **kwargs)


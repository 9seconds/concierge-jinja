# -*- coding: utf-8 -*-


import concierge_jinja.templater


TEMPLATE = """\
lalala

{% for i in range(2) %}
i - {{ i }}
{% endfor %}
"""

RESULT = """\
lalala


i - 0

i - 1
"""


def test_name():
    assert concierge_jinja.templater.Jinja2Templater.name == "jinja2"


def test_render():
    tpl = concierge_jinja.templater.Jinja2Templater()

    assert tpl.render(TEMPLATE) == RESULT

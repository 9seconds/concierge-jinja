# -*- coding: utf-8 -*-


import concierge.templater
import jinja2


class Jinja2Templater(concierge.templater.Templater):

    name = "jinja2"

    def render(self, content):
        env = jinja2.Environment()
        template = env.from_string(content)
        content = template.render()

        return content

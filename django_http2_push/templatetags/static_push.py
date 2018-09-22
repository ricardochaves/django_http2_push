from django import template
from django.templatetags.static import StaticNode

register = template.Library()


class StaticPushNode(StaticNode):
    def render(self, context):
        rendered = url = super(StaticPushNode, self).render(context)

        if not url:
            url = self.url(context)

        if url:
            update_push_list_urls(context, url)

        return rendered


@register.tag("static_push")
def do_static_push(parser, token):
    return StaticPushNode.handle_token(parser, token)


def update_push_list_urls(context, url):

    request = context.get("request")
    if request:
        if not hasattr(request, "push_list"):
            request.push_list = set()
        request.push_list.add(url)

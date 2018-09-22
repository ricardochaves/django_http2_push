from django.utils.deprecation import MiddlewareMixin


def _build_header(asset_names):
    asset_template = "<{asset_path}>; rel=preload"
    return ", ".join(asset_template.format(asset_path=asset_name) for asset_name in asset_names)


def get_link_header_from_response(response):
    header_links = response.get("Link", "")
    if header_links:
        header_links += ", "
    return header_links


class PushHttp2Middleware(MiddlewareMixin):
    @staticmethod
    def process_response(request, response):

        if not getattr(request, "push_list", None):
            return response

        header_links = get_link_header_from_response(response)

        header_links += _build_header(request.push_list)

        response["Link"] = header_links

        return response

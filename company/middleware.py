import logging

logger = logging.getLogger('django')

class LogHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.log_request(request)

        response = self.get_response(request)

        self.log_response(request, response)

        return response

    def log_request(self, request):
        request_headers = self.format_headers(request.headers)
        logger.info(f"\nHTTP Request: {request.method} {request.get_full_path()}")
        logger.info("\tRequest Headers:\n%s", request_headers)

        if request.method == 'POST':
            post_data = request.POST if request.POST else request.body.decode('utf-8')
            logger.info("POST Data:\n\t\t%s", post_data)

    def log_response(self, request, response):
        response_headers = self.format_headers(response.headers)
        logger.info(f"\nHTTP Response: {response.status_code} for {request.method} {request.get_full_path()}")
        logger.info("\tResponse Headers:\n%s", response_headers)

    def format_headers(self, headers):
        return "\n".join([f"\t\t{key}: {value}" for key, value in headers.items()])
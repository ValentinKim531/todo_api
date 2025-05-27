from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from threading import Thread
from .astanahub_scraper import scrape_companies
import os


class ScrapeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
        Thread(target=scrape_companies).start()
        return Response({"status": "extraction in background"})

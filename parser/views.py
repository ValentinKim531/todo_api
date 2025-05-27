from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from threading import Thread
from .astanahub_scraper import scrape_companies
from rest_framework.generics import ListAPIView
from .models import AstanaHubCompany
from .serializers import AstanaHubCompanySerializer
import os


class ScrapeView(APIView):

    def post(self, request):
        os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

        Thread(target=scrape_companies).start()

        return Response(
            {
                "status": "started",
                "message": "Извлечение данных началось. "
                           "Дождитесь завершения (примерно 5–10 секунд) и "
                           "проверьте /admin или GET /parser/companies/",
                "estimated_duration_sec": 10,
            },
            status=status.HTTP_202_ACCEPTED,
        )


class CompanyListView(ListAPIView):
    queryset = AstanaHubCompany.objects.all().order_by("created_at")[:10]
    serializer_class = AstanaHubCompanySerializer

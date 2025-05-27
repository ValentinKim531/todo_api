import os
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from threading import Thread
from .astanahub_scraper import scrape_companies
from rest_framework.generics import ListAPIView
from .models import AstanaHubCompany
from .serializers import AstanaHubCompanySerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny


class ScrapeView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(operation_summary="Извлечение компаний с сайта Astana Hub")
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
    permission_classes = [AllowAny]

    @swagger_auto_schema(operation_summary="Результаты парсинга компаний с Astana Hub")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

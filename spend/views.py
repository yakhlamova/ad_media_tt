from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework import status

from .models import SpendStatistic
from .serializers import SpendSerializer


class SpendStatisticsView(APIView):
    def get(self, request):
        queryset = SpendStatistic.objects.values("date", "name").annotate(
            total_spend=Sum("spend"),
            total_impressions=Sum("impressions"),
            total_clicks=Sum("clicks"),
            total_conversion=Sum("conversion"),
            total_revenue=Sum("revenuestatistic__revenue"),
        )

        serializer = SpendSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

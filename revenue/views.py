from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework import status

from .models import RevenueStatistic
from .serializers import RevenueSerializer


class RevenueStatisticView(APIView):
    def get(self, request):
        queryset = RevenueStatistic.objects.values("date", "name").annotate(
            total_revenue=Sum("revenue"),
            #
            total_spend=Sum("spend__spend"),
            total_impressions=Sum("spend__impressions"),
            total_clicks=Sum("spend__clicks"),
            total_conversion=Sum("spend__conversion"),
        )

        serializer = RevenueSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

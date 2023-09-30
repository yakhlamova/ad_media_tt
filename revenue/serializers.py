from rest_framework import serializers


class RevenueSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    date = serializers.DateField()
    revenue_total = serializers.DecimalField(max_digits=9, decimal_places=2)
    spend_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    impressions_total = serializers.IntegerField()
    clicks_total = serializers.IntegerField()
    conversion_total = serializers.IntegerField()

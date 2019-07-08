from charting.models import BondYield
from rest_framework import serializers


class BondYieldSerializer(serializers.ModelSerializer):
  class Meta:
    model = BondYield
    fields = '__all__'

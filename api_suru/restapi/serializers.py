from restapi.models import Aritcle
from rest_framework import serializers

class AritcleSerializer(serializers.ModelSerializer):
    # Model serilializer

    class Meta:
        model=Aritcle
        fields=['id','title','authorname','email','date']




    """
    #Normal serializer
    title = serializers.CharField(max_length=200)
    authorname = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=20)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Aritcle.objects.create(validated_data)

    def update(self, instance, validated_datas):
        instance.title = validated_datas.get('title',instance.title)
        instance.authorname = validated_datas.get('authorname',instance.authorname)
        instance.email = validated_datas.get('email',instance.email)
        instance.date = validated_datas.get('date',instance.date)
        instance.save()
        return instance

    """


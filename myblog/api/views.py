
from rest_framework import viewsets

from .models import Articles
from .serializers import ArticlesSerializer
# Create your views here.

class AriticleAPIViewSet(viewsets.ModelViewSet):
    """記事モデルのCRUD用APIクラス"""

    serializer_class = ArticlesSerializer
    queryset = Articles.objects.all()

    # def list(self):
    #     super().list()



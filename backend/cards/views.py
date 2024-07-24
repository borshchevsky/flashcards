from rest_framework.viewsets import ModelViewSet

from cards.models import Deck, Card
from cards.serializers import DeckSerializer, CardSerializer


class DeckView(ModelViewSet):
    serializer_class = DeckSerializer
    queryset = Deck.objects.all()


class CardView(ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

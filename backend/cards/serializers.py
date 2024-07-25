from rest_framework import serializers

from cards.models import Deck, Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'card_deck',
            'front',
            'back'
        )


class DeckSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, source='card_set', required=False)

    class Meta:
        model = Deck
        fields = (
            'id',
            'name',
            'cards'
        )

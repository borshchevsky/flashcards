from rest_framework.routers import DefaultRouter

from cards.views import DeckView, CardView

router = DefaultRouter()
router.register('decks', DeckView)
router.register('cards', CardView)

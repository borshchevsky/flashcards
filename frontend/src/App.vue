<template>
  Decks:
  <div v-for="deck in data" :key="deck.id">
    <p href="">{{ deck.name }}</p>
    <div v-for="card in deck.cards" :key="card.id">
      <div class="cards-list" @click.stop="setCard(card.id)">
        {{ card.id }}
      </div>
    </div>
  </div>
  <CardView :cardId="currentCardId"/>
</template>

<script setup>

import { onMounted, ref } from "vue";
import CardView from '@/components/CardView'
const data = ref();
const currentCardId = ref();

function setCard(cardId) {
  console.log(cardId)
  currentCardId.value = cardId;
}

onMounted(async () => {
 data.value = await (await fetch('http://localhost:8000/api/v1/decks/')).json();
})

</script>


<style>
.cards-list:hover {
  cursor: default;
}
</style>
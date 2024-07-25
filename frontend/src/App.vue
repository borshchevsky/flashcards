<template>
  <div class="main">
    <div class="row">
      <div class="navbar">
        <a class="logo" href="#">FlashCards</a>
        <router-link to="decks">Decks</router-link>
        <a href="#">Settings</a>
        <router-link to="about">About</router-link>
        <a href="#">Log In</a>
        <a href="#">Register</a>
      </div>
    </div>
    <div class="row">
      <router-view/>
    </div>
  </div>
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

.main {
  margin: 10px;
  background: #fdfaff;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.row {
  display: flex;
  justify-content: center;
  flex-direction: row;
}

.navbar a {
  margin: 40px;
}

.navbar {
  flex-direction: row;
}

.logo {
  font-size: 36px;
  font-weight: bold;
  text-decoration: none;
  color: black;
}
</style>
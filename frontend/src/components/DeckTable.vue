<template>
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Cards</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="deck in decks" :key="deck.id">
         <td>{{ deck.name }}</td>
         <td>{{ deck.cards.length }}</td>
         <td><a href="#">Learn</a></td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
import { onMounted, ref } from "vue";

const decks = ref();

onMounted(async () => {
  decks.value = await (await fetch('http://localhost:8000/api/v1/decks/')).json();
  console.log(decks.value)
})
</script>

<style scoped>
        table {
            border-collapse: collapse;
            margin: 255px 0;
            font-size: 14px;
            font-family: sans-serif;
            min-width: 400px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
            border-radius: 5px;
        }

        thead tr {
            background-color: lightgray;
            text-align: left;
        }

        th {
            font-size: 16px;
        }

        th:first-child {
            border-radius: 5px 0 0 0;
        }

        th:last-child {
            border-radius: 0 5px 0 0;
        }

        th, td {
            padding: 12px 15px;
        }

        tbody tr {
            border-bottom: 1px solid #dddddd;
        }

        table a {
            text-decoration: none;
        }
</style>
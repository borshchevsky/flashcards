<template>
  <div class="container">
    <div>
      Front: {{ card && card.front }}
    </div>
    <div>
      Back: {{ card && card.back }}
    </div>
  </div>
</template>

<script setup>
import { defineProps, ref, watch } from 'vue';

const props = defineProps({ cardId: String });
const card = ref();

watch(
    () => props.cardId,
    async () => {
      card.value = await (await fetch(`http://localhost:8000/api/v1/cards/${props.cardId}`)).json()
    }
)

</script>

<style scoped>
  .container   {
    flex-direction: column;
  }
</style>
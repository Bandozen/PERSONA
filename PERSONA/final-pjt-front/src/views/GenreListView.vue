<template>
  <div>
    <h1>원하시는 장르를 선택해주세요!</h1>
      <GenreItem />
  </div>
</template>

<script>
import GenreItem from "@/components/GenreItem.vue";

export default {
  components: {
    GenreItem,
  },
};
</script>

<style></style>

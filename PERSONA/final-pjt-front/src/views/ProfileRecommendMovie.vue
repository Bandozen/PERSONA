<template>
  <div>
    <div class="card">
      <router-link :to="{ name: 'MovieDetail', params: { id: movie.pk } }">
        <img :src="`https://image.tmdb.org/t/p/original${movie['fields'].poster_path}`" class="img-fluid image zoom">
      </router-link>
    </div>
  </div>
</template>
  
<script>

  export default {
    name: "ProfileRecommendMovie",
    props: {
      movie: {type: Object,
      },
    },
    data() {
      return {
        toggle: false,
      }
    },
    methods: {
      openModal() {
        // console.log("hi")
        this.toggle = !this.toggle
      },
    },
  
  }
</script>
  
<style scoped>
/* @import "~@egjs/flicking-plugins/dist/arrow.css"; */
  .card .image {
    height: 350px;
    width: 250px;
    object-fit: cover;
  }
  
  .zoom {
    transition: transform .2s; /* Animation */
    margin: 0 auto;
  }
  
  .zoom:hover {
    transform: scale(1.2);
  }
</style>
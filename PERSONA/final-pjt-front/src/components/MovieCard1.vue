<template>
  <div>
    <h1 style="text-align: left; font-weight:bold; color: #00788D; margin-left: 30px">
      페르소나 최신 작품을 만나보세요!
    </h1>
    <div id="carouselNowPlaying" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div
          class="carousel-item"
          v-for="(group, index) in groupMovies"
          :key="index"
          :class="{ active: index === 0 }"
        >
          <div class="row">
            <div class="col-3" v-for="movie in group" :key="movie.id">
              <button class="btn btn-outline-dark">
                <router-link
                  :to="{ name: 'MovieDetail', params: {'id': movie.id } }"
                >
                  <img
                    :src="getImageUrl(movie.poster_path)"
                    class="d-block w-100"
                    :alt="movie.title"
                    style="height: 20rem"
                  />
                </router-link>
              </button>
              <h6>{{ movie.title }}</h6>
            </div>
          </div>
        </div>
      </div>
      <a
        class="carousel-control-prev"
        href="#carouselNowPlaying"
        role="button"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </a>
      <a
        class="carousel-control-next"
        href="#carouselNowPlaying"
        role="button"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </a>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "movieCard1",
  data() {
    return {
      movieTitle: "",
      movieContent: "",
      movieVideo: "",
    };
  },
  methods: {
    updateInfo(movie) {
      // console.log(movie)
      const videoUrl = `https://api.themoviedb.org/3/movie/${movie.id}/videos?api_key=a51700c7b5c0eac2db0ce7a959dcc750`;
      this.movieTitle = movie.title;
      this.movieContent = movie.overview;

      axios({
        method: "get",
        url: videoUrl,
      })
        .then((res) => {
          // console.log(res.data.results)
          const videoKey = res.data.results[0].key;
          this.movieVideo =
            "https://www.youtube.com/embed/" +
            videoKey +
            "?mute=1&autoplay=1&rel=0&controls=0&showinfo=0";
          //console.log(this.movieVideo)
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getImageUrl(posterPath) {
      if (posterPath) {
        return "https://image.tmdb.org/t/p/w220_and_h330_face/" + posterPath;
      }
    },
  },
  computed: {
    newMovieList() {
      return this.$store.state.newMovieList;
    },
    groupMovies() {
      const movieSize = 4;
      const sizes = [];
      for (
        let i = 0;
        i < this.$store.state.newMovieList.length;
        i += movieSize
      ) {
        sizes.push(this.$store.state.newMovieList.slice(i, i + movieSize));
      }
      return sizes;
    },
  },
};
</script>

<style >
h6 {
  color: white;
}
</style>

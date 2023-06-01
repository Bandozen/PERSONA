<template>
  <div class="justify-content-center">
    <div class="jb-box">
      <iframe
        class="mainVideo"
        width="100%"
        height="500"
        src="https://www.youtube.com/embed/oSqK_v6zPoM?mute=1&autoplay=1&rel=0&controls=0&showinfo=0"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      ></iframe>
      <div class="jb-text">
        <p>오펜하이머</p>
        <br />
        <p style="font-size: 15px">
          "나는 이제 죽음이요, 세상의 파괴자가 되었도다." <br />
          세계 최초의 핵무기 개발 프로젝트인 맨해튼 계획. <br />
          잇따른 절망과 죄책감은 그를 더욱 궁지로 내몰리게 만든다. <br />
          잔혹한 세상에서 살아남으려면 그들과 함께 미쳐버리는 것이 나은 걸까.
          <br />
          비운의 천재 물리학자의 고뇌가 시작된다.
        </p>
      </div>
    </div>
    <div class="contentbox">
      <MovieCard1 />
      <hr />
      <MovieCard2 />
    </div>
  </div>
</template>

<script>
import MovieCard1 from "@/components/MovieCard1.vue";
import MovieCard2 from "@/components/MovieCard2.vue";

export default {
  name: "MovieView",
  methods: {
    getMovies() {
      this.$store.dispatch("getMovies");
    },
    getPopularMovies() {
      this.$store.dispatch("getPopularMovies");
    },
  },
  components: {
    MovieCard1,
    MovieCard2,
  },
  created() {
    this.getMovies();
    this.getPopularMovies();
  },
  computed: {
    newMovieList() {
      return this.$store.state.newMovieList;
    },
    popularMovieList() {
      return this.$store.state.popularMovieList;
    },
  },
};
</script>

<style>
.contentbox {
  background-color: black;
}

.jb-box {
  width: 100%;
  height: 0;
  overflow: hidden;
  margin: 0px auto;
  position: relative;
  padding-bottom: 56.25%;
}

.jb-text {
  position: absolute;
  top: 50%;
  width: 100%;
  background-color: transparent;
}

.jb-text p {
  margin-top: -24px;
  margin-left: 30px;
  text-align: left;
  font-size: 40px;
  color: #ffffff;
  background-color: transparent;
}

.mainVideo {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>

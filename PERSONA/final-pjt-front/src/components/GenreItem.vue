<template>
  <div>
    <h3>{{ this.movie_genre }} 영화 목록</h3>
    <div class="btn-group">
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(1, '전체')">전체</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(12, '모험')">모험</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(14, '판타지')">판타지</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(16, '애니메이션')"
          >애니메이션</a
        >
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(18, '드라마')">드라마</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(27, '공포')">공포</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(28, '액션')">액션</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(35, '코미디')">코미디</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(36, '역사')">역사</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(37, '서부')">서부</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(53, '스릴러')">스릴러</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(80, '범죄')">범죄</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(99, '다큐멘터리')"
          >다큐멘터리</a
        >
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(878, 'SF')">SF</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(9648, '미스터리')">미스터리</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(10402, '음악')">음악</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(10749, '로맨스')">로맨스</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(10751, '가족')">가족</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(10752, '전쟁')">전쟁</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(10770, 'TV 영화')">TV 영화</a>
      </button>
    </div>
    <hr />
    <div v-if="sortBtn" class="main">
      <template v-if="genres.length">
        <div class="row row-cols-1 row-cols-md-3 g-4 sub">
          <div v-for="genre in genres" :key="genre.id">
            <div class="col main">
              <div
                class="card"
                style="width: 400px; height: 450px; margin: 50px"
              >
                <router-link
                  style="text-decoration: none; color: inherit"
                  :to="{ name: 'MovieDetail', params: { id: genre.id } }"
                >
                  <img
                    :src="getImageUrl(genre.poster_path)"
                    class="card-img-top"
                    alt="이미지를 표시할 수 없습니다."
                    style="width: 100%; height: 450px"
                  />
                  <div class="card-body">
                    <h5 class="card-title">{{ genre.title }}</h5>
                  </div>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </template>
      <template v-else>
        <h3>
          해당 영화 정보가 없습니다. 빠른 시일 내에 데이터를 제공해드리겠습니다.
        </h3>
      </template>
    </div>
          <div style="display: flex; justify-content: center; margin: 50px">
            <button
              type="button"
              @click="appendGenre()"
              :disabled="this.dataFull === true"
              :class="{ disabled: dataFull }"
              style="justify-content: center"
            >
              더 보기 ({{ cntGenre }}/{{ totalGenre }})
            </button>
          </div>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/v1";

export default {
  data() {
    return {
      movies: {},
      genreAll: {},
      genres: [],
      movie_genre: "",
      totalGenre: 0,
      cntGenre: 6,
      dataFull: false,
    };
  },
  created() {
    this.recommendMovie(1);
  },
  methods: {
    getMovies() {
      axios({
        method: "get",
        url: `${API_URL}/moviegenre`,
      }).then((res) => {
        console.log(res.data);
        this.movies = res.data;
      });
    },
    recommendMovie(num) {
      axios({
        method: "get",
        url: `${API_URL}/${num}/sort`,
      }).then((res) => {
        //console.log(res.data);
        this.genreAll = res.data;
        let data = [];
        for (var i = 0; i < this.cntGenre; i++) {
          data.push(res.data[i]);
        }
        //console.log(data)
        this.genres = data;
        this.totalGenre = res.data.length;
        console.log(this.totalGenre);
      });
    },
    appendGenre() {
      if (this.cntGenre < this.totalGenre) {
        this.cntGenre += 6;
        let data = [];
        for (var i = 0; i < this.cntGenre; i++) {
          data.push(this.genreAll[i]);
        }
        this.genres = data;
      } else {
        this.dataFull = true;
        alert("모든 데이터를 출력했습니다!");
      }
    },
    sortBtn(num, movie_genre) {
      this.movie_genre = movie_genre;
      axios({
        method: "get",
        url: `${API_URL}/${num}/sort`,
      }).then((res) => {
        this.genreAll = res.data;
        let data = [];
        for (let i = 0; i < this.cntGenre && i < this.genreAll.length; i++) {
          data.push(this.genreAll[i]);
        }
        this.genres = data;
        this.totalGenre = this.genreAll.length;
      });
    },
    getImageUrl(posterPath) {
      if (posterPath) {
        return "https://image.tmdb.org/t/p/w220_and_h330_face/" + posterPath;
      }
    },
  },
};
</script>

<style>
.main {
  display: flex;
  justify-content: center;
}
</style>

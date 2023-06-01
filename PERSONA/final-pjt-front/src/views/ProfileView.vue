<template>
  <div class="row py-5 px-4">
    <div class="col-sm-8">
      <div class="col">
        <div class="">
          <div class="d-flex">
            <div class="name" style="height:250px; width:250px">
              <div class="">
                <div class="about">
                  <div class="profile" style="text-align:center">
                    <img src="@/assets/arsenal.png" alt="..." width="180" >
                  </div>
                </div>
              </div>
            </div>
            <div style="margin-left: 30px; margin-top: 20px;">
              <div class="d-flex" style="margin-bottom: 35px;">
                <div style="font-size:23px; font-weight:bold; margin-right: 50px; margin-top: 15px;">😃 {{ user_info[0].username }}</div>
                <div class="d-flex">
                  <div>
                    <div style="text-align:center; font-weight:bold; ">{{ user_like_movies.length}}</div>
                    <div style="margin-top:5px; margin-right:20px; ">❤️좋아요를 누른 영화</div>
                  </div>
                </div>
              </div>
              <div>
                <div style="margin-top: 10px; text-align: left; color: #95E0C8;">⚽ MBTI : {{ user_info[0].mbtis }}</div>
              </div>
            </div>
          </div>
          <div class="py-4 px-4">
            <div class="d-flex align-items-center justify-content-between mb-3">
              <h5 style="font-weight:bold; margin-left:10px; color: pink; ">❤️좋아요를 누른 영화</h5>           
            </div>
            <div class="p-4">
              <div class="row">
                <div v-if="user_like_movies.length > 0" class="container-fluid">
                  <div id="movieCarousel" class="carousel slide" data-bs-ride="carousel">
                    <ol class="carousel-indicators">
                      <li data-bs-target="#movieCarousel" v-for="(movieGroup, index) in Math.ceil(user_like_movies.length / 4) || 1" :key="index" :data-bs-slide-to="index" :class="{ active: index === 0 }"></li>
                    </ol>
                    <div class="carousel-inner">
                      <template v-if="user_like_movies.length <= 4">
                        <div class="carousel-item active">
                          <div class="row justify-content-center">
                            <div v-for="movie in user_like_movies" :key="movie.id" class="col-md-3">
                              <div class="d-flex justify-content-center">
                                <ProfileMovie :movie="movie"></ProfileMovie>
                              </div>
                            </div>
                          </div>
                        </div>
                      </template>
                      <template v-else>
                        <div v-for="(movieGroup, index) in user_like_movies.reduce((acc, cur, index) => {
                            const group = Math.floor(index / 4);
                            if (!acc[group]) acc[group] = [];
                            acc[group].push(cur);
                            return acc;
                          }, [])"
                          :key="index"
                          class="carousel-item"
                          :class="{ active: index === 0 }"
                        >
                          <div class="row justify-content-center">
                            <div v-for="movie in movieGroup" :key="movie.id" class="col-md-3">
                              <div class="d-flex justify-content-center">
                                <ProfileMovie :movie="movie"></ProfileMovie>
                              </div>http://localhost:8080/profile#movieCarousel
                            </div>
                          </div>
                        </div>
                      </template>
                    </div>
                    <a class="carousel-control-prev" href="#movieCarousel" role="button" data-bs-slide="prev">
                      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                      <span class="visually-hidden">Previous</span>
                    </a>
                    <a class="carousel-control-next" href="#movieCarousel" role="button" data-bs-slide="next">
                      <span class="carousel-control-next-icon" aria-hidden="true"></span>
                      <span class="visually-hidden">Next</span>
                    </a>
                  </div>
                </div>
                <div v-else class="container-fluid">
                  <h6 style="background-color: #FFFFFF; color: red;">좋아요를 한 영화가 없습니다.</h6>
                </div>
              </div>
            </div>
            <div class="d-flex align-items-center justify-content-between mb-3" style="margin-top:30px">
              <h5 style="font-weight:bold; margin-left:10px; color: pink;">❤️좋아요를 누른 영화로 추천 (없으면 랜덤추천)</h5>
            </div>
            <div class="p-4">
              <div class="row">
                <div v-if="user_like_recommends[0]" class="container-fluid">
                  <div id="recommendCarousel" class="carousel slide" data-bs-ride="carousel">
                    <div class="carousel-inner">
                      <div v-for="(movieGroup, index) in Math.ceil(user_like_recommends[0].length / 4)" :key="index" :class="['carousel-item', { active: index === 0 }]">
                        <div class="row justify-content-center">
                          <div v-for="movie in user_like_recommends[0].slice(index * 4, (index * 4) + 4)" :key="movie.pk" class="col-md-3">
                            <div class="d-flex justify-content-center">
                              <ProfileRecommendMovie :movie="movie"></ProfileRecommendMovie>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <a class="carousel-control-prev" href="#recommendCarousel" role="button" data-bs-slide="prev">
                      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                      <span class="visually-hidden">Previous</span>
                    </a>
                    <a class="carousel-control-next" href="#recommendCarousel" role="button" data-bs-slide="next">
                      <span class="carousel-control-next-icon" aria-hidden="true"></span>
                      <span class="visually-hidden">Next</span>
                    </a>
                  </div>
                </div>
              </div>
            </div>
            <div class="d-flex align-items-center justify-content-between mb-3">
              <h5 style="font-weight:bold; margin-left:10px; color: pink;">❤️MBTI로 영화 추천</h5>
            </div>
            <div class="p-4">
              <div class="row">
                <div v-if="user_mbti_recommends" class="container-fluid">
                  <div id="mbtiRecommendCarousel" class="carousel slide" data-bs-ride="carousel">
                    <div class="carousel-inner">
                      <div v-for="(movieGroup, index) in Math.ceil(user_mbti_recommends.length / 4)" :key="index" :class="['carousel-item', { active: index === 0 }]">
                        <div class="row justify-content-center">
                          <div v-for="movie in user_mbti_recommends.slice(index * 4, (index * 4) + 4)" :key="movie.id" class="col-md-3">
                            <div class="d-flex justify-content-center">
                              <ProfileRecommendMbti :movie="movie"></ProfileRecommendMbti>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <a class="carousel-control-prev" href="#mbtiRecommendCarousel" role="button" data-bs-slide="prev">
                      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                      <span class="visually-hidden">Previous</span>
                    </a>
                    <a class="carousel-control-next" href="#mbtiRecommendCarousel" role="button" data-bs-slide="next">
                      <span class="carousel-control-next-icon" aria-hidden="true"></span>
                      <span class="visually-hidden">Next</span>
                    </a>
                  </div>
                </div>
              </div>
            </div>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>


<script>

import { mapState } from 'vuex'
import ProfileMovie from './ProfileMovie.vue'
import ProfileRecommendMovie from './ProfileRecommendMovie.vue'
import ProfileRecommendMbti from './ProfileRecommendMbti.vue'

  
  export default {
    name: "ProfileView",
    components: {
      ProfileMovie,
      ProfileRecommendMovie,
      ProfileRecommendMbti,
    },
    data() {
      return {
      }
    },
  
    computed: {
      ...mapState(['user_info', 'user_like_movies', 'user_like_recommends', 'user_mbti_recommends']),
      isLogin() {
      return this.$store.getters.isLogin;
      },
      
    },
  
    methods: {
    },
  
    created() {
      this.$store.dispatch('userLikeMovies')
      this.$store.dispatch('userLikeRecommends')
      this.$store.dispatch('userMbtiRecommends')
    },
  }
</script>
  
<style scoped>
  .my-block {
    background-color: black;
  }
  
  .profile-head {
      transform: translateY(3rem)
  }
  
  
  .is-circle {
    background-color:darkgray;
  }
  
  
  .name{
    animation: hue-rotate 2s linear infinite alternate;
    color: rgb(26, 26, 26);
    border-radius: 5px;
    display: inline-block;
  
  }
  
  /* @keyframes hue-rotate {
    to{ filter: hue-rotate(90deg)}
  }
   */
  
    .update:active{
      transform: translateY(4px) translateX(4px);
      box-shadow: #BC41AB 0px 0px 0px;
    }
  
    .movie_update{
      background-color: #E92964;
      box-shadow: #BC41AB 4px 4px 0px;
      border-radius: 5px;
      transition: transform 200ms, box-shadow 200ms;
      color : #fff;
      width: 175px;
      height: 40px;
      text-align: center;
      outline: none;
    

    }
  
    .movie_update:active{
      transform: translateY(4px) translateX(4px);
      box-shadow: #BC41AB 0px 0px 0px;
    }
  
</style>
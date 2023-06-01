import Vue from "vue";
import Vuex from "vuex";

import axios from "axios";
import router from "../router";

import createPersistedState from "vuex-persistedstate";


const HOME_URL = "http://127.0.0.1:8000";

const API_URL =
  "https://api.themoviedb.org/3/movie/now_playing?api_key=a51700c7b5c0eac2db0ce7a959dcc750&language=ko-KR";
const POPULAR_URL =
  "https://api.themoviedb.org/3/movie/popular?api_key=a51700c7b5c0eac2db0ce7a959dcc750&language=ko-KR";

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState({
    storage: window.sessionStorage // store를 session storage에 유지
})],
  state: {
    newMovieList: [],
    popularMovieList: [],
    token: null,
    user_info: [],
    communitys: [],
    movieComments: [],
    like_movies: [],
    user_like_movies: [],
    user_like_recommends: [],
    genreMovieList: [],
    user_mbti_recommends: [],
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false;
    },
  },
  mutations: {
    // SIGN_UP(state, token){
    //   state.token = token
    // },
    SAVE_TOKEN(state, token) {
      if (router.currentRoute.path !== "/movie") {
        state.token = token;
        console.log(state.token);
        router.push({ name: "movie" });
      }
    },
    GET_MOVIES(state, newMovieList) {
      state.newMovieList = newMovieList;
    },
    GET_POPULAR_MOVIES(state, popularMovieList) {
      state.popularMovieList = popularMovieList;
    },
    GET_COMMUNITY(state, communitys) {
      state.communitys = communitys;
    },
    GET_USER_INFO(state, user_info) {
      state.user_info = user_info;
      // console.log('1')
      // console.log(state.user_info)
    },
    USER_LIKE_MOVIES(state, user_like_movies) {
      state.user_like_movies = user_like_movies
    },

    USER_LIKE_RECOMMENDS(state, user_like_recommends) {
      state.user_like_recommends = user_like_recommends
    },

    USER_MBTI_RECOMMENDS(state, user_mbti_recommends) {
      state.user_mbti_recommends = user_mbti_recommends
    },

    LOGOUT(state) {
      state.token = null;
      state.user_info = [];
      router.push({ name: "login" });
    },
    LIKE_MOVIES(state, like_movies) {
      console.log('개수확인', like_movies)
      state.like_movies = like_movies
      console.log('1', like_movies)
    }
  },
  actions: {
    // 최신영화 가져오기!
    getMovies(context) {
      axios({
        method: "get",
        language: "ko-KR",
        url: API_URL,
      })
        .then((res) => {
          context.commit("GET_MOVIES", res.data.results);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // 인기영화 가져오기!
    getPopularMovies(context) {
      axios({
        method: "get",
        url: POPULAR_URL,
      })
        .then((res) => {
          //console.log(res.data.results)
          context.commit("GET_POPULAR_MOVIES", res.data.results);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    signUp(context, payload) {
      const username = payload.username;
      const password = payload.password;
      const password2 = payload.password2;
      const name = payload.name;
      const mbtis = payload.mbtis;
      const genders = payload.genders;

      axios({
        method: "post",
        url: `${HOME_URL}/accounts/signup/`,
        data: {
          username,
          password,
          password2,
          name,
          mbtis,
          genders,
        },
      })
        .then((res) => {
          console.log(res.data);
          //context.commit('SIGN_UP', res.data.key)
          context.commit("SAVE_TOKEN", res.data.access);
          console.log("잘들어갔음!");
        })
        .catch((err) => {
          console.log(err);
        });
    },

    login(context, payload) {
      const username = payload.username;
      const password = payload.password;
      axios({
        method: "post",
        url: `${HOME_URL}/auth/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          context.commit("SAVE_TOKEN", res.data.access);
          console.log("로그인 성공!");
          const token = res.data.access;
          const user_pk = res.data.user.pk
          // console.log('-----')
          // console.log(token)
          axios({
            method: "get",
            url: `${HOME_URL}/accounts/profile/`,
            headers: {
              Authorization: `Bearer ${token}`,
            },
            params: {
              user_pk: user_pk
            }
          })
            .then((response) => {
              context.commit('GET_USER_INFO', response.data)
              console.log('사용자 정보:', response.data);

            })
            .catch((err) => {
              console.log(err);
              console.log("사용자 정보 가져오기 실패...");
            });
        })
        .catch((err) => {
          console.log(err);
          console.log("로그인 실패...");
        });
    },

    logout(context) {
      context.commit("LOGOUT");
    },

    getCommunity(context) {
      axios({
        method: "get",
        url: `${HOME_URL}/api/v1/community/`,
        // headers: {
        //   Authorization: `Bearer ${token}`,
        // }
      }).then((response) => {
        context.commit("GET_COMMUNITY", response.data);
        console.log(response)
      });
    },

    userLikeMovies(context) {
      const userId = context.state.user_info[0].user_id
      const token = context.state.token
      axios({
        method: 'get',
        url: `${HOME_URL}/accounts/${userId}/user_like_movie/`,
        headers: {
          Authorization: `Bearer ${token}`,
        }, 
      })
        .then((res) => {
          context.commit("USER_LIKE_MOVIES", res.data)
        }) 
        .catch(err => {
          console.log(err)
        })
    },
    userLikeRecommends(context) {
      const userId = context.state.user_info[0].user_id
      const token = context.state.token
      axios({
        method: 'get',
        url: `${HOME_URL}/accounts/${userId}/user_like_reco/`,
        headers: {
          Authorization: `Bearer ${token}`,
        }, 
      })
        .then((res) => {
          context.commit("USER_LIKE_RECOMMENDS", res.data)
        }) 
        .catch(err => {
          console.log(err)
        })
    },

    userMbtiRecommends(context) {
      const userId = context.state.user_info[0].user_id
      const token = context.state.token
      axios({
        method: 'get',
        url: `${HOME_URL}/accounts/${userId}/user_mbti_reco/`,
        headers: {
          Authorization: `Bearer ${token}`,
        }, 
      })
        .then((res) => {
          context.commit("USER_MBTI_RECOMMENDS", res.data)
        }) 
        .catch(err => {
          console.log(err)
        })
    },

    likeMovies(context, payload) {
    const token = payload.token;
    const userId = payload.userId;
    const mbtis = payload.mbtis
    const movieId = payload.movieId

    axios({
      method: 'post',
      url: `${HOME_URL}/api/v1/movies/${movieId}/likes/`,
      data: {
        userId, mbtis
      },
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then(() => {
        console.log('커뮤니티 좋아요가 성공적으로 등록되었습니다.');
        // 로컬에서 community_user_like 리스트 업데이트
        context.dispatch('fetchMovieLikes', movieId)
      })
      .catch(err => {
        console.log(err);
      });
    },

    fetchMovieLikes(context, movieId){
      const token = context.state.token
      axios({
        method: 'get',
        url: `${HOME_URL}/api/v1/movies/${movieId}/`,
        data: {
          movie_pk: movieId
        },
        headers: {
        Authorization: `Bearer ${token}`,
      },
      })
        .then((res) => {
          //서버에서 받아온 좋아요 개수 업데이트
          console.log('여기까지?')
          // console.log(res.data)
          context.commit('LIKE_MOVIES', res.data.movie_user_like)
        })
        .catch(err => {
          console.log(err)
        })
    },

    getLikeMovie(context, payload) {
      const token = payload.token;
      const userId = payload.userId;
      const mbtis = payload.mbtis
      const movieId = payload.movieId
      axios({
        method: 'get',
        url: `${HOME_URL}/api/v1/movies/${movieId}/likes/`,
        data: {
          userId, mbtis
        },
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
        .then((res) => {
          console.log('커뮤니티 좋아요가 성공적으로 등록되었습니다.');
          // 로컬에서 community_user_like 리스트 업데이트
          context.commit('LIKE_MOVIES', res.data.movie_user_like)
          console.log('개수확인', res.data.movie_user_like)
        })
        .catch(err => {
          console.log(err);
        });
    },

  },
  modules: {},
});

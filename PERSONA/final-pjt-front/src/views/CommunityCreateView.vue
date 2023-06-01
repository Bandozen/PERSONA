<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createCommunity">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunityCreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    },
    ...mapState(['user_info'])
  },
  methods: {
    createCommunity() {
      const title = this.title
      const content = this.content
      const storedData = sessionStorage.getItem("vuex");
      const token = JSON.parse(storedData).token;
      const user = this.user_info[0].user_id
      // const username = this.user_info[0].username
      console.log(this.user_info[0])
      const community_user_like = []
      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/community/`,
        data: { title, content, user, community_user_like},
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.$router.push({name: 'community'})
      })
      .catch((err) => {
        console.log(err.response)
      })
    }
  }
}
</script>

<style>

</style>

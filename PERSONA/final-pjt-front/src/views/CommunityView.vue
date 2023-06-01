<template>
  <div class="community">
    <header>
    <h1>Community Page</h1>
    </header>
    <CommunityList />
  </div>
</template>

<script>
import CommunityList from '@/components/CommunityList.vue'

export default {
  name: 'CommunityView',
  components: {
    CommunityList,
  },
  
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  methods: {
    getCommunity() {
      this.$store.dispatch('getCommunity')
    }
  },

  created() {
    this.getCommunity()
  },
  

}
</script>

<style >
* {
  box-sizing: border-box;
  margin: 0;
  color: #ffffff;
  background-color: black;
}

.community {
  width: 100%;
  margin-top: 5rem;
  padding: 0 3rem;
  display: flex;
  flex-direction: column;
}
</style>
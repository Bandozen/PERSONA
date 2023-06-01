<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark">
      <router-link style="text-decoration: none; color: inherit" to="/movie">
        <img
          src="./assets/Persona.png"
          alt="로고 이미지"
          style="width: 150px; height: 150px"
        />
      </router-link>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item>
            <router-link
              style="text-decoration: none; color: inherit"
              to="/movie"
              >Movie</router-link
            ></b-nav-item
          >
          <b-nav-item>
            <router-link
              style="text-decoration: none; color: inherit"
              to="/genre"
              >Genre</router-link
            ></b-nav-item
          >
          <b-nav-item>
            <router-link
              style="text-decoration: none; color: inherit"
              to="/community"
              >커뮤니티</router-link
            ></b-nav-item
          >
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template #button-content>
              <em>User</em>
            </template>
            <b-dropdown-item variant="light"
              ><router-link
                v-if="!isLogin"
                style="text-decoration: none; color: inherit"
                to="/login"
                >로그인 |
              </router-link></b-dropdown-item
            >
            <b-dropdown-item variant="light"
              >
            <router-link
              v-if="isLogin"
              style="text-decoration: none; color: inherit"
              to="/profile"
              >프로필 |
            </router-link>
            </b-dropdown-item
            >
            <b-dropdown-item variant="light">
              <router-link
                v-if="!isLogin"
                style="text-decoration: none; color: inherit"
                to="/signup"
                >회원가입</router-link
              ></b-dropdown-item
            >
            <b-dropdown-item variant="light"
              ><a href="#" v-if="isLogin" @click="logout"
                >로그아웃 |
              </a></b-dropdown-item
            >
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  methods: {
    logout() {
      this.$store.dispatch("logout");
      alert("로그아웃되었습니다.");
      this.$router.push({ name: "movie" });
    },
  },
};
</script>

<style>
* {
  background-color: black;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

nav {
  padding: 30px;
  background-color: black;
}

nav a {
  font-weight: bold;
  color: white;
}

nav a.router-link-exact-active {
  color: rgb(211, 47, 39);
}
</style>

<template>
  <div class="loginbox">
    <div id="Login">
      <div class="login">
        <h1>Sign In</h1>
        <div class="login-info">
          <form @submit.prevent="login">
            <input
              placeholder="아이디를 적어주세요."
              type="text"
              id="username"
              v-model="username"
            />
            <br />
            <input
              placeholder="비밀번호를 적어주세요."
              type="password"
              id="password"
              v-model="password"
            />
            <br />
            <input type="submit" value="로그인" @click="login" />
          </form>
        </div>
      </div>
      <div class="signup2">
        <span>계정이 없으신가요?</span>
        <router-link class="nav-item" :to="{ name: 'signup' }"
          >Sign Up</router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      username: null,
      password: null,
    };
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    }
  },
  methods: {
    login() {
      const username = this.username;
      const password = this.password;

      const payload = {
        username,
        password,
      };

      this.$store.dispatch("login", payload);
    },
    logout() {
    this.$store.dispatch('logout')
  },
  },
};
</script>

<style >
.loginbox {
  margin: 0;
  box-sizing: border-box;
  border: 1px solid;
  position: relative;
  color: white;
}

#Login {
  position: absolute;
  top: 50%;
  left: 50%;
  margin: -25px 0 0 -25px;
  margin-top: 7rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: 0.5px solid #4b4a54;
  border-radius: 10px;
  background-color: rgba(000, 000, 000, 0.4);
}

.login {
  width: 400px;
  height: 400px;
  display: flex;
  flex-direction: column;
  padding: 50px;
}

.login > h1 {
  margin-bottom: 30px;
}

.login-info input {
  border: 1px solid rgb(211, 211, 211);
  width: 100%;
  height: 40px;
  border-radius: 5px;
  padding: 10px;
  font-size: 12px;
  margin: 15px;
}

#Login button {
  margin-top: 30px;
  height: 50px;
  border: none;
  background-color: rgb(211, 47, 39);
  border-radius: 5px;
  font-weight: 700;
  color: #ffffff;
  border-radius: 5px;
  padding: 5px;
}

.signup2 {
  margin-bottom: 20px;
  width: 400px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.signup2 span {
  margin-right: 10px;
}

.nav-item {
  text-decoration: none;
  font-weight: 500;
  color: rgb(211, 47, 39);
}
</style>

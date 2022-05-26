<template>
  <v-app>
    <v-main>
      <LoginScreen :toggle_callback="togglePages" v-if="screen === 'login'" />
      <Recovery :toggle_callback="togglePages" v-if="screen === 'recovery'" />
    </v-main>
  </v-app>
</template>

<script>
import LoginScreen from "./components/LoginScreen.vue";
import Recovery from "./components/Recovery.vue";

export default {
  name: "App",

  components: {
    LoginScreen,
    Recovery,
  },

  methods: {
    togglePages() {
      if (this.screen === "login") this.screen = "recovery";
      else if (this.screen === "recovery") this.screen = "login";
    },
  },

  data: () => ({
    screen: "login",
  }),
};
</script>

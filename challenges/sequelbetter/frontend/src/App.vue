<template>
  <v-app dark src="/cinema.jpg">
    <v-app-bar>
      <v-toolbar-title>The sequel is never better</v-toolbar-title>
    </v-app-bar>
    <v-main class="sequelcontainer">
      <v-container class="main">
        <v-alert v-if="error !== false"
          >Something went wrong when we tried to execute your query:
          {{ error }}</v-alert
        >
        <v-form @keyup.enter="sendRequest">
          <v-text-field
            label="Movie to check"
            variant="contained"
            prepend-icon="mdi-movie-search"
            clearable
            v-model="query"
          ></v-text-field>
        </v-form>
        <v-progress-linear indeterminate v-if="loading"></v-progress-linear>
        <v-container v-if="results && results.length != 0">
          <h1>Result</h1>
          <v-row justify="space-around">
            <movie-sequel-pair
              v-for="(pair, idx) in results"
              :key="idx"
              :data="pair"
            >
            </movie-sequel-pair
          ></v-row>
        </v-container>
      </v-container>
    </v-main>
    <v-footer id="footer">
      <p>
        Photo by
        <a
          href="https://unsplash.com/@felixmooneeram?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
          >Felix Mooneeram</a
        >
        on
        <a
          href="https://unsplash.com/s/photos/movie?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
          >Unsplash</a
        >. Data provided by
        <a href="https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset"
          >The Movies Dataset</a
        >
        under
        <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0</a>.
      </p>
    </v-footer>
  </v-app>
</template>

<style>
#main {
  min-height: 100%;
  background: none;
}
#footer {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
}
#footer a {
  color: white;
}
body {
  background-image: url("assets/cinema.jpg");
  background-repeat: no-repeat;
  background-size: auto auto;
  background-position: center center;
}
</style>

<script>
import MovieSequelPair from "./components/MovieSequelPair.vue";
export default {
  components: { MovieSequelPair },
  name: "App",

  methods: {
    async sendRequest() {
      const handle_error = (e) => {
        this.error = e;
        this.results = [];
      };
      const handle_done = () => {
        this.loading = false;
      };

      this.loading = true;

      fetch(`/lookup?q=${this.query}`)
        .then((response) => {
          this.error = false;
          response
            .json()
            .then((json) => {
              this.results = json["results"];
            })
            .catch(handle_error)
            .finally(handle_done);
        })
        .catch(handle_error)
        .finally(handle_done);
    },
  },

  data: () => ({
    query: "",
    loading: false,
    error: false,
    results: [],
  }),
};
</script>

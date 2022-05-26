<template>
  <v-container fill-height>
    <v-card class="elevation-12">
      <v-toolbar dark color="primary">
        <v-toolbar-title>FlagManager Login</v-toolbar-title>
      </v-toolbar>
      <v-card-text>
        <v-container v-if="flag !== ''">
          <v-alert type="success" prominent>
            <template v-slot:text>
              Sign in successfully! We've found one flag: {{ flag }}
            </template>
          </v-alert>
        </v-container>
        <v-container v-if="error !== ''">
          <v-alert type="error" prominent>
            <template v-slot:text> Something went wrong: {{ error }} </template>
          </v-alert>
        </v-container>
        <v-container>
          <v-alert v-if="failed_login_attempts >= 5" type="info" prominent>
            <template v-slot:text>
              If you forgot your password, you can try to retrieve it
            </template>
            <template v-slot:append>
              <v-btn variant="text" size="small" @click="toggle_callback"
                >Reset password</v-btn
              >
            </template>
          </v-alert>
        </v-container>
        <v-form ref="form" @submit.capture="try_login" id="login-form">
          <v-text-field
            v-model="username"
            name="username"
            label="Username"
            type="text"
            placeholder="Email address"
          ></v-text-field>

          <v-text-field
            v-model="password"
            name="password"
            label="Password"
            type="password"
            placeholder="password"
          ></v-text-field>
          <v-btn color="success" class="mr-4" type="submit" form="login-form">
            Login
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginScreen",

  props: ["toggle_callback"],

  data: () => ({
    failed_login_attempts: 0,
    login_failed: false,
    error: "",
    flag: "",

    username: "",
    password: "",

    recovery_step: 0,

    birthday: new Date(),
    birthday_failed: false,

    nickname: "",
    nickname_failed: false,

    fav_place: "",
    fav_place_failed: false,
  }),

  methods: {
    try_login() {
      axios
        .post("/api/login", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          if ("Err" in response.data) {
            this.error = response.data["Err"];
            this.login_failed = true;
            if (
              this.error === "UsernameNotFound" ||
              this.error === "InvalidPassword"
            )
              ++this.failed_login_attempts;
          } else {
            this.error = "";
            this.login_failed = false;

            if ("Ok" in response.data) this.flag = response.data["Ok"]["flag"];
          }
        })
        .catch((err) => {
          this.error = err;
        });
    },
  },
};
</script>

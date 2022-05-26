<template>
  <v-container fill-height>
    <v-card class="elevation-12">
      <v-toolbar dark color="primary">
        <v-btn icon @click="toggle_callback">
          <v-icon> mdi-arrow-left </v-icon>
        </v-btn>
        <v-toolbar-title>FlagManager: Forgot password?</v-toolbar-title>
      </v-toolbar>
      <v-card-text>
        <v-container v-if="error !== ''">
          <v-alert type="error" prominent>
            <template v-slot:text> {{ error }} </template>
          </v-alert>
        </v-container>
        <v-container v-if="recovered_password !== ''">
          <v-alert type="success" prominent>
            <template v-slot:text>
              Verification has been completed. You can now login using the
              following password: {{ recovered_password.password }}
            </template>
          </v-alert>
        </v-container>
        <v-form ref="form" @submit.capture="try_submit" id="login-form">
          <v-text-field
            v-model="username"
            name="username"
            label="Username"
            type="email"
            placeholder="Email address"
          ></v-text-field>

          <v-text-field
            v-model="birthday"
            name="birthday"
            label="birthday"
            type="date"
            placeholder="birthday"
          ></v-text-field>

          <v-text-field
            v-model="nickname"
            v-if="recovery_step > 0"
            name="nickname"
            label="Nickname as a child"
            type=""
            placeholder="Nickname as a child"
          ></v-text-field>

          <v-text-field
            v-model="fav_place"
            v-if="recovery_step > 0"
            name=""
            label="Favorite square in Belgium"
            type=""
            placeholder="Favorite square in Belgium"
          ></v-text-field>

          <v-btn
            color="success"
            class="mr-4"
            type="submit"
            form="login-form"
            :loading="loading"
            :disabled="loading"
          >
            Continue
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";

const CONVERT_ERROR = (error) => {
  switch (error) {
    case "NoSuchMail":
      return "Email address not found";
    case "InvalidBirthDate":
      return "Incorrect birthday";
    case "MoreDataNeeded":
      return "More recovery data is needed";
    case "InvalidNickName":
      return "Incorrect nickname";
    case "InvalidSquare":
      return "Incorrect favorite square in Belgium";
    default:
      return error;
  }
};

export default {
  name: "LoginScreen",
  props: ["toggle_callback"],

  data: () => ({
    username: "",

    birthday: new Date(),
    nickname: "",
    fav_place: "",

    error: "",
    recovery_step: 0,
    loading: false,

    recovered_password: "",
  }),

  methods: {
    try_submit() {
      this.loading = true;
      if (this.recovery_step === 0) this.try_recovery_1();
      if (this.recovery_step === 1) this.try_recovery_2();
    },
    async try_recovery_1() {
      return axios
        .post("/api/recover", {
          email: this.username,
          birthday: this.birthday,
        })
        .then((response) => {
          const data = response.data;
          if ("Err" in data) {
            this.error = CONVERT_ERROR(data["Err"]);
            this.login_failed = true;

            if (data["Err"] === "MoreDataNeeded") {
              this.recovery_step = 1;
            }
            return;
          }

          this.error = "";
          this.login_failed = false;
        })
        .catch((err) => {
          this.error = err;
          this.login_failed = true;
        })
        .finally(() => {
          this.loading = false;
        });
    },
    async try_recovery_2() {
      return axios
        .post("/api/recover", {
          email: this.username,
          birthday: this.birthday,
          highschool_nickname: this.nickname,
          fav_square: this.fav_place,
        })
        .then((response) => {
          const data = response.data;
          if ("Err" in data) {
            this.error = CONVERT_ERROR(data["Err"]);
            this.login_failed = true;
            return;
          }

          if ("Ok" in data) {
            this.recovered_password = data["Ok"];
          }

          this.error = "";
          this.login_failed = false;
        })
        .catch((err) => {
          this.error = err;
          this.login_failed = true;
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
  computed: {
    has_error() {
      return this.birthday_failed || this.nickname_failed || this.error !== "";
    },
  },
};
</script>

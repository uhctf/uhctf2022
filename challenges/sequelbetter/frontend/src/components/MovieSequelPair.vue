<template>
  <v-col cols="4">
    <v-card elevation="8">
      <v-card-text>
        <v-timeline density="compact" truncate-line="none">
          <v-timeline-item right :size="timeline_size">
            <strong>{{ data.title }}</strong>
            {{ data.rating }}/10
          </v-timeline-item>
          <v-timeline-item
            :size="timeline_size"
            v-if="data.sequel_title !== null && data.sequel_rating !== null"
          >
            <strong>{{ data.sequel_title }}</strong>
            {{ data.sequel_rating }}/10
          </v-timeline-item>
          <v-timeline-item :size="timeline_size" v-else>
            No sequel found
          </v-timeline-item>
        </v-timeline> </v-card-text
      ><v-card-actions>
        <v-alert
          v-if="data.sequel_rating && data.sequel_rating > data.rating"
          type="success"
          >The sequel is better!</v-alert
        >
        <v-alert
          v-else-if="data.sequel_rating && data.sequel_rating < data.rating"
          >The sequel is worse!</v-alert
        ></v-card-actions
      >
    </v-card>
  </v-col>
</template>
  
<script>
export default {
  props: ["data"],
  data: () => ({
    timeline_size: "small",
  }),
};
</script>
  
  <style>
</style>
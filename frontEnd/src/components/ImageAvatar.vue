<template>
  <v-avatar size="100" rounded="0">
    <v-img
      :src="imgSrc"
    ></v-img>
  </v-avatar>
</template>

<script>
  export default {
    props: {
      imgSrc: {
        type: String,
        default: "https://www.svgrepo.com/download/287754/smartphone.svg"
      },
    },
  };
</script>

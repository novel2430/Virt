<template>
  <v-app-bar class="main" flat>
    <v-btn icon to="/">
      <v-icon>mdi-arrow-left-bold</v-icon>
    </v-btn>
    <v-app-bar-title class="text-center" style="margin:0px">{{ title }}</v-app-bar-title>
    <v-btn icon>
      <v-icon>mdi-dots-vertical</v-icon>
    </v-btn>
  </v-app-bar>
</template>

<script>
  export default {
    data: () => ({ 
    }),
    props: {
      title: {
        type: String,
        required: true,
      },
    },
  };
</script>


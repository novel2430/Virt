<script setup>
  import SearchBar from '@/components/SearchBar.vue'
</script>

<template>
  <v-app-bar class="main" flat border=false>
    <v-btn icon>
      <v-icon>mdi-account</v-icon>
    </v-btn>
    <SearchBar/>
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

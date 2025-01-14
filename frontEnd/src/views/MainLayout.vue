<script setup>
  import BottomBar from '@/components/BottomBar.vue'
</script>
<template>
  <v-layout class="test">
    <router-view />
    <!-- Bottom Bar -->
    <BottomBar class="bottom-bar"/>
  </v-layout>
</template>

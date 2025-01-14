<script setup>
  import TopBar from '@/components/NavTopBar.vue'
  import Card from '@/components/Card.vue'
</script>

<template>
  <!-- Top Bar -->
  <TopBar title="艺术治疗"/>
  <!-- Main Area -->
  <v-main class="main">
    <v-container>
      <v-row 
        dense
        v-for="n in cards"
      >
        <v-col>
          <Card 
          :title=n.title 
          :icon=n.icon 
          :imgSrc=n.src
          />
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
  export default {
    data: () => ({ 
      cards: [
        {
          title: "画出心流",
          icon: "🖌️",
          src: "https://www.svgrepo.com/download/411712/paint.svg",
        },
        {
          title: "心轮疗愈",
          icon: "🧘🏻‍♀️",
          src: "https://www.svgrepo.com/download/411750/stamp.svg",
        },
        {
          title: "弹出心流",
          icon: "🎹",
          src: "https://www.svgrepo.com/download/411733/rotate.svg",
        },
      ],
    }),
  };
</script>

<style lang="scss" scoped>
</style>

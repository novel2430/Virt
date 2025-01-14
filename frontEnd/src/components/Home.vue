<script setup>
  import TopBar from '@/components/TopBar.vue'
  import Card from '@/components/Card.vue'
</script>

<template>
  <!-- Top Bar -->
  <TopBar title="Home"/>
  <!-- Main Area -->
  <v-main class="main">
    <v-container>
      <v-row dense>
        <v-col class="card-spacing">
          <Card 
          title="倾诉解答" 
          icon="👂🏻" 
          text="三言两语，渡人之舟"
          imgSrc="https://www.svgrepo.com/download/287785/working-work.svg"
          to="/question-area"
          />
        </v-col>
      </v-row>
      <v-row dense>
        <v-col class="card-spacing">
          <Card 
          title="每日一问" 
          icon="🙋" 
          text="有什么想问的呀？"
          to="/day-question"
          />
        </v-col>
      </v-row>
      <v-row dense>
        <v-col class="card-spacing">
          <Card
          title="艺术治疗"
          icon="🎨"
          text="艺术可以调剂身心喔！"
          imgSrc="https://www.svgrepo.com/download/287744/coffee.svg"
          to="/art-therapy"
          />
        </v-col>
      </v-row>
      <v-row dense>
        <v-col class="card-spacing">
          <Card
          title="温暖小店"
          icon="🛍️"
          text="来小店休憩一下吧..."
          imgSrc="https://www.svgrepo.com/download/287766/shopping-bag.svg"
          to="/nice-store"
          />
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<style lang="scss" scoped>
.card-spacing {
  margin-bottom: 2%;
  display: flex; 
  justify-content: center;
}
</style>

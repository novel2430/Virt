<script setup>
  import TopBar from '@/components/NavTopBar.vue'
  import Card from '@/components/StoreCard.vue'
</script>

<template>
  <!-- Top Bar -->
  <TopBar title="温暖小店"/>
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
          :price=n.price
          :text=n.text
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
          title: "咖啡杯",
          price: "25",
          text: "经典陶瓷咖啡杯，适合家用和办公，容量300ml，简约设计，易于清洗。",
          src: "https://www.svgrepo.com/download/315922/drink-cup-coffee.svg",
        },
        {
          title: "耳机",
          price: "120",
          text: "入耳式有线耳机，立体音效，兼容大多数设备，提供舒适佩戴体验，适合音乐爱好者。",
          src: "https://www.svgrepo.com/download/315931/headphones-blue.svg",
        },
        {
          title: "运动水壶",
          price: "45",
          text: "便携式塑料水壶，容量750ml，带有防漏设计，适合户外运动或日常使用。",
          src: "https://www.svgrepo.com/download/315919/coffee-drink.svg",
        },
        {
          "title": "码表",
          "price": "150",
          "text": "专业运动码表，多功能计时设计，适合跑步、骑行和健身使用。",
          "src": "https://www.svgrepo.com/download/315898/time-cronometer.svg"
        },
        {
          "title": "哑铃",
          "price": "200",
          "text": "高品质哑铃，防滑设计，适合力量训练，支持多种重量选择。",
          "src": "https://www.svgrepo.com/download/315903/weight-dumbbell.svg"
        },
        {
          "title": "篮球",
          "price": "80",
          "text": "标准尺寸篮球，适合室内外使用，耐磨材质提供长久使用体验。",
          "src": "https://www.svgrepo.com/download/315908/basketball.svg"
        },
      ],
    }),
  };
</script>

<style lang="scss" scoped>
</style>

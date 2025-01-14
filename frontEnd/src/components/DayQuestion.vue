<script setup>
  import TopBar from '@/components/NavTopBar.vue'
  import QuestionCard from '@/components/QuestionCard.vue'
</script>

<template>
  <!-- Top Bar -->
  <TopBar title="每日一问"/>
  <!-- Main Area -->
  <v-main class="main">
    <v-container>
      <v-row
        v-for="n in questions"
        :key="n"
      >
        <v-col>
          <QuestionCard
            :userName="n.name"
            :icon="n.icon"
            :content="n.content"
            :time="n.time"
            :views="n.view"
          />
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
  export default {
    data: () => ({ 
      questions: [
        {
          name: "布丁",
          icon: "🍮",
          content: "你今天吃早餐了吗？",
          time: "1 minute",
          view: "15"
        },
        {
          name: "饼干",
          icon: "🍪",
          content: "你喜欢下雨天吗？",
          time: "5 minutes",
          view: "20"
        },
        {
          name: "巧克力",
          icon: "🍫",
          content: "你常常熬夜吗？",
          time: "10 minutes",
          view: "30"
        },
        {
          name: "牛奶",
          icon: "🥛",
          content: "你觉得冬天比夏天好吗？",
          time: "15 minutes",
          view: "25"
        },
        {
          name: "蛋糕",
          icon: "🎂",
          content: "你今天心情好吗？",
          time: "20 minutes",
          view: "35"
        },
        {
          name: "糖果",
          icon: "🍬",
          content: "你愿意一个人去旅行吗？",
          time: "30 minutes",
          view: "40"
        }
      ],
    }),
  };
</script>

<style lang="scss" scoped>
.btn-area {
  display: flex;                /* 使用 flexbox */
  justify-content: space-around; /* 水平居中并在元素之间添加间隔 */
  align-items: center;          /* 垂直居中 */
  width: 100%;
}
.btn-yes {
  background-color: $primary-highlight-color;
  color: $text-color;
}
.btn-no {
  background-color: $primary-background-color;
  color: $text-color;
}
</style>

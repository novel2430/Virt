<script setup>
  import TopBar from '@/components/NavTopBar.vue'
  import SearchBar from '@/components/SearchBar.vue'
  import QuestionAreaIcon from '@/components/QuestionAreaIcon.vue'
  import PostCard from '@/components/PostCard.vue'
</script>

<template>
  <!-- Top Bar -->
  <TopBar title="倾诉解答"/>
  <!-- Main Area -->
  <v-main class="main">
    <v-container>
      <!-- Search Bar -->
      <v-row style="margin-bottom: 20px;">
        <v-col>
          <SearchBar/>
        </v-col>
      </v-row>
      <!-- Question Area Icon Btn -->
      <v-row dense>
        <v-col
        v-for="n in firstRow"
        :key="n"
        >
          <QuestionAreaIcon :title=n.title :iconName=n.icon />
        </v-col>
      </v-row>
      <v-row dense>
        <v-col
        v-for="n in secondRow"
        :key="n"
        >
          <QuestionAreaIcon :title=n.title :iconName=n.icon />
        </v-col>
      </v-row>
      <!-- Emotion Post Card -->
      <v-row 
        v-for="n in postCards"
        :key="n"
        dense
        style="margin-top: 20px;"
      >
        <PostCard 
          :userName=n.userName
          :postTag=n.tag
          :postText=n.text
          :time=n.time
          :views=n.view
          :icon=n.icon
        />
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
  export default {
    data: () => ({ 
      firstRow: [
        { title: "自我", icon: "🙆🏻", },
        { title: "家庭", icon: "🏠", },
        { title: "校园", icon: "🏫", },
        { title: "情感", icon: "♥️", },
      ],
      secondRow: [
        { title: "社交", icon: "🧑‍🤝‍🧑", },
        { title: "职场", icon: "⌨️", },
        { title: "疾病", icon: "🏥", },
        { title: "莫名", icon: "🤷🏻‍♀️", },
      ],
      postCards: [
        {
          userName: "苹果",
          tag: "#早餐 #难过",
          text: "早餐不好吃..",
          time: "2 second",
          view: "10",
          icon: "🍎",
        },
        {
          userName: "橙子",
          tag: "#工作 #忙碌",
          text: "今天工作好多，感觉喘不过气了。",
          time: "5 minutes",
          view: "25",
          icon: "🍊",
        },
        {
          userName: "葡萄",
          tag: "#失落 #安慰",
          text: "总是感觉自己做得不够好。",
          time: "15 minutes",
          view: "30",
          icon: "🍇",
        },
        {
          userName: "柚子",
          tag: "#健身 #疲惫",
          text: "刚跑完5公里，腿快断了。",
          time: "30 minutes",
          view: "60",
          icon: "🍐",
        },
        {
          userName: "樱桃",
          tag: "#晚餐 #孤单",
          text: "一个人吃饭，感觉有点落寞。",
          time: "1 hour",
          view: "40",
          icon: "🍒",
        },
      ],
    }),
  };
</script>

<style lang="scss" scoped>
.card-spacing {
  margin-bottom: 2%;
  display: flex; 
  justify-content: center;
}
</style>

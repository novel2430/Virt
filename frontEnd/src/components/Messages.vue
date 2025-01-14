<script setup>
  import TopBar from '@/components/NavTopBar.vue'
  import EmojiAvatar from '@/components/EmojiAvatar.vue'
</script>

<template>
  <!-- Top Bar -->
  <TopBar title="信息"/>
  <!-- Main Area -->
  <v-main>
    <v-container>
      <!-- Btn Area -->
      <v-row>
        <v-col class="d-flex justify-center">
          <v-sheet
            elevation="2"
            rounded="xl"
            class="sheet"
          >
            <v-row class="text-center">
              <v-col
                v-for="n in btnArea"
                :key="n"
              >
                <div>
                  <v-btn icon flat  class="btn-area-btn" size="50">
                    <v-icon size="40">{{ n.icon }}</v-icon>
                  </v-btn>
                </div>
                <div>
                  <a class="btn-title">{{ n.title }}</a>
                </div>
              </v-col>
            </v-row>
          </v-sheet>
        </v-col>
      </v-row>
      <!-- Messages Title -->
      <v-row>
        <v-col>
          <a class="btn-title">其他消息</a>
        </v-col>
      </v-row>
      <!-- Messages Area -->
      <v-row
        v-for="n in msgs"
        :key="n"
        dense
      >
        <v-col>
          <v-card hover class="btn-title">
            <v-card-item>
              <template v-slot:prepend>
                <EmojiAvatar
                  :icon=n.avatar
                />
              </template>
              <v-card-title>{{ n.name }}</v-card-title>
              <v-card-subtitle>{{ n.content }}</v-card-subtitle>
            </v-card-item>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
  export default {
    data: () => ({ 
      btnArea: [
        {icon: "mdi-thumb-up", title: "点赞"},
        {icon: "mdi-comment", title: "评论"},
        {icon: "mdi-heart-multiple", title: "收藏"},
      ],
      msgs: [
        {
          name: "薯条",
          content: "今天买的咖啡洒了，好心疼！",
          avatar: "🍟",
        },
        {
          name: "咖啡",
          content: "刚才和朋友看了一部超好笑的电影！",
          avatar: "☕",
        },
        {
          name: "披萨",
          content: "这几天一直加班，感觉好累。",
          avatar: "🍕",
        },
        {
          name: "奶茶",
          content: "刚买的奶茶被同事顺手拿走了...哭。",
          avatar: "🥛",
        },
        {
          name: "炸鸡",
          content: "今天午餐吃了超辣的炸鸡，真过瘾！",
          avatar: "🍗",
        },
        {
          name: "爆米花",
          content: "下班路上看到了一只超级可爱的流浪猫！",
          avatar: "🍿",
        },
      ],
    }),
  };
</script>

<style lang="scss" scoped>
.sheet {
  background-color: $second-background-color;
  min-width: 300px;
  width: 70%;
  padding: 20px;
}
.btn-area-btn {
  background-color: $transparent;
  color: #ffffff;
}
.btn-title {
  color: $text-color;
}
.msg-avatar {
  background-color: $second-background-color;
}
</style>

<script setup>
  import EmojiAvatar from '@/components/EmojiAvatar.vue'
</script>

<template>
  <v-card
    variant="elevated"
    class="wave-card"
    hover
  >
    <v-card-item>
      <template v-slot:append>
        <v-btn icon size="40" flat>
            <v-icon icon="mdi-dots-vertical"></v-icon>
        </v-btn>
      </template>
      <v-card-title style="height: 60px">
        <EmojiAvatar
          :icon="icon"
        />
        {{ userName }}
      </v-card-title>
    </v-card-item>
    <v-card-text class="tag">
      {{ postTag }}
    </v-card-text>
    <v-card-text style="padding-top: 2%; padding-bottom: 0;">
      <div class="post-card">
        <v-card class="gray-card" variant="outlined">
          <v-card-text style="font-size: 14px;">
            {{ postText }}
          </v-card-text>
        </v-card>
      </div>
    </v-card-text>
    <v-card-text style="font-size: 12px;">
      <div style="display: flex; text-align: center; justify-content: space-between">
      <a>{{ time }} ago . {{ views }} views</a>
      <a>
        <v-btn icon class="icon-btn" flat size="30" style="margin-right:10px;">
          <v-icon>mdi-thumb-up</v-icon>
        </v-btn>
        <v-btn icon class="icon-btn" flat size="30">
          <v-icon>mdi-forum</v-icon>
        </v-btn>
      </a>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    data: () => ({ 
    }),
    props: {
      userName: {
        type: String,
        default: "Novel2430",
      },
      icon: {
        type: String,
        default: "🍄",
      },
      postTag: {
        type: String,
        default: "#happy #coffee",
      },
      postText: {
        type: String,
        default: "Hello, World!",
      },
      time: {
        type: String,
        default: "2 second",
      },
      views: {
        type: String,
        default: "10",
      },
    },
  };
</script>

<style lang="scss" scoped>
.post-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: start;
}
.tag {
  color: $em-text-color;
  padding-bottom: 0;
  font-size: 15px
}
</style>

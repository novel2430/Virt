<script setup>
  import EmojiAvatar from '@/components/EmojiAvatar.vue'
</script>
<template>
  <v-card
    variant="elevated"
    class="wave-card"
    hover
  >
    <v-card-item v-if="isAi==true" class="left-title" style="padding-bottom: 0px;">
      <v-card-title style="height: 60px;">
        <EmojiAvatar
          icon="👨‍⚕️"
        />
        咨询师
      </v-card-title>
    </v-card-item>
    <v-card-item v-if="isAi==false" class="right-title" style="padding-bottom: 0px;">
      <v-card-title style="height: 60px;">
        <EmojiAvatar
          :icon="icon"
        />
        您
      </v-card-title>
    </v-card-item>
    <v-card-text style="padding-top: 2%; padding-bottom: 2%;">
      <div class="post-card">
        <v-card class="gray-card" variant="outlined">
          <v-card-text style="font-size: 14px;">
            <span class="content">{{ content }}</span>
          </v-card-text>
        </v-card>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    data: () => ({ 
    }),
    props: {
      icon: {
        type: String,
        default: "🍔",
      },
      content: {
        type: String,
        default: "Hello, World",
      },
      isAi: {
        type: Boolean,
        default: true,
      }
    },
  };
</script>

<style lang="scss" scoped>
.right-title {
  display: flex; 
  justify-content: end; 
  height: 60px;
}
.left-title {
  height: 60px;
}
.content {
  white-space: pre-wrap; /* 保留换行符并自动换行 */
}
</style>

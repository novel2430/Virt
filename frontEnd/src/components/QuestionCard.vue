<script setup>
  import EmojiAvatar from '@/components/EmojiAvatar.vue'
</script>
<template>
  <v-card
    variant="elevated"
    class="wave-card"
    hover
  >
  <template v-slot:actions >
    <div class="btn-area">
      <v-btn
        rounded="xl"
        class="btn-yes"
      >
        yes
      </v-btn>
      <v-btn
        rounded="xl"
        class="btn-no"
      >
        no
      </v-btn>
    </div>
  </template>
    <v-card-item style="padding-bottom: 0px;">
      <template v-slot:append>
        <v-btn icon size="40" flat>
            <v-icon icon="mdi-dots-vertical"></v-icon>
        </v-btn>
      </template>
      <v-card-title style="height: 60px;">
        <EmojiAvatar
          :icon="icon"
        />
        {{ userName }}
      </v-card-title>
    </v-card-item>
    <v-card-text style="padding-top: 1%; padding-bottom: 0;">
      <div class="post-card">
        <v-card class="gray-card" variant="outlined">
          <v-card-text class="text-center" style="font-size: 14px;">
            {{ content }}
          </v-card-text>
        </v-card>
      </div>
    </v-card-text>
    <v-card-text style="font-size: 12px; padding-top: 4px; padding-bottom: 2px;">
      <a>{{ time }} ago . {{ views }} views</a>
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
        default: "mdi-account-circle",
      },
      content: {
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
.btn-area {
  display: flex;
  justify-content: space-around;
  align-items: center;
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
.avatar {
  background-color: $second-background-color;
}
</style>

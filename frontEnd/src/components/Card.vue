<script setup>
  import EmojiAvatar from '@/components/EmojiAvatar.vue'
  import ImageAvatar from '@/components/ImageAvatar.vue'
</script>

<template>
  <v-card
    hover
    :style="`min-height: ${minHeight}; width: 97%; `" 
    border="xs"
  >
    <v-card-item>
    <template v-slot:append>
      <ImageAvatar
        :imgSrc="imgSrc"
      />
    </template>
    <template v-slot:prepend>
      <EmojiAvatar
        :icon="icon"
      />
    </template>
      <v-card-title>
        {{ title }}
      </v-card-title>
      <v-card-subtitle v-if="subtitle">{{ subtitle }}</v-card-subtitle>
    </v-card-item>
    <v-card-text v-if="text">{{ text }}</v-card-text>
  </v-card>
</template>

<script>
  export default {
    props: {
      title: {
        type: String,
        required: true,
      },
      subtitle: {
        type: String,
        default: "",
      },
      text: {
        type: String,
        default: null,
      },
      icon: {
        type: String,
        default: "🍄"
      },
      minHeight: {
        type: String,
        default: "150px"
      },
      imgSrc: {
        type: String,
        default: "https://www.svgrepo.com/download/287754/smartphone.svg"
      },
    },
  };
</script>

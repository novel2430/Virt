<template>
  <v-avatar size="50" class="avatar" rounded="circle" variant="elevated">
    <a style="font-size: 30px; color: #000000;">{{ icon }}</a>
  </v-avatar>
</template>

<script>
  export default {
    data: () => ({ 
    }),
    props: {
      icon: {
        type: String,
        default: "🍄",
      },
    },
  };
</script>

<style lang="scss" scoped>
.avatar {
  background-color: $second-background-color;
}
</style>

<template>
  <div class="area-box">
    <div>
      <v-btn icon class="icon-btn" size="60">
        <!-- <v-icon>{{ iconName }}</v-icon> -->
        <a style="font-size: 30px;">{{ iconName }}</a>
      </v-btn>
    </div>
    <div>
      <span class="title">{{ title }}</span>
    </div>
  </div>
</template>

<script>
  export default {
    data: () => ({ 
    }),
    props: {
      title: {
        type: String,
        default: "hello",
      },
      iconName: {
        type: String,
        default: "mdi-home",
      },
    },
  };
</script>

<style lang="scss" scoped>
.area-box {
  background-color: rgba(0,0,0,0);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: start;
  color: $text-color;
}
.icon-btn {
  background-color: $second-background-color;
}
.title {
  font-size: 16px;
}
</style>


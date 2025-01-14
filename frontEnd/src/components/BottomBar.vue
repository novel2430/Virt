<template>
  <v-bottom-navigation
      v-model="value"
      mode="shift"
    >
    <v-btn to="/">
      <v-icon>mdi-home-outline</v-icon>
      <span>家</span>
    </v-btn>

    <v-btn to="/ask">
      <v-icon>mdi-help-circle-outline</v-icon>
      <span>咨询</span>
    </v-btn>

    <v-btn to="/msg">
      <v-icon>mdi-forum-outline</v-icon>
      <span>信息</span>
    </v-btn>

    <v-btn to="/profile">
      <v-icon>mdi-account-outline</v-icon>
      <span>个人</span>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
  export default {
    data: () => ({ value: 1 }),
    computed: {
    },
    methods: {
    },
  };
</script>

<style lang="scss" scoped>
</style>

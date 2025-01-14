<script setup>
  import TopBar from '@/components/NavTopBar.vue'
</script>

<template>
  <!-- Top Bar -->
  <TopBar title="个人"/>
  <!-- Main Area -->
  <v-main>
    <v-container>
      <v-row>
        <v-col>
          <v-card flat class="d-flex justify-center profile-box">
            <v-card-item>
              <template v-slot:prepend>
                <v-avatar style="background-color: #ffffff;" size="100" rounded="circle" variant="elevated">
                  <a style="font-size: 70px; color: #000000;">{{ people.avatar }}</a>
                </v-avatar>
              </template>
              <v-card-title>{{ people.name }}</v-card-title>
              <v-card-subtitle>{{ people.id }}</v-card-subtitle>
            </v-card-item>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-list class="list" density="compact">
            <v-list-item
              v-for="(item, i) in items"
              :key="i"
              :value="item"
              class="list-item"
              color="orange"
            >
              <template v-slot:prepend>
                <v-icon :icon="item.icon"></v-icon>
              </template>
              <template v-slot:append>
                <v-icon>mdi-arrow-right-thick</v-icon>
              </template>
              <v-list-item-title v-text="item.text"></v-list-item-title>
            </v-list-item>
          </v-list>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
  export default {
    data: () => ({ 
      people: {
        name: "鲜香菇",
        id: "22421370",
        avatar: "🍄",
      },
      items: [
        { text: '资料', icon: 'mdi-account-outline' },
        { text: '积分', icon: 'mdi-cards-outline' },
        { text: '邀请码', icon: 'mdi-code-json' },
        { text: '收藏', icon: 'mdi-creation-outline' },
        { text: '设置', icon: 'mdi-tune' },
      ],
    }),
  };
</script>

<style lang="scss" scoped>
.profile-box {
  padding: 10px;
  background-color: $transparent;
  color: $text-color;
}
.list {
  background-color: $transparent;
}
.list-item {
  background-color: $transparent;
  padding: 20px;
}
</style>

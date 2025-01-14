<template>
  <v-text-field
      class="search"
      append-inner-icon="mdi-magnify"
      density="compact"
      label="Outlined"
      rounded
      variant="outlined"
      hide-details
      single-line
      bg-color="#ffffff"
      @click:append-inner="onClick"
    ></v-text-field>
</template>

<style lang="scss" scoped>
.search {
}
</style>

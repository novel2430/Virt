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
    <template v-slot:prepend>
      <ImageAvatar :imgSrc="imgSrc"/></template>
      <v-card-title class="title">
        {{ title }}
        <v-btn 
          class="btn-buy"
          rounded="xl"
          flat
          variant="outlined"
        >
          buy
        </v-btn>
      </v-card-title>
      <v-card-subtitle>
          <v-sheet
            elevation="2"
            rounded="xl"
            class="sheet"
          >
            <v-container>
              <v-row>
                <v-col class="col">
                  <a>{{ price }}元</a>
                </v-col>
              </v-row>
              <v-row>
                <v-col class="col">
                    <div class="word">
                      <a>{{ text }}</a>
                    </div>
                </v-col>
              </v-row>
            </v-container>
          </v-sheet>
      </v-card-subtitle>
    </v-card-item>
  </v-card>
</template>

<script>
  export default {
    props: {
      title: {
        type: String,
        required: true,
      },
      price: {
        type: String,
        default: "16",
      },
      text: {
        type: String,
        default: "Hello, World!",
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

<style lang="scss" scoped>
.title {
  display: flex; 
  text-align: center; 
  justify-content: space-between;
  margin-bottom: 5px;
  font-size: 20px;
}
.btn-buy {
  background-color: $primary-highlight-color; 
  border: 0px;
}
.sheet {
  background-color: $second-background-color; 
  margin-top: 0px;
  margin-bottom: 10px;
  padding-top: 20px;
  padding-bottom: 20px;
}
.col {
  padding-bottom: 0px;
  padding-top: 0px;
  font-size: 16px;
}
.word {
  word-wrap: break-word;
  white-space: normal;
  font-size: 12px;
}
</style>

import { createApp } from 'vue'
import router from './router';
import vuetify from './vuetify.js'

// Components
import App from './App.vue'

const app = createApp(App);

// Env
app.provide("apiHost", "http://127.0.0.1:5000")
// app.provide("apiHost", "https://www.yejsgk.top/ff")

app.use(router).use(vuetify).mount('#app')

import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/components/Home.vue';
import Ask from '@/components/ChatArea.vue';
import QuestionArea from '@/components/QuestionArea.vue';
import Message from '@/components/Messages.vue'
import Profile from '@/components/Profile.vue'
import DayQuestion from '@/components/DayQuestion.vue'
import ArtTherapy from '@/components/ArtTherapy.vue'
import Store from '@/components/Store.vue'

const appName = '解忧旅社';

const buildWebPageName = function(title) {
  return title + ' - ' + appName;
};

const routes = [
  // Main Page
  { path: '/', name: buildWebPageName('首页'), component: Home },
  { path: '/ask', name: buildWebPageName('咨询'), component: Ask },
  { path: '/msg', name: buildWebPageName('信息'), component: Message },
  { path: '/profile', name: buildWebPageName('个人'), component: Profile },
  // Child Page
  { path: '/question-area', name: buildWebPageName('倾诉解答'), component: QuestionArea },
  { path: '/day-question', name: buildWebPageName('每日一问'), component: DayQuestion },
  { path: '/art-therapy', name: buildWebPageName('艺术治疗'), component: ArtTherapy },
  { path: '/nice-store', name: buildWebPageName('温暖小店'), component: Store },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  document.title = to.name; // 使用路由名称作为页面标题
  next();
});

export default router;


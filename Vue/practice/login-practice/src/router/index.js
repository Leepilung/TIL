import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import DashBoard from '../views/DashBoard.vue';

const routes = [
  {
    path: '/',
    name: 'HhomeView',
    component: HomeView,
  },
  {
    path: '/dashboard',
    name: 'DashBoard',
    component: DashBoard,
  },
  {
    path: '/:PathMatch(.*)',
    name: 'not-found',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/ErrorView.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
  },
  {
    path: '/basic',
    name: 'basic',
    component: () =>
      import(
        /* webpackChunkName: "contact", webpackPrefetch:true */ '../views/BasicView.vue'
      ),
  },
  {
    path: '/contact',
    name: 'contact',
    component: () =>
      import(/* webpackChunkName: "contact" */ '../views/ContactView.vue'),
  },
  {
    path: '/databinding',
    name: 'Databinding',
    component: () => import('../views/DatabindingView.vue'),
  },
  {
    path: '/example',
    name: 'Example',
    component: () => import('../views/ExampleView.vue'),
  },
  {
    path: '/example2',
    name: 'ExampleTwo',
    component: () => import('../views/ExampleTwoView.vue'),
  },
  {
    path: '/rendering',
    name: 'RenderingView',
    component: () => import('../views/RenderingView.vue'),
  },
  {
    path: '/event',
    name: 'EventView',
    component: () => import('../views/EventView.vue'),
  },
  {
    path: '/computed',
    name: 'ComputedView',
    component: () => import('../views/ComputedView.vue'),
  },
  {
    path: '/watch',
    name: 'WatchView',
    component: () => import('../views/WatchView.vue'),
  },
  {
    path: '/inquiry',
    name: 'InquiryView',
    component: () => import('../views/InquiryView.vue'),
  },
  {
    path: '/save',
    name: 'SaveView',
    component: () => import('../views/SaveView.vue'),
  },
  {
    path: '/server',
    name: 'ServerData',
    component: () => import('../views/ServerData.vue'),
  },
  {
    path: '/component',
    name: 'ComponentView',
    component: () => import('../views/ComponentView.vue'),
  },
  {
    path: '/slot',
    name: 'SlotUseModalLayout',
    component: () => import('../views/SlotUseModalLayout.vue'),
  },
  {
    path: '/project',
    name: 'ProvideInject',
    component: () => import('../views/ProvideInject.vue'),
  },
];
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

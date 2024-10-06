import { createRouter, createWebHistory } from 'vue-router';
import TransactionsProductsList from '../components/TransactionsProductsList.vue';
import SubscribeComponent from '../components/SubscribeComponent.vue';
import EditClientInfo from '../components/EditClientInfo.vue';

const routes = [
  {
    path: '/',
    component: TransactionsProductsList,
  },
  {
    path: '/subscribe',
    component: SubscribeComponent,
  },
  {
    path: '/edit-client',
    component: EditClientInfo,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

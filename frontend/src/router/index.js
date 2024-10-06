import { createRouter, createWebHistory } from 'vue-router';
import MainComponent from "../components/MainComponent.vue";
import TransactionsProductsList from '../components/TransactionsProductsList.vue';
import SubscribeComponent from '../components/SubscribeComponent.vue';
import EditClientInfo from '../components/EditClientInfo.vue';

const routes = [
  {
    path: '/',
    name: 'MainComponent',
    component: MainComponent
  },
  {
    path: '/listados',
    name: 'TransactionsProductsList',
    component: TransactionsProductsList
  },
  {
    path: '/suscribir',
    name: 'SubscribeComponent',
    component: SubscribeComponent
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

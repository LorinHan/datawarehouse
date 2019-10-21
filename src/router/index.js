import Vue from 'vue'
import Router from 'vue-router'
const Home = r => require.ensure([], () => r(require('@/components/pages/Home')), 'chunkname1');
const Maps = r => require.ensure([], () => r(require('@/components/pages/Map')), 'chunkname2');
const Cities = r => require.ensure([], () => r(require('@/components/pages/Cities')), 'chunkname3');
const Price = r => require.ensure([], () => r(require('@/components/pages/Price')), 'chunkname4');

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/map',
      name: 'Map',
      component: Maps
    },
    {
      path: '/cities',
      name: 'Cities',
      component: Cities
    },
    {
      path: '/price',
      name: 'Price',
      component: Price
    }
  ]
})

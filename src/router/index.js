import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    components: {
      default: ()=> Home,
      nav: ()=> import( '../components/header.vue'),
    }
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    components: {
      default: ()=> import( '../views/About.vue'),
      nav: ()=> import( '../components/header.vue'),
    }
  },

  {
    path: '/test',
    name: 'Test',
    components: {
      default: ()=> import( '../views/Test.vue'),
      nav: ()=> import( '../components/header.vue'),
    }  },
 
  {
    path: '/userinfo',
    name: 'userinfo',
    components: {
      default: ()=> import( '../views/Userinfo.vue'),
      nav: ()=> import( '../components/header.vue'),
    }
  },
  {
    path: '/ProductInfo',
    name: 'ProductInfo',
    components: {
      default: ()=> import( '../views/ProductInfo.vue'),
      nav: ()=> import( '../components/header.vue'),
    }
  },
  {
    path: '/Shopcart',
    name: 'Shopcart',
    components: {
      default: ()=> import( '../views/Shopcart.vue'),
      nav: ()=> import( '../components/header.vue'),
    }
  },
  {
    path: '/:catchAll(.*)',
    components: {
      default: ()=> import( '../views/error.vue'),
      nav: ()=> import( '../components/header.vue'),
    }
    //component: () => import('../views/error.vue')
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

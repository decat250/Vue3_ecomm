import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'


const routes = [
  {
    path: '/adm',
    name: 'Admin',
    components: {
      nav: () => import('../views/adm/Login.vue'),
    }
  },
  {
    path: '/admindex',
    name: 'admindex',
    components: {
      nav: () => import('../views/adm/header.vue'),
      default: () => import('../views/adm/index.vue'),
    },

    children: [
      {
        path: "product",
        component: () => import("../views/adm/product.vue")
      },
      {
        path: "user",
        component: () => import("../views/adm/user.vue")
      },
      {
        path: "banner",
        component: () => import("../views/adm/banner.vue")
      },
      {
        path: "type",
        component: () => import("../views/adm/type.vue")
      },
      {
        path: "orderadm",
        component: () => import("../views/adm/orderadm.vue")
      },
      {
        path: "order_itemadm/:id",
        component: () => import("../views/adm/order_itemadm.vue")
      },
    ]
  },
  {
    path: '/',
    name: 'Home',
    components: {
      default: () => Home,
      nav: () => import('../components/header.vue'),
    }
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    components: {
      default: () => import('../views/About.vue'),
      nav: () => import('../components/header.vue'),
    }
  },

  {
    path: '/test',
    name: 'Test',
    components: {
      default: () => import('../views/Test.vue'),
      nav: () => import('../components/header.vue'),
    }
  },
  {
    path: '/question/',
    name: 'Question',
    components: {
      default: () => import('../views/qa.vue'),
      nav: () => import('../components/header.vue'),
    }
  },
  {
    path: '/success/',
    name: 'Success',
    components: {
      default: () => import('../views/success.vue'),
      nav: () => import('../components/header.vue'),
    }
  },
  {
    path: '/order_item/:id',
    name: 'order_item',
    components: {
      default: () => import('../views/order_item.vue'),
      nav: () => import('../components/header.vue'),
    }
  },
  {
    path: '/failed/',
    name: 'Failed',
    components: {
      default: () => import('../views/failed.vue'),
      nav: () => import('../components/header.vue'),
    }
  },
  {
    path: '/order/',
    name: 'Order',
    components: {
      default: () => import('../views/order.vue'),
      nav: () => import('../components/header.vue'),
    }
  },
  {
    path: '/form/',
    name: 'Form',
    components: {
      default: () => import('../views/Form.vue'),
      nav: () => import('../components/header.vue'),
    }
  },
  {
    path: '/userinfo',
    name: 'userinfo',
    components: {
      default: () => import('../views/Userinfo.vue'),
      nav: () => import('../components/header.vue'),
    }
  },
  {
    path: '/ProductInfo/:id',
    name: 'ProductInfo',
    components: {
      default: () => import('../views/ProductInfo.vue'),
      nav: () => import('../components/header.vue'),
    }
  },
  {
    path: '/Shopcart',
    name: 'Shopcart',
    components: {
      default: () => import('../views/Shopcart.vue'),
      nav: () => import('../components/header.vue'),
    }
  },
  {
    path: '/cvs_get/:CVSStoreID/:CVSStoreName/:CVSAddress',
    name: 'cvs_get',
    components: {
      default: () => import('../views/cvs_get.vue'),
    }
  },
  {
    path: '/table',
    name: 'Table',
    components: {
      nav: () => import('../views/table.vue'),
    }
  },
  {
    path: '/:catchAll(.*)',
    components: {
      default: () => import('../views/error.vue'),
      nav: () => import('../components/header.vue'),
    }
    //component: () => import('../views/error.vue')
  }

]

export const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import naive from 'naive-ui'

import "bootstrap/dist/css/bootstrap.min.css"

import 'vfonts/Lato.css'

import "bootstrap"

  

const app = createApp(App)
//test
/*
router.beforeEach((to, from, next)=>{
    const isLogin = localStorage.getItem('token') == 'ImLogin' ;
    if( isLogin ){
      next();
    } else {
      if( to.path !== '/login')
        next('/login');
      else
        next();
    }
  });
*/
app.use(router)
app.use(naive)
app.mount('#app')

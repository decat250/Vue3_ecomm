import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import naive from 'naive-ui'
import GAuth from 'vue3-google-oauth2'

import "bootstrap/dist/css/bootstrap.min.css"

import 'vfonts/Lato.css'

import "bootstrap"

import "ecpay_aio_nodejs"

const gAuthOptions = { clientId: '617585413164-r67padapiur3n6f9p2m9h9lkt2nomh45.apps.googleusercontent.com', scope: 'email', prompt: 'consent', fetch_basic_profile: false }

const app = createApp(App)
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
app.use(GAuth, gAuthOptions)

app.use(router)
app.use(naive)
app.mount('#app')

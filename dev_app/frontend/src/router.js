// import Vue from 'vue'
import {createRouter, createWebHashHistory} from 'vue-router'
import Home from './components/modules/Home.vue'
import Routing from './components/modules/MyInstruction.vue'

// Vue.use(VueRouter)
const rootes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/routing',
        name: 'routing',
        component: Routing
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes: rootes
})

export default router

    

import { createRouter, createWebHistory } from 'vue-router';
import DeckView from '@/views/DeckView'
import AboutView from '@/views/AboutView'

const routes = [
    {
        path: '/',
        name: 'decks',
        component: DeckView
    },
    {
        path: '/decks',
        name: 'decks',
        component: DeckView
    },
    {
        path: '/about',
        name: 'about',
        component: AboutView
    }

]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
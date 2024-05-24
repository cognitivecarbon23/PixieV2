import { createApp } from 'vue'
import LoginComponent from './components/LoginComponent.js';

createApp({
    components: {
        'login-component': LoginComponent
    }
}).mount('#app');
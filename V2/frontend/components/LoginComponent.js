export default {
    data() {
        return {
            username: '',
            password: ''
        };
    },
    methods: {
        login() {
            fetch('http://localhost:3000/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: this.username,
                    password: this.password
                })
            })
                .then(response => response.json())
                .then(data => {
                    if (data.access_token) {
                        localStorage.setItem('jwt', data.access_token);
                        window.location.href = '/hello';
                    } else {
                        alert('Login failed: ' + (data.msg || 'Unknown error'));
                    }
                })
                .catch(error => {
                    console.error('Error logging in:', error);
                    alert('Login failed: ' + error.message);
                });
        }
    },
    template: `
        <div>
            <input v-model="username" placeholder="Username">
            <input type="password" v-model="password" placeholder="Password">
            <button @click="login">Login</button>
        </div>
    `
};
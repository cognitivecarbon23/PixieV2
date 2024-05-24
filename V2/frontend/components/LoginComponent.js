export default {
    template: `
    <div>
      <h1>Login</h1>
      <input v-model="username" placeholder="Username">
      <input type="password" v-model="password" placeholder="Password">
      <button @click="login">Login</button>
    </div>
  `,
    data() {
        return {
            username: '',
            password: ''
        };
    },
    methods: {
        login() {
            // Your login logic here
        }
    }
};

import os

# Define project structure
project_structure = {
    'project_name': 'V2',
    'folders': [
        'backend',
        'backend/routes',
        'frontend',
        'frontend/components',
        'frontend/styles',
        'frontend/assets'
    ],
    'files': {
        'backend/server.js': r'''
const express = require('express');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const cors = require('cors');

const app = express();
const PORT = 3000;
const SECRET_KEY = 'your_secret_key';

app.use(bodyParser.json());
app.use(cors());

const users = [{ username: 'user', password: 'pass' }];

app.post('/api/login', (req, res) => {
    const { username, password } = req.body;
    const user = users.find(u => u.username === username && u.password === password);

    if (user) {
        const token = jwt.sign({ username: user.username }, SECRET_KEY, { expiresIn: '1h' });
        res.json({ access_token: token });
    } else {
        res.status(401).json({ msg: 'Invalid credentials' });
    }
});

app.get('/api/hello', (req, res) => {
    res.json({ message: 'Hello, world!' });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
        ''',
        'frontend/index.html': r'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="styles/style.css">
    <script src="https://unpkg.com/vue@3.2.31"></script>
</head>
<body>
    <div id="app"></div>
    <script src="main.js"></script>
</body>
</html>
        ''',
        'frontend/main.js': r'''
import { createApp } from 'vue';
import LoginComponent from './components/LoginComponent.js';

createApp({
    components: {
        'login-component': LoginComponent
    }
}).mount('#app');
        ''',
        'frontend/components/LoginComponent.js': r'''
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
        ''',
        'frontend/components/HelloComponent.js': r'''
export default {
    template: '<div>Hello, world!</div>'
};
        ''',
        'frontend/styles/style.css': r'''
body {
    font-family: Arial, sans-serif;
}
.main-login {
    max-width: 300px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
    text-align: center;
}
.login-button {
    display: block;
    width: 100%;
    padding: 10px;
    margin-top: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
        '''
    }
}

# Create project structure
os.makedirs(project_structure['project_name'], exist_ok=True)

for folder in project_structure['folders']:
    os.makedirs(os.path.join(project_structure['project_name'], folder), exist_ok=True)

for file_path, file_content in project_structure['files'].items():
    full_path = os.path.join(project_structure['project_name'], file_path)
    with open(full_path, 'w') as file:
        file.write(file_content.strip())

# Change directory to project
os.chdir(project_structure['project_name'])

print("Please run the following commands manually:")
print("npm init -y")
print("npm install express body-parser jsonwebtoken cors webpack webpack-cli vue-loader vue-template-compiler css-loader style-loader babel-loader @babel/core @babel/preset-env")

# Create webpack.config.js
with open('webpack.config.js', 'w') as webpack_config:
    webpack_config.write(r'''
const path = require('path');
const { VueLoaderPlugin } = require('vue-loader');

module.exports = {
    mode: 'development',  // Set mode to 'development'
    entry: './frontend/main.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist')
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env']
                    }
                }
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            }
        ]
    },
    resolve: {
        alias: {
            vue: 'vue/dist/vue.esm-bundler.js'
        }
    },
    plugins: [
        new VueLoaderPlugin()
    ],
    devServer: {
        contentBase: path.join(__dirname, 'frontend'),
        compress: true,
        port: 8080
    }
};
    ''')

# Run webpack to build the frontend
print("Please run the following command manually:")
print("npx webpack")

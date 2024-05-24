const path = require('path');
const { VueLoaderPlugin } = require('vue-loader');

module.exports = {
    mode: 'development',
    entry: './V2/frontend/main.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'V2', 'dist')
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
        static: path.join(__dirname, 'V2', 'frontend'), // Use 'static' instead of 'contentBase'
        compress: true,
        port: 8080
    }
};

const path = require('path');

module.exports = {
  entry: path.join(__dirname, "properties", "ui", "index.tsx"),
  output: {
    path:path.resolve(__dirname, "properties", "static", "js"),
  },
  module: {
    rules: [
      {
        test: /\.?ts|tsx$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react', '@babel/preset-typescript']
          }
        }
      },
    ]
  },
}
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const ESlintPlugin = require("eslint-webpack-plugin");
const path = require("path");
const webpack = require("webpack");

const serverConfig = {
	mode: process.env.ENV || "development",
	entry: path.resolve(__dirname, "./src/index.js"),
	output: {
		path: path.join(__dirname, "/dist"),
		filename: "[name].js",
	},
	resolve: {
		extensions: ["*", ".js", ".jsx"],
	},
	module: {
		rules: [
			{
				test: /\.js$/,
				exclude: /node_modules/,
				use: {
					loader: "babel-loader",
				},
			},
			{
				test: /\.(css|sass|scss)$/,
				use: ["style-loader", "css-loader", "sass-loader"],
			},
			{
				test: /\.(png|jpe?g|gif)$/,
				use: [
					{
						loader: "file-loader",
					},
				],
			},
		],
	},
	plugins: [
		new webpack.HotModuleReplacementPlugin(),
		new CleanWebpackPlugin(),
		new HtmlWebpackPlugin({
			template: "public/index.html",
		}),
		new ESlintPlugin({
			extensions: ["js", "jsx"],
		}),
	],
	devServer: {
		contentBase: path.resolve(__dirname, "./dist"),
		hot: true,
	},
};

module.exports = serverConfig;

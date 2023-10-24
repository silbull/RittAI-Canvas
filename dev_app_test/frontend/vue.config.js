const { defineConfig } = require('@vue/cli-service')
const path = require("path");
module.exports = defineConfig({
  transpileDependencies: true,
  assetsDir: "static",
  outputDir: path.resolve(__dirname, "../backend/app/dist"),
})

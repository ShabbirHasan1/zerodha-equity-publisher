
module.exports = {
  filenameHashing: false,
  devServer: {
    proxy: {
      '^/api': {
        target: process.env.BACKEND_URL,
        changeOrigin: true
      },
    }
  }
}
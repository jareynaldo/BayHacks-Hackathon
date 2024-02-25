const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

// Proxy configuration
const proxyOptions = {
  target: 'https://pypi.org',
  changeOrigin: true,
  // Add additional headers if needed
  headers: {
    'Access-Control-Allow-Origin': '*',
    // Add other headers if needed
  },
};

// Create the proxy
const apiProxy = createProxyMiddleware('/', proxyOptions);

// Use the proxy for all requests
app.use(apiProxy);

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Proxy server listening on http://localhost:${port}`);
});

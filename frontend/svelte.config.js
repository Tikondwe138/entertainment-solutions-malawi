import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

const config = {
  // Preprocessing (TypeScript, PostCSS, etc.)
  preprocess: vitePreprocess(),

  kit: {
    adapter: adapter(),
    alias: {
      $lib: 'src/lib',
      $routes: 'src/routes',
      $stores: 'src/stores',
      $assets: 'src/assets'
    },
    // If backend API runs on another port (e.g., FastAPI at 8000)
    vite: {
      server: {
        proxy: {
          '/api': 'http://localhost:8000'
        }
      }
    }
  }
};

export default config;

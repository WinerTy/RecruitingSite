import process from 'node:process'
import { defineNuxtConfig } from 'nuxt/config'
import magnetConfig from './config/magnet'
import scooterConfig from './config/scooter'

const siteConfigs = {
  scooter: scooterConfig,
  magnet: magnetConfig,
}

const siteConfig = siteConfigs[process.env.SITE as keyof typeof siteConfigs]

if (!siteConfig) {
  throw new Error(`Unknown site: ${process.env.SITE}`)
}

export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  ssr: true,
  devtools: {
    enabled: true,
  },
  modules: [
    '@pinia/nuxt',
    '@nuxt/eslint',
  ],
  imports: {
    autoImport: true,
    dirs: ['./utils/', './utils/api', './store/'],
  },
  eslint: {
    config: {
      standalone: false,
    },
  },
  runtimeConfig: {
    public: {
      siteConfig,
    },
  },
})

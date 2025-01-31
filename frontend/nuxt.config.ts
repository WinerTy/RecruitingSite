import process from 'node:process'
import { defineNuxtConfig } from 'nuxt/config'
import magnetConfig from './config/magnet'
import scooterConfig from './config/scooter'

const siteConfigs = {
  scooter: scooterConfig,
  magnet: magnetConfig,
}

const siteStyles = {
  scooter: 'assets/scss/site-variables/scooter.scss',
  magnet: 'assets/scss/site-variables/magnet.scss',
}

const siteConfig = siteConfigs[process.env.SITE as keyof typeof siteConfigs]
const siteStyle = siteStyles[process.env.SITE as keyof typeof siteStyles]

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
    '@nuxtjs/i18n',
  ],
  i18n: {
    locales: [
      {
        code: 'ru',
        file: `${process.env.SITE}/ru.json`,
      },
      {
        code: 'tg',
        file: `${process.env.SITE}/tg.json`,
      },
    ],
    defaultLocale: 'ru',
  },
  imports: {
    autoImport: true,
    dirs: ['./utils/', './utils/api', './store/'],
  },
  eslint: {
    config: {
      standalone: false,
    },
  },
  css: [
    '~/assets/scss/index.scss',
    siteStyle,
  ],
  runtimeConfig: {
    public: {
      siteConfig,
    },
  },
})

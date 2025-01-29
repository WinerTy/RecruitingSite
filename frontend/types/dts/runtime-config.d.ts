declare module 'nuxt/schema' {
  interface RuntimeConfig {
    public: {
      siteConfig: {
        site_id: number
        name: string
        theme: string
        logo: string
        apiUrl: string
      }
    }
  }
}
export { }

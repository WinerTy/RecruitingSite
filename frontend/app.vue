<script setup lang="ts">
const {
  public: { siteConfig: config },
} = useRuntimeConfig()
</script>

<template>
  <div>
    <h1>{{ config.site_id }}</h1>
    <h1>{{ config.name }}</h1>
  </div>
</template>


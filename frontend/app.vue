<script setup lang="ts">
const {
  public: { siteConfig: config },
} = useRuntimeConfig()

const { locale, locales, setLocale } = useI18n()

const selectedLocale = ref(locale.value)

function changeLanguage() {
  setLocale(selectedLocale.value)
}
</script>

<template>
  <div>
    <h1>{{ config.site_id }}</h1>
    <h1>{{ $t('welcome') }}</h1>
  </div>
  <div>
    <select v-model="selectedLocale" @change="changeLanguage">
      <option v-for="locale in locales" :key="locale.code" :value="locale.code">
        {{ locale.code }}
      </option>
    </select>
  </div>
</template>

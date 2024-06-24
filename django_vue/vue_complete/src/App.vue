
<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <header>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink :to="{name : 'articles'}">Articles</RouterLink>
      <RouterLink :to="{name : 'articles-create'}">Create</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>

<style scoped>
header{
  margin-bottom: 3rem;
}
</style>

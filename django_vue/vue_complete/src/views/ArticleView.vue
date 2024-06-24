<template>
  <div>
    <button @click="fetchArticles">articles 가져오기</button>
    <ul>
      <li v-for="article in articleStore.articles">
        <h2>{{ article.title }}</h2>
        <p>{{ article.content }}</p>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useArticleStore } from '/src/stores/articles'
import { onMounted } from 'vue'
const articleStore = useArticleStore()


function fetchArticles() {
  articleStore.fetchArticles()
}

onMounted(() => {
  // fetchArticles()
})

</script>

<style lang="scss" scoped>

</style>
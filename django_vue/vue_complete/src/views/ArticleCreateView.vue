<template>
  <div>
    <form @submit.prevent="createArticle">
    <label for="title">title : </label>
    <input type="text" name="title" id="title" v-model="data.title"><br>
    <label for="content">content : </label>
    <textarea name="content" id="content" cols="30" rows="10" v-model="data.content"></textarea><br>
    <button type="submit">submit</button>
    </form>
  </div>
</template>

<script setup>
import { useArticleStore } from '/src/stores/articles'
import { reactive } from 'vue'

const articleStore = useArticleStore()

const data = reactive({
  title: '',
  content: ''
})

function createArticle() {
  articleStore.createArticle(data)
  
}
</script>

<style lang="scss" scoped>

</style>
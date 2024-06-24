import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
  
  const articles = ref([])

  function fetchArticles() {
    axios({
      url : 'http://127.0.0.1:8000/articles/'
    })
      .then(response => {
        articles.value = response.data
      })
      .catch(error => console.error(error))
  }

  function createArticle(data) {
    axios({
      url : 'http://127.0.0.1:8000/articles/',
      method : 'POST',
      data : data
    })
  }
  
  return { articles, fetchArticles, createArticle}
})

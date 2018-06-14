<template>
  <h2 class="page-title">
    <slot>Page Title</slot>
  </h2>
</template>

<script>
export default {
  name: 'PageTitle'
}
</script>

<style lang="scss" scoped>
.page-title {
  color: #99a9bf;
  font-size: 1.3rem;
  font-weight: normal;
  border-bottom: 1px solid #eaecef;
  margin: {
    top: 0;
    bottom: 20px;
  }
  padding: {
    bottom: 15px;
  }
}
</style>

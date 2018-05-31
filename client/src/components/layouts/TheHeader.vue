<template>
  <ElHeader class="header">
    <h1 class="brand">
      <router-link to="/">
        BINSPDT
      </router-link>
    </h1>

    <nav class="nav">
      <ElMenu
        mode="horizontal"
        :default-active="`/${$route.path.split('/')[1]}`"
        :router="true">
          <ElMenuItem index="/">{{ $t('routes.home') }}</ElMenuItem>

          <ElMenuItem index="/binary">{{ $t('routes.binary') }}</ElMenuItem>

          <ElMenuItem index="/source">{{ $t('routes.source') }}</ElMenuItem>
      </ElMenu>
    </nav>
  </ElHeader>
</template>

<script>
export default {
  name: 'TheHeader'
}
</script>

<style lang="scss" scoped>
.header {
  .brand {
    font-family: 'Libre Franklin';
    a {
      color: black;
      text-decoration: none;
    }
  }
  padding: 0 2rem;
  border-bottom: solid 1px #e6e6e6;
  .brand {
    float: left;
  }
  .nav {
    float: right;
  }
}
</style>

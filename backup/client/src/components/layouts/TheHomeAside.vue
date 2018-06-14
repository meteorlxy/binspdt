<template>
  <ElAside>
    <ElMenu
      :default-active="$route.path"
      :router="true">
      <ElMenuItem index="/">
        <i class="el-icon-setting"></i>

        <span>{{ $t('routes.home') }}</span>
      </ElMenuItem>

      <ElMenuItem index="/binary">
        <i class="el-icon-news"></i>

        <span>{{ $t('routes.binary') }}</span>
      </ElMenuItem>

      <ElMenuItem index="/source">
        <i class="el-icon-document"></i>

        <span>{{ $t('routes.source') }}</span>
      </ElMenuItem>
    </ElMenu>
  </ElAside>
</template>

<script>
export default {
  name: 'TheHomeAside'
}
</script>

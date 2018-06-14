<template>
  <ElAside>
    <ElMenu
      :default-active="$route.path"
      :router="true">
      <ElMenuItem index="/binary/modules">
        <i class="el-icon-menu"></i>{{ $t('routes.modules') }}
      </ElMenuItem>

      <ElSubmenu index="1">
        <template slot="title"><i class="el-icon-zoom-in"></i>{{ $t('routes.analysis') }}</template>

        <ElMenuItem index="/analysis/basic_block">{{ $t('routes.basic_block') }}</ElMenuItem>
      </ElSubmenu>
    </ElMenu>
  </ElAside>
</template>

<script>
export default {
  name: 'TheSourceAside'
}
</script>

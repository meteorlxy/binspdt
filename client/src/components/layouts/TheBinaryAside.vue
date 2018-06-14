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

        <ElMenuItem index="/binary/analysis/api">{{ $t('routes.api') }}</ElMenuItem>
      </ElSubmenu>

      <ElMenuItem index="/binary/results">
        <i class="el-icon-tickets"></i>{{ $t('routes.results') }}
      </ElMenuItem>
    </ElMenu>
  </ElAside>
</template>

<script>
export default {
  name: 'TheBinaryAside'
}
</script>
